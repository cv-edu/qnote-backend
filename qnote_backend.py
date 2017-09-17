import qnote_cv
import upload_image
from url_to_text import url_to_text
import categorize

def qnote(filename):
    total = qnote_cv.process(filename)
    contents = []
    for i in range(total):
        url = upload_image.upload(f"contour-{i+1}.png")
        text = url_to_text(url)
        contents.append(text)

    return contents

if __name__ == '__main__':
    contents = qnote("form.png")
    print(contents)
