import socket
import re
import requests
from bs4 import BeautifulSoup
import time

hote = 'ctf09.root-me.org'

port = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
sock.connect((hote, port))
print(f"Connecté à {hote}:{port}")


def get_page_info(soup, question):
    if 'title' in question:
        title_tag = soup.find('title')

        if title_tag:
            page_title = title_tag.get_text(strip=True)
            return "{\"solution\": \""+page_title+"\"}"
        else:
            print("no title tag")
            return
    elif 'description' in question:
        description_tag = soup.find('meta', {'name': 'description'})
        if description_tag:
            description = description_tag['content']
            return "{\"solution\": \""+description+"\"}"
        else:
            print("no title tag")
            return

def get_child_info(soup, question):
    if 'tag' in question:
        match = re.search(r"child's tag of (.*?) with (.*?)\?", question)
        of = match.group(1)
        condition = match.group(2).split("=")

        element = soup.find(of, {condition[0]: condition[1]})

        if element:
            id = -1 if 'last' in question else 0
            child = element.find_all(recursive=True)[id]  # Find the last child
            child_tag = child.name if child else None
            return "{\"solution\": \""+child_tag+"\"}"
        else:
            print("no element")

    elif 'value' in question:
        match = re.search(r"child's (.*?) value of (.*?) with (.*?)\?", question)

        value = match.group(1)
        of = match.group(2)
        condition = match.group(3).split("=")

        element = soup.find(of, {condition[0]: condition[1]})

        if element:
            id = -1 if 'last' in question else 0
            child = element.find_all(recursive=True)[id]  # Find the last child
            child_value = child.get(value) if child else None
            if isinstance(child_value, str):
                return "{\"solution\": \""+child_value+"\"}"
            return "{\"solution\": \""+child_value[-1]+"\"}"
        else:
            print("no element")

def get_parent_info(soup, question):
    if 'tag' in question:
        match = re.search(r"parent's tag of (.*?) with (.*?)\?", question)
        of = match.group(1)
        condition = match.group(2).split("=")

        element = soup.find(of, {condition[0]: condition[1]})

        if element:
            parent_tag = element.parent.name if element and element.parent else None
            return "{\"solution\": \""+parent_tag+"\"}"
        else:
            print("no element")

    elif 'value' in question:
        match = re.search(r"parent's (.*?) value of (.*?) with (.*?)\?", question)

        value = match.group(1)
        of = match.group(2)
        condition = match.group(3).split("=")

        element = soup.find(of, {condition[0]: condition[1]})

        if element:
            parent_value = element.parent.get(value) if element and element.parent else None
            if isinstance(parent_value, str):
                return "{\"solution\": \""+parent_value+"\"}"
            return "{\"solution\": \""+parent_value[-1]+"\"}"
        else:
            print("no element")

def get_element_value(soup, question):
    match = re.search(r"of the element (.*?) with (.*?)\?", question)
    of = match.group(1)
    condition = match.group(2).split("=")

    # print(soup.prettify())

    if 'innerText' in question:

        element = soup.find(of, {condition[0]: condition[1]})

        if element:
            inner_text_value = element.get_text(strip=False).replace('"', '\\"').replace('\n', '').replace("\t", ' ')
            return "{\"solution\": \""+inner_text_value+"\"}"
        else:
            print("no element")
    elif 'innerHTML' in question:

        element = soup.find(of, {condition[0]: condition[1]})

        if element:
            print("element: ", element)
            html_value = ''.join(map(str, element.contents)).replace('"', '\\"').replace("\t", ' ').replace('\n', '', 1)
            return "{\"solution\": \""+html_value+"\"}"
        else:
            print("no element")
    elif 'outerHTML' in question:

        element = soup.find(of, {condition[0]: condition[1]})

        if element:
            print("element: ", element, "\n\n")
            for child in element.find_all(recursive=False):
                if len(element.find_all(recursive=False)) > 1:
                    child.decompose()
            html_value = str(element).replace('"', '\\"').replace('\n', '')
            return "{\"solution\": \""+html_value+"\"}"
        else:
            print("no element")

def get_random_value(soup, question):
    match = re.search(r"the (.*?)'s (.*?) value with (.*?)\?", question)

    of = match.group(1)
    typeof_value = match.group(2)
    condition = match.group(3).split("=")

    element = soup.find(of, {condition[0]: condition[1]})

    if element:
        value = element.get(typeof_value)
        if (isinstance(value, str)):
            return "{\"solution\": \""+value+"\"}"
        return "{\"solution\": \""+value[-1]+"\"}"
    else:
        print("no element")


def find_answer(content, question):

    soup = BeautifulSoup(content, 'html.parser')

    if "page" in question:
        return get_page_info(soup, question)
    elif 'child' in question:
        return get_child_info(soup, question)
    elif 'parent' in question:
        return get_parent_info(soup, question)
    elif 'of the element' in question:
        return get_element_value(soup, question)
    else:
        return get_random_value(soup, question)
    
            

while True:

    donnees = sock.recv(1028).decode('utf-8')
    print("Données reçues:", donnees)

    if not donnees:
        break

    # Afficher les données reçues

    # Utiliser une expression régulière pour extraire les chiffres de la chaîne
    match = re.search(r'{"url": "http://ctfXX.root-me.org:8000/(.*?)", "cookie": {"random": (.*?)}, "question": "(.*?)"}', donnees)
        
    if match and 'Question:' not in donnees:
        page = match.group(1)
        cookie = match.group(2)
        question = match.group(3)
        url = "http://"+hote+":8000/"+page

        content = requests.get(url=url, cookies={"random": cookie})
        if content.status_code == 200:
            res = find_answer(content.text, question)+"\n"
            print("res: ", res)
            answer = sock.sendall(res.encode('utf-8'))
        else:
            print("Content ERROR: ", content.status_code)