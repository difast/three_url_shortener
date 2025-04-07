from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.url import ShortURL
from app.services.shortener import generate_short_code, calculate_expiry
from app.database import get_db
from app.schemas.url import URLShortenRequest
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/shorten")
def shorten_url(request: URLShortenRequest, db: Session = Depends(get_db)):
    # Логика сокращения URL
    pass

@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    # Логика перенаправления
    pass