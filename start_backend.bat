@echo off
echo Starting NCERT Doubt Explainer Backend...
cd backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
pause