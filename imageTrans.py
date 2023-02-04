import cv2
import pytesseract
from googletrans import Translator

# Read the image
img = cv2.imread("image.jpg")

# Extract text from the image
text = pytesseract.image_to_string(img)

# Translate the text
translator = Translator(service_urls=['translate.google.com'])
target_language = "fr"
translated_text = translator.translate(text, dest=target_language).text

print(translated_text)