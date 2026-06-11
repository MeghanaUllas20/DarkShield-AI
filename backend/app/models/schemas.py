from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Any
from datetime import datetime

class PatternEvidence(BaseModel):
    pattern_name: str
    confidence: float
    severity: str
    evidence: List[str]

class RiskScore(BaseModel):
    overall: int
    level: str

class PhishingAnalysis(BaseModel):
    is_phishing: bool
    probability: float
    risk_level: str

class AnalyzeRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[HttpUrl] = None
    screenshot_base64: Optional[str] = None

class AnalyzeResponse(BaseModel):
    scan_id: str
    timestamp: datetime
    url: Optional[str]

    ai_summary: str 
    recommendation: str

    
    detected_patterns: List[PatternEvidence]
    risk_score: RiskScore
    trust_score: RiskScore
    phishing_analysis: PhishingAnalysis

class PatternDetail(BaseModel):
    name: str
    description: str

    examples: List[str]
