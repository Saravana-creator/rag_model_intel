import fitz
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_path):
    text=""
    doc=fitz.open(pdf_path)
    for page in doc:
        text+=page.get_text("text")
        if not text.strip():
            pix=page.get_pixmap()
            img=Image.open(io.BytesIO(pix.tobytes("png")))
            text+=pytesseract.image_to_string(img,lang='eng+hin+urd')
    return text