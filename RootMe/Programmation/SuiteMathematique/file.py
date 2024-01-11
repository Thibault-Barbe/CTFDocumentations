import requests
import re

get = requests.get('http://challenge01.root-me.org/programmation/ch1/')
print(get.text + "\n")
cookies = get.cookies
html_content = get.text

first = re.search(r" (-?\d+) \+ U<sub>n</sub> \] (.*?) \[ n \* (-?\d+) ", html_content)
second = re.search(r"U<sub>0</sub> = (-?\d+)\n", html_content)
third = re.search(r'You must find U<sub>(\d+)</sub>', html_content)

if first:
    addNumber = int(first.group(1))
    operation = 1 if first.group(2) == "+" else -1
    multiplyNumber = int(first.group(3))
    print("Addition Number:", addNumber)
    print("opeation: ", operation)
    print("Multiplication Number:", multiplyNumber)

if second:
    result = int(second.group(1))
    print("U<sub>0</sub>:", result)

if third:
    target_n = int(third.group(1))
    print("Target n:", target_n)

i = 1
while( i <= target_n):
    result = (addNumber + result) + (((i-1) * multiplyNumber) * operation)
    i = i + 1


print(f"U<sub>{i}</sub> = {result}")
print(result)

res = get = requests.get('http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='+str(result), cookies=cookies)
print(res.text)