import os

import qnote_cv
import upload_image
from url_to_text import url_to_text
import categorize

def qnote(filename):
    qnote_cv.process(filename)
    contents = upload_image.upload_multiple()

    infos = []
    for cont in contents:
        print(cont)
        file = f"{cont}.png"
        print(contents[cont])
        text = url_to_text(contents[cont])
        infos.append(text)

        os.remove(file)

    return infos

if __name__ == '__main__':
    contents = qnote("zacc.png")
    print(contents)
