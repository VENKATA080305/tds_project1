import pytesseract
from PIL import Image
from .file_handler import write_file

def process_credit_card_extraction():
    """Extracts credit card number from an image using OCR (LLM Mock)"""
    try:
        image_path = "/data/card_image.png"
        card_number = pytesseract.image_to_string(Image.open(image_path), config="--psm 8").strip()
        
        if not card_number or not card_number.replace(" ", "").isdigit():
            return {"error": "Failed to extract credit card"}, 500

        write_file("/data/credit_card.txt", card_number)
        return {"status": "Credit card extracted"}, 200
    except Exception as e:
        return {"error": f"Failed to extract credit card: {str(e)}"}, 500
