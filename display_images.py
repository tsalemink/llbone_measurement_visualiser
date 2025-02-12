import os
import numpy as np
from PIL import Image, ImageFont, ImageDraw


# function to add text underneath images
def text_img(txt, IMG_SIZE_W):
    image = Image.new("RGBA", (IMG_SIZE_W, IMG_SIZE_W//2), "white")
    font = ImageFont.truetype("segoeui.ttf", 20)
    draw = ImageDraw.Draw(image)
    position = (0, 20)

    bbox = draw.textbbox(position, text=txt, font=font, align="center")
    draw.rectangle(bbox, fill="white")
    draw.text(position, txt, font=font, fill="black", align="center")
    return image


if __name__ == "__main__":
    IMG_SIZE_W = 200
    IMG_SIZE_H = 200

    # path
    path = '.\\test_images\\'

    img_data = []
    txt_data = []

    for img in os.listdir(path):
        img_data.append(np.array(Image.open(path + img).resize((IMG_SIZE_W, IMG_SIZE_H))))
        txt_data.append(np.array(text_img("Measurements", IMG_SIZE_W)))

    # convert to numpy array
    for i, img in enumerate(img_data):
        if i == 0:
            np_img_data = np.vstack((img, txt_data[i]))
        else:
            img = np.vstack((img, txt_data[i]))
            np_img_data = np.hstack((np_img_data, img))

    # display image
    img = Image.fromarray(np_img_data)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 12)
    img.show()
