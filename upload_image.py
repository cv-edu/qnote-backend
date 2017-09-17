import pyimgur
from os import environ

client_id = environ.get("PYTHON_IMGUR_ID")
im = pyimgur.Imgur(client_id)

def upload(filepath):
    image = im.upload_image(filepath)
    return image.link

def upload_multiple():
    names = ["body", "class", "date", "name"]
    uploaded = {}
    for key in names:
        uploaded[key] = upload(f"{key}.png")

    return uploaded

if __name__ == '__main__':
    print(upload_multiple())
