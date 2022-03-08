x = int(input())

dictionary = {}

for i in range(x):
    text = input().split()
    dictionary[text[0]] = text[1]

while True:
    try:
        contact = input()
        if contact in dictionary:
            print(contact+"="+dictionary[contact])
        else:
            print("Not found")
    except EOFError:
        break