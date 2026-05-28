import sys

from PIL import Image

images = []

for agg in sys.argv:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images
)