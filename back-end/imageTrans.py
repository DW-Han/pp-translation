import cv2
import pytesseract
from googletrans import Translator
import numpy as np
import requests

api_key = 'AIzaSyA8jT11NKVpqK3HcP2ed5n30iQ3x6poffQ'
tolang = 'lt'
lang = 'en'

def translateImg():
    # Read the image
    img = cv2.imread("image.png")

    # Get the size of the image
    height, width = img.shape[:2]

    # Extract text from the image
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img)

    # Define the color to fill the text region
    color = (0, 0, 0) # black color

    # Draw a filled rectangle over the text region
    cv2.rectangle(img, (0, 0), (width, height), color, -1)

    # Translate the text
    url = f'https://translation.googleapis.com/language/translate/v2?q={text}&target={tolang}&format=text&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        translated_text = response.json()['data']['translations'][0]['translatedText']
        print(translated_text)
        text = translated_text
    else:
        print('Translation failed:', response.text)

    # Define the font and color for the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255) # white color

    # Get the size of the text
    text_width, text_height = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]

    # Calculate the position of the text
    text_x = (width - text_width) // 2
    text_y = (height + text_height) // 2

    # Add the text to the image
    cv2.putText(img, text , (text_x, text_y), font, 1, color, 2)

    '''
    # Show the image with the added text
    cv2.imshow("Image with Text", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    print(text)

    filename= 'output.jpg'
    cv2.imwrite(filename, img)
    return filename