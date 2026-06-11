import os
import json
import base64
import logging
import uuid
from datetime import datetime
from io import BytesIO
from PIL import Image
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from typing import Dict, Any

from app.models.schemas import AnalyzeRequest
from app.core.config import settings

logger = logging.getLogger(__name__)

class AIDetectorService:
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            logger.warning("GEMINI_API_KEY is missing.")
        
        genai.configure(api_key=settings.GEMINI_API_KEY)
        
        self.safety_settings = {
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        }

        self.model = genai.GenerativeModel(
            'gemini-2.5-flash', 
            generation_config={"response_mime_type": "application/json"}
        )

    def run_analysis(self, payload: AnalyzeRequest) -> Dict[str, Any]:
        prompt = """
        You are an expert cybersecurity and UX analyst. Analyze the provided URL, text, and/or screenshot for deceptive UX (dark patterns) and phishing indicators.
        
        Return ONLY a valid JSON object matching this exact structure:
        {
          "ai_summary": "string (A detailed, professional 2-3 sentence threat analysis explaining exactly what is happening and why it is dangerous or safe)",
          "recommendation": "string (Actionable advice on what the user should do next, e.g., 'Close the tab immediately' or 'Safe to browse')",
          "detected_patterns": [
            {
              "pattern_name": "string (e.g., forced_action, hidden_costs, urgency, misdirection)",
              "confidence": float (0.0 to 1.0),
              "severity": "string (low, medium, high)",
              "evidence": ["string array explaining exactly what triggered this"]
            }
          ],
          "risk_score": { "overall": integer (0-100), "level": "string (low, medium, high)" },
          "trust_score": { "overall": integer (0-100), "level": "string (low, medium, high)" },
          "phishing_analysis": {
            "is_phishing": boolean,
            "probability": float (0.0 to 1.0),
            "risk_level": "string (low, medium, high)"
          }
        }
        """

        contents = [prompt]
        
        if payload.url:
            contents.append(f"URL: {payload.url}")
        if payload.text:
            contents.append(f"Page Text: {payload.text}")

        if payload.screenshot_base64 and len(payload.screenshot_base64) > 100:
            try:
                base64_str = payload.screenshot_base64
                if ',' in base64_str:
                    base64_str = base64_str.split(',')[1]
                image_data = base64.b64decode(base64_str)
                img = Image.open(BytesIO(image_data))
                contents.append(img)
            except Exception as e:
                logger.error(f"Image decode error: {e}")

        try:
            response = self.model.generate_content(contents, safety_settings=self.safety_settings)
            
            clean_text = response.text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:-3]
            elif clean_text.startswith("```"):
                clean_text = clean_text[3:-3]
                
            ai_data = json.loads(clean_text)
            
            ai_data["scan_id"] = str(uuid.uuid4())
            ai_data["timestamp"] = datetime.utcnow().isoformat()
            ai_data["url"] = str(payload.url) if payload.url else None
            
            return ai_data
            
        except Exception as e:
            print(f"\n[!!!] AI ERROR: {str(e)}\n")
            return self._get_fallback_response(payload)

    def _get_fallback_response(self, payload: AnalyzeRequest) -> Dict[str, Any]:
        return {
            "scan_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "url": str(payload.url) if payload.url else None,
            "ai_summary": "Analysis failed or timed out. Unable to generate threat report.",
            "recommendation": "Proceed with caution. Manual verification recommended.",
            "detected_patterns": [],
            "risk_score": {"overall": 0, "level": "low"},
            "trust_score": {"overall": 100, "level": "high"},
            "phishing_analysis": {"is_phishing": False, "probability": 0.0, "risk_level": "low"}
        }

detector_service = AIDetectorService()
