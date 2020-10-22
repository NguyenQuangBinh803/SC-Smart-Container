#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Edward J. C. Ashenbert - Miyuki Nogizaka - Nguyen Quang Binh, September 2020

import cv2
import numpy as np
from ocr_worker.utils.recognize import ocr

class EasyOCRRecognizer:
    def __init__(self):
        self.reader = ocr.Reader()

    def recognize_image(self, image):
        global real_results
        results = self.reader.readtext(image)
        return results
