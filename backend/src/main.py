# from ocr_module import extract_text_from_image
# from search_module import search_google
# from parse_module import load_responses, parse_response

# backend/src/main.py (FastAPI Backend)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="BeanThereScannedThat",
    description="This is the backend for the BeanThereScannedThat application, which processes coffee-related data using OCR and search functionalities.",
    version="1.0",
    openapi_prefix="/api"
)

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "FastAPI Backend Running!"
    }

@app.get("/coffee")
def get_coffee():
    return {"name": "Ethiopian Yirgacheffe", "origin": "Ethiopia"}
