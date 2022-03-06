x = int(input())

for item in range(x):
    userstr = input()
    result = ''
    for index in range(len(userstr)):
        if index % 2 == 0:
            result += userstr[index]

    result += ' '

    for index in range(len(userstr)):
        if index % 2 != 0 :
            result += userstr[index]

    print(result)
        