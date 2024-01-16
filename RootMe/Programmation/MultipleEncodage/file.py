import socket
import re
import base64
import codecs

hote = "challenge01.root-me.org"
port = 52017

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((hote, port))
print(f"Connecté à {hote}:{port}")

def decode_morse(morse_string):
    morse_code_dict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
                   '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
                   '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
                   '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                   '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
                   '--..': 'z', '.----': '1', '..---': '2', '...--': '3',
                   '....-': '4', '.....': '5', '-....': '6', '--...': '7',
                   '---..': '8', '----.': '9', '-----': '0', '--..--': ', ',
                   '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
                   '-.--.': '(', '-.--.-': ')'}

    decoded_string = ""

    for letter in morse_string.split("/"):
        decoded_string = decoded_string + morse_code_dict[letter]
    
    return decoded_string


def decode_string(encoded_string):

    try:
        decoded_base85 = base64.b85decode(encoded_string).decode('utf-8')
        print(f"Base85 Decoding: {decoded_base85}")
        return decoded_base85
    except Exception as e:
        pass

    try:
        decoded_base64 = base64.b64decode(encoded_string).decode('utf-8')
        print(f"Base64 Decoding: {decoded_base64}")
        return decoded_base64
    except Exception as e:
        pass

    try:
        decoded_base32 = base64.b32decode(encoded_string).decode('utf-8')
        print(f"Base32 Decoding: {decoded_base32}")
        return decoded_base32
    except Exception as e:
        pass

    try:
        decoded_hex = codecs.decode(encoded_string, 'hex').decode('utf-8')
        print(f"Hex Decoding: {decoded_hex}")
        return decoded_hex
    except Exception as e:
        pass

    try:
        decoded_morse = decode_morse(encoded_string)
        print(f"Decoded Morse: {decoded_morse}")
        return decoded_morse
    except Exception as e:
        pass
    return

while True:

    donnees = sock.recv(1024).decode('utf-8')

    if not donnees:
        break

    print("Données reçues: ", donnees)


    t = re.search(r" please: '(.*?)'", donnees)

    if t:
        encoded_string = t.group(1)

        res = decode_string(encoded_string)+"\n"

        print("decode result: ", res)

        sock.sendall(res.encode('utf-8'))
    else:
        print("no t")

sock.close()