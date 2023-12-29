import cairosvg
import pytesseract
from PIL import Image

# Ruta de la imagen SVG
svg_file_path = "/home/ale/Pictures/Post 1.svg"

# Ruta para guardar la imagen temporal
temp_image_path = "temp_image.png"

# Convertir SVG a imagen PNG utilizando Pycairo
cairosvg.svg2png(url=svg_file_path, write_to=temp_image_path)

# Utilizar Tesseract OCR para extraer texto de la imagen
image = Image.open(temp_image_path)
text = pytesseract.image_to_string(image)
print(text)

# Eliminar la imagen temporal
image.close()
