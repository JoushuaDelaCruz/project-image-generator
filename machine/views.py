from django.shortcuts import HttpResponse
from django.views import View
from machine.helper.image_generator import ImageGenerator
from machine.helper.image_uploader import upload_image

class MachineView(View):
    async def get(self, request, text):
        generator = ImageGenerator()
        await generator.generate_image(text)
        public_id = await upload_image()
        return HttpResponse(public_id)