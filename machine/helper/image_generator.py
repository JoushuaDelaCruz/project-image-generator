from dotenv import load_dotenv
import os
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline 

class ImageGenerator:
    """
    Uses StableDiffusion from Hugging Face to generate images from a given text.
    """
    load_dotenv()
    model = "CompVis/stable-diffusion-v1-4"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    token = os.getenv("TOKEN")

    def __init__(self):
        """
        Initializes the pipeline.
        """
        self.pipeline = StableDiffusionPipeline.from_pretrained(self.model, variant="fp16", torch_dtype=torch.float16, use_auth_token=self.token)
        self.pipeline.to(self.device)


    async def generate_image(self, text):
        """
        Generates an image from a given text.
        """
        with autocast(self.device):
            image = self.pipeline(text, guidance_scale=8.5).images[0]
        image.save("generated_image.png")