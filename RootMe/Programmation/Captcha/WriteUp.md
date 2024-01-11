# CAPTCHA me if you can

## 20 Points

### Énoncé

Casser le CAPTCHA pour valider le challenge dans les 3 secondes.

## Solution

Le but du challenge est de réussir le captcha en moins de 2 secondes, ce qui n'est pas possible à la main. Il faut donc faire un programme pour cela. On va donc faire cela en python. [Code ici](./file.py)

1. Récupérer l'image du captcha

```Python
url = 'http://challenge01.root-me.org/programmation/ch8/'

s = requests.get(url)

ses = s.cookies

match = re.search(r';base64,(.*?)\"', s.text)

img_data = base64.b64decode(match.group(1))

f = open('image.png', 'wb')
f.write(img_data)
f.close()
```

2. Retirer les points dérangeants sur l'image. [Image avec](./image.png) | [Image sans](./filtered.png)

```Python
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
```

3. Utiliser un ORC pour pouvoir lire les charactères sur l'image. Ici, on utilisera pytesseract, qui est une librairie python qui utilise l'ORC tesseract.

```Python
result =  pytesseract.image_to_string(img)
result = unicodedata.normalize('NFKD', result).encode('ascii', 'ignore')
```
4. Faire la requête POST pour envoyer le résultat de l'ORC et valider captcha

```Python
data = {'cametu': result.decode('utf-8').rstrip()}

response = requests.post(url,cookies=ses , data=data)
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.text)
```