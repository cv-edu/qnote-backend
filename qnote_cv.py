import cv2
import matplotlib.pyplot as plt

contoured = []
approx_contours = []

def read(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    global contoured
    contoured = gray.copy()
    cv2.drawContours(contoured, contours, -1, color=(0, 255, 0), thickness=10)

    largest = max(contours, key=cv2.contourArea)

    global approx_contours
    approx_contours = []
    for c in filter(lambda cnt: cnt is not largest, contours):
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
        if len(approx) is 4:
            approx_contours.append(approx)

    min_area = 5e4
    approx_contours = [c for c in approx_contours if cv2.contourArea(c) > min_area]

    contoured = gray.copy()
    cv2.drawContours(contoured, approx_contours, -1, color=(127, 0, 127), thickness=7)

def save():
    for i, cnt in enumerate(approx_contours):
        x, y, w, h = cv2.boundingRect(cnt)

        img = contoured[y:y+h, x:x+w]
        plt.imsave(f"contour-{i+1}.png", img);

if __name__ == '__main__':
    read("form.png")
    save()
