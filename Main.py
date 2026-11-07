running = True

def text_to_decimal(message):
    a = ""

    for i in range (len(message)):  
        a = a + str(decimal_to_binary(ord(message[i]))) 

    return a

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
    print(encryption(text_to_decimal(message)))
