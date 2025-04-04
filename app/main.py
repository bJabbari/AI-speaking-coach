import os
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from io import BytesIO

from app.models.response_generator import generate_response

load_dotenv()
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")


@app.post("/generate")
async def generate_api_response(
        file: UploadFile = File(...),
        band: str = Form(...),
        api_key: str = Form(default=None)
):
    try:
        image_data = await file.read()
        image = Image.open(BytesIO(image_data)).convert("RGB")

        result = generate_response(image, band, api_key)

        return JSONResponse(content={
            "caption": result["caption"],
            "speaking_response": result["response"],
            "band": band,
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
