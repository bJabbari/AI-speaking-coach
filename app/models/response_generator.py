from app.models.blip1_captioner import generate_caption
from app.models.llm_utils import generate_speaking_response

from PIL import Image


def generate_response(image: Image.Image, band: str, api_key=None) -> dict:
    caption = generate_caption(image)
    response = ""
    if api_key is not None:
        response = generate_speaking_response(caption, band, api_key)
    return {
        "caption": caption,
        "response": response
    }
