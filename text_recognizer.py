from abs_text_recognizer import ABSTextRecognizer
import pytesseract
import torch



class TextRecognizerRus(ABSTextRecognizer):
    def __init__(self):
        pass

    def recognize(self, path):
        if isinstance(path, str):
            return pytesseract.image_to_string(path, lang='rus')
