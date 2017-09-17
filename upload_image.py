import pyimgur
from os import environ

client_id = environ.get("PYTHON_IMGUR_ID")
im = pyimgur.Imgur(client_id)

def upload(filepath):
    image = im.upload_image(filepath)
    return image.link

if __name__ == '__main__':
    print(upload("form.png"))
