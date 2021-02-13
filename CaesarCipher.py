def encrypt(message, s):
    result = ''
    s = s % 100
    for i in range(len(message)):
        current = message[i]
        num = ord(current) + s + 500
        print(num)
        result += chr(num)
    print(result)
    return result

def decrypt(message, s):
    result = ''
    s = s % 100
    for i in range(len(message)):
        current = message[i]
        result += chr(ord(current) - s - 500)
    print(result)
    return result

