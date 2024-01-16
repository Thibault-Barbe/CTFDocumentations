import requests
import re
from PIL import Image, ImageFilter
import base64
import unicodedata ,pytesseract

url = 'http://challenge01.root-me.org/programmation/ch8/'

s = requests.get(url)

ses = s.cookies

match = re.search(r';base64,(.*?)\"', s.text)

img_data = base64.b64decode(match.group(1))

f = open('image.png', 'wb')
f.write(img_data)
f.close()

img = Image.open("image.png")

img = img.convert("RGBA")
pixdata = img.load()

#Clean the background noise, if color != white, then set to black.

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y] == (0, 0, 0, 255):
            pixdata[x, y] = (255, 255, 255, 255)


width, height = img.size
new_size = width*8, height*8
img = img.resize(new_size, Image.LANCZOS)
img = img.convert('L')
img = img.point(lambda x: 0 if x < 155 else 255, '1')
img.save('filtered.png')

result =  pytesseract.image_to_string(img)
result = unicodedata.normalize('NFKD', result).encode('ascii', 'ignore')

# result = subprocess.run(['gocr', 'image.png', '-C a-z A-Z 0-9'], stdout=subprocess.PIPE, text=True)

print(result.decode('utf-8').rstrip())

data = {'cametu': result.decode('utf-8').rstrip()}

response = requests.post(url,cookies=ses , data=data)
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.text)

# POST http://challenge01.root-me.org/programmation/ch8/ body: {cametu: 'azbdslope3fE'}