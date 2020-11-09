from PIL import Image
from operator import itemgetter

im = Image.open("screenshot.png")
im = im.convert("P")
im2 = Image.new("P",im.size,255)

im = im.convert("P")

his = im.histogram()
# print( im.histogram())


values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
    print( j,k)

temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix == 802 or pix == 805: # these are the numbers to get_
            im2.putpixel((y,x),0)
im2.save("output.png")


def get_captcha_text(location, size):
    # pytesseract.pytesseract.tesseract_cmd = 'path/to/pytesseract'
    im = Image.open('screenshot.png')
    left = location['x']
    top = location['y']-10
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']-10
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    # response = requests.get("http://main.sci.gov.in/php/captcha.php")
    captcha_text = image_to_string(Image.open('screenshot.png'))
    return captcha_text
