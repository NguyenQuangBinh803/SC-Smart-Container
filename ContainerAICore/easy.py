import easyocr
import glob
if __name__ == "__main__":
    reader = easyocr.Reader(['en']) # need to run only once to load model into memory
    images = glob.glob("cropped_container")
    for image in images:
        result = reader.readtext(image)
        print(result)