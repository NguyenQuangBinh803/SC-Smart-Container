#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Edward J. C. Ashenbert - Miyuki Nogizaka - Nguyen Quang Binh, May 2020

import cv2
import numpy as np


class ImagePreprocessCore:
    def __init__(self):
        print("Init the preprocess core")
        self.threshold_parameter = 150
        self.resize_parameter = 3
        self.color_thresh = [0, 170, 0]

    def sort_contours(self, cnts, method="left-to-right"):
        reverse = False
        i = 0
        if method == "right-to-left" or method == "bottom-to-top":
            reverse = True
        if method == "top-to-bottom" or method == "bottom-to-top":
            i = 1
        boundingBoxes = [cv2.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][i], reverse=reverse))
        return (cnts, boundingBoxes)

    def extract_white_text(self, frame):
        height, width, _ = frame.shape
        frame = cv2.resize(frame, (width * self.resize_parameter, height * self.resize_parameter))
        height, width, _ = frame.shape
        image = np.zeros((height, width, 3), np.uint8)
        image[:] = (255, 255, 255)
        img = frame.copy()
        res_img = image - img
        thresh1 = self.color_thresh[0]
        thresh2 = self.color_thresh[1]
        thresh3 = self.color_thresh[2]
        indices = res_img[:, :] > (thresh1, thresh2, thresh3)
        res_img[indices] = 255
        res_img[indices == False] = 0
        indices = res_img[:, :] == 255
        res_img[indices] = 0
        res_img[indices == False] = 255
        return_image = cv2.medianBlur(cv2.threshold(cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY)[1], 5)
        return return_image


    def remove_unwanted_object(self, return_image):
        height, width = return_image.shape[:2]
        cnts = cv2.findContours(return_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        mask = np.zeros((height, width), np.uint8)

        for cnt in cnts:
            x, y, w, h = cv2.boundingRect(cnt)
            if x == 0 or x + w >= width or y == 0 or y + h >= height - 10 or w * h < 100:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(return_image, [box], 0, 0, -1)
            elif w * h > 100 and w * h < 8000 and h < 200:
                roi = return_image[y:y + h, x:x + w]
                mask[y:y + h, x:x + w] = roi

        return mask

    def extract_text_group(self, mask):
        sqKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))
        return_image = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, sqKernel)
        # cv2.imwrite('mophology/' + filename, return_image)
        cnts = cv2.findContours(return_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        for cnt in cnts:
            x, y, w, h = cv2.boundingRect(cnt)
            if w * h > 3000:
                group_of_text_image = np.zeros((height, width), np.uint8)
                offset = 0
                group_of_text_image[y - offset:y + h + offset, x - offset:x + offset + w] = mask[
                                                                                            y - offset:y + h + offset,
                                                                                            x - offset:x + offset + w]
                group_of_text_image = cv2.threshold(group_of_text_image, 0, 255, cv2.THRESH_BINARY_INV)[1]
                self.all_text_images.append(group_of_text_image)
        return self.all_text_images

    def preprocess_image(self, frame):
        height, width, _ = frame.shape
        frame = cv2.resize(frame, (width * 3, height * 3))
        height, width, _ = frame.shape
        image = np.zeros((height, width, 3), np.uint8)
        image[:] = (255, 255, 255)
        img = frame.copy()
        res_img = image - img
        thresh1 = 0
        thresh2 = 170
        thresh3 = 0
        indices = res_img[:, :] > (thresh1, thresh2, thresh3)
        res_img[indices] = 255
        res_img[indices == False] = 0
        indices = res_img[:, :] == 255
        res_img[indices] = 0
        res_img[indices == False] = 255
        return_image = cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)
        return_image = cv2.threshold(return_image, 0, 255, cv2.THRESH_BINARY)[1]
        return_image = cv2.medianBlur(return_image, 5)


        cnts = cv2.findContours(return_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        mask = np.zeros((height, width), np.uint8)

        for cnt in cnts:
            x, y, w, h = cv2.boundingRect(cnt)
            if x == 0 or x + w >= width or y == 0 or y + h >= height - 10 or w * h < 100:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x
                # print(box[0][1])
                box = np.int0(box)
                cv2.drawContours(return_image, [box], 0, 0, -1)
            elif w * h > 100 and w * h < 8000 and h < 200:
                # cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1)
                roi = return_image[y:y + h, x:x + w]
                mask[y:y + h, x:x + w] = roi

        sqKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30,30))
        return_image = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, sqKernel)
        # cv2.imwrite('mophology/' + filename, return_image)
        cnts = cv2.findContours(return_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        for cnt in cnts:
            x, y, w, h = cv2.boundingRect(cnt)
            if w * h > 3000:
                group_of_text_image = np.zeros((height, width), np.uint8)
                offset = 0
                group_of_text_image[y - offset:y + h + offset, x - offset:x + offset + w] = mask[
                                                                                            y - offset:y + h + offset,
                                                                                            x - offset:x + offset + w]
                group_of_text_image = cv2.threshold(group_of_text_image, 0, 255, cv2.THRESH_BINARY_INV)[1]
                self.all_text_images.append(group_of_text_image)
        return self.all_text_images

if __name__ == "__main__":
    all_text_images = []
    preprocess_core = ImagePreprocessCore()
    image = cv2.imread("cropped_container/1582668749815.jpg")

    return_image = preprocess_core.extract_white_text(image)
    return_image = preprocess_core.remove_unwanted_object(return_image)
    cv2.imshow("res_img", return_image)
    cv2.waitKey(0)

    sqKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30,30))
    return_image = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, sqKernel)
    cv2.imshow("return_image", return_image)
    cnts = cv2.findContours(return_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        if w * h > 3000:
            group_of_text_image = np.zeros((height, width), np.uint8)
            offset = 0
            group_of_text_image[y - offset:y + h + offset, x - offset:x + offset + w] = mask[
                                                                                        y - offset:y + h + offset,
                                                                                        x - offset:x + offset + w]
            group_of_text_image = cv2.threshold(group_of_text_image, 0, 255, cv2.THRESH_BINARY_INV)[1]
            all_text_images.append(group_of_text_image)

    for image in all_text_images:
        cv2.imshow(str(image), image)
        cv2.waitKey(0)