from dotenv import load_dotenv
import cloudinary
import os

load_dotenv()

cloudinary.config(
    cloud_name = os.getenv("CLOUD_NAME"),
    api_key = os.getenv("CLOUD_API"),
    api_secret = os.getenv("CLOUD_SECRET")
)

import cloudinary.uploader

async def upload_image():
    """
    Uploads the generated image to Cloudinary.
    """
    response = cloudinary.uploader.upload("generated_image.png")
    return response["public_id"]