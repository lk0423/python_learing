from PIL import Image

img_list = ['1.jpg', '2.png']
path = 'F:/360downloads/wpcache/'
for imgs in img_list:
    img = Image.open(path + imgs)
    if imgs == '1.jpg':
        pic = img.resize((400, 200))
        pic.save(path + imgs)
    if imgs == '2.png':
        pic = img.resize((400, 100))
        pic.save(path + imgs)
