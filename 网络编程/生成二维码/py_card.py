import qrcode

img = qrcode.make('http://www.baidu.com')
# img <qrcode.image.pil.PilImage object at 0x00000183533D5CF8>
with open('./image/baidu.png', 'wb') as f:
    img.save(f)
