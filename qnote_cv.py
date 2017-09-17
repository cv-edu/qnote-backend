import cv2
import matplotlib.pyplot as plt

contoured = []
approx_contours = []

def read(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
    _, contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    global contoured
    contoured = gray.copy()
    cv2.drawContours(contoured, contours, -1, color=(0, 255, 0), thickness=10)

    global approx_contours
    approx_contours = []
    for i, cnt in enumerate(contours):
        if heirarchy[0][i][3] == 0:
            approx_contours.append(cnt)
    contours = approx_contours

    approx_contours = []
    for c in contours:
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
        if len(approx) is 4:
            approx_contours.append(approx)

    min_area = 5e4
    approx_contours = [c for c in approx_contours if cv2.contourArea(c) > min_area]

    contoured = gray.copy()
    cv2.drawContours(contoured, approx_contours, -1, color=(127, 0, 127), thickness=7)

def save():
    i = 0
    for cnt in approx_contours:
        x, y, w, h = cv2.boundingRect(cnt)

        img = contoured[y:y+h, x:x+w]
        plt.imsave(f"contour-{i+1}.png", img);

        i += 1

    return i

def process(filename):
    read(filename)
    return save()

if __name__ == '__main__':
    i = process("form.png")
    print(f"form.png: {i} images created")
