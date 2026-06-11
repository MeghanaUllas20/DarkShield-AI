from fastapi import APIRouter, HTTPException, Path
from typing import List
from app.models.schemas import AnalyzeRequest, AnalyzeResponse, PatternDetail
from app.services.detector import detector_service
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_endpoint(request: AnalyzeRequest):
    try:
        # The AI returns a dict that perfectly matches AnalyzeResponse
        result_dict = detector_service.run_analysis(request)
        return AnalyzeResponse(**result_dict)
    except Exception as e:
        logger.error(f"Endpoint error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during analysis.")

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "DarkShield AI Multimodal Backend"}

# --- Mocked Endpoints below for UI structure ---

@router.get("/patterns/library", response_model=List[PatternDetail])
async def get_pattern_library():
    return [
        {"name": "forced_action", "description": "Forcing user action to proceed.", "examples": []},
        {"name": "urgency", "description": "Fake timers or stock warnings.", "examples": []}
    ]

@router.get("/patterns/{pattern_name}")
async def get_pattern_details(pattern_name: str = Path(...)):
    return {"name": pattern_name, "description": f"Details for {pattern_name}", "examples": []}

@router.get("/history")
async def get_history():
    return {"history": []}