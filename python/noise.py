from PIL import Image

img = Image.new('RGB', (60, 30), color = 'red')
img.save('../temp/pil_red.png')