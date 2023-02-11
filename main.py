from processer import Process
from ocr import Classifier
import sys
import cv2

def main():
    # Step 0: Set image height and width max and choose image
    S_HEIGHT = 450
    S_WIDTH = 450
    S_IMAGE_PATH = "resources/sudoku.jpg"

    # Step 1: Cleanup image
    img_clean = Process.clean(S_IMAGE_PATH)
    cv2.imshow("test",img_clean)
    cv2.waitKey(0)
    print(img_clean)
    return 0

if __name__ == "__main__":
    main()
else:
    print("Run as main, exiting")
    exit(1)