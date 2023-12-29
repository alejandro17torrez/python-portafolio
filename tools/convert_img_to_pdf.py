import logging

from PIL import Image

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def is_extension_there(path: str) -> bool:
    extensions = (".pdf", ".png", ".jpg", ".svg")
    for extension in extensions:
        if path.find(extension):
            return True
        break
    return False


image_path = input("enter the image path: ")
pdf_path = input("enter the image path: ")


if is_extension_there(image_path) and is_extension_there(pdf_path):
    image = Image.open(image_path).convert("RGB").save(pdf_path)
    log.debug(image)
else:
    raise ValueError("format not correct")
