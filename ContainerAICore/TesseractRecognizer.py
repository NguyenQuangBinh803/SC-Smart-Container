#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Edward J. C. Ashenbert - Miyuki Nogizaka, September 2020

import pytesseract
from ContainerAICore.ImagePreprocessCore import ImagePreprocessCore

class tesseract_text_recognize(ImagePreprocessCore):

    def __init__(self):
        super().__init__()
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.config = ("-l eng --oem 3 --psm 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        self.all_text_images = []

    def recognize_image(self, images):
        global real_results
        if len(images) > 2:
            results = []
            for img in images:
                text = pytesseract.image_to_string(img, config=self.config)

                if len(text) >= 3:
                    results.append(text)

            if results != None:
                real_results = [None] * len(results)
                for res in results:

                    if not res.isdecimal() and not res.isalpha() and len(results) >= 3:
                        real_results[2] = res
                    elif res.isdecimal() and not res.isalpha() and len(results) >= 2:
                        if len(res) > 6:
                            res = res[:6]
                        real_results[1] = res
                    elif not res.isdecimal() and res.isalpha()  and len(results) >= 1:
                        real_results[0] = res
                if len(real_results) >= 2:
                    return_text = str(real_results[0]) + str(real_results[1])
                    return return_text
                else:
                    return 'Cannot recognize due to something I dont know'


