running = True

def text_to_decimal(message):
    for i in range (len(message)):
        return(decimal_to_binary(ord(message[i])), end = "")

def decimal_to_binary(message):
    n = int(message)  # decimal number
    res = ''  # binary result

    for i in range (8):
        res = str(n % 2) + res
        n //= 2
    return(res)

def encryption(message):
    return (message)

while running:
    message = input(">> ")
    print(text_to_decimal(message))
