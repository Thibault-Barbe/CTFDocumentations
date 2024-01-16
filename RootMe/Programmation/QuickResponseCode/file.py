import requests
import re
import base64
import cv2


url = 'http://challenge01.root-me.org/programmation/ch7/'

s = requests.get(url)

session = s.cookies
match = re.search(r';base64,(.*?)\"', s.text)
img_data = base64.b64decode(match.group(1))

f = open('image.png', 'wb')
f.write(img_data)
f.close()

image_path = './image.png'

def top_left(image):

    big_square = (20, 20)
    small_square = (35, 35)

    big_square_size = 58
    small_square_size = 30

    color = (0, 0, 0)

    cv2.rectangle(image, big_square, (big_square[0] + big_square_size, big_square[1] + big_square_size), color, 8)
    cv2.rectangle(image, small_square, (small_square[0] + small_square_size, small_square[1] + small_square_size), color, -1)

def top_right(image):

    big_square = (image.shape[1] - 22, 20)
    small_square = (image.shape[1] - 35, 35)

    big_square_size = 58
    small_square_size = 30

    color = (0, 0, 0)

    cv2.rectangle(image, (big_square[0] - big_square_size, big_square[1]), (big_square[0], big_square[1] + big_square_size), color, 8)

    cv2.rectangle(image, (small_square[0] - small_square_size, small_square[1]), (small_square[0], small_square[1] + small_square_size), color, -1)

def bottom_left(image):

    big_square = (20, image.shape[0] - 20)
    small_square = (35, image.shape[0] - 34)

    big_square_size = 58
    small_square_size = 30

    color = (0, 0, 0)

    cv2.rectangle(image, big_square, (big_square[0] + big_square_size, big_square[1] - big_square_size), color, 8)

    cv2.rectangle(image, small_square, (small_square[0] + small_square_size, small_square[1] - small_square_size), color, -1)

def correct_qr_code(image_path, output_path):
    image = cv2.imread(image_path)

    top_right(image)
    top_left(image)
    bottom_left(image)

    cv2.imwrite(output_path, image)

def decode_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Initialize the QRCode detector
    qr_code_detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    value, pts, qr_code_data = qr_code_detector.detectAndDecode(image)

    # Check if a QR code was detected
    if value:
        print(f'Data: {qr_code_data}')
        print(f'Points: {pts}')
        print(f'value: {value}')
        return value
    else:
        print('No QR code detected.')

correct_qr_code(image_path, 'new.png')

# cv2.imwrite('new.png', good_qr_code)

res = decode_qr_code('./new.png')

data = {'metu': res.split(" ")[3] }

response = requests.post(url,cookies=session , data=data)
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.text)
