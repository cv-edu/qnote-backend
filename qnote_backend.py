import os

import qnote_cv
import upload_image
from url_to_text import url_to_text
import write_notes

def qnote(filename):
    qnote_cv.process(filename)
    contents = upload_image.upload_multiple()

    infos = {}
    for cont in contents:
        file = f"{cont}.png"
        text = url_to_text(contents[cont])
        infos[cont] = text;

        os.remove(file)

    write_notes.write(infos)

if __name__ == '__main__':
    qnote("zacc.png")
