string = input('input string: ')

for x in string:
    if(x % 2 != 0):
        string.insert(x, ' ')
    print(string)

