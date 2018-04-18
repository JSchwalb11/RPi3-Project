import binascii

#this function converts text into a binary string
def toBin(a):
    new = ""
    for ch in a:
        new += bin(ord(ch))[2:].zfill(8)
    return new

#this function turns string binary into text
def toText(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

#this function helps turn string binary into text
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

#this function will turn smaller blocks of bits into 32 bits (binary) by zero filling
def to32Bit(x):
    if(len(x) != 32):
        for i in range(0, 32 - len(x)):
            x += "0"
        return x
    return x

#this function will turn smaller blocks of bits into 64 bits (binary) by zero filling
def to64Bit(x):
    if(len(x) != 64):
        for i in range(0, 64 - len(x)):
            x += "0"
        return x
    return x

'''
requires two 32 bit blocks of string binary, takes the first
argument and does a XOR bitwise operation with the second argument
'''
def xOR(x, y):
    new = ""
    for i in range(0, 32):
        if(x[i] == "0" and y[i] == "0"):
            new += "0"
        if(x[i] == "0" and y[i] == "1"):
            new += "1"
        if(x[i] == "1" and y[i] == "0"):
            new += "1"
        if(x[i] == "1" and y[i] == "1"):
            new += "0"
    return new

'''
requires a string message and key, splits the key into two equal parts, the first half is
used for for XOR operations and the second half is used for doubling the amount of bytes
of the message. The encryption works by spliting the message into 32bit chuncks, and
doubling the amount of chuncks there are, XORing the first half of chuncks and then swapping
the first and second half, resulting in a message that is longer and encytped.
'''
def encrypt(msg, key):
    msg = toBin(msg)
    key = toBin(key)

    keyList = []
    addList = []

    temp = ""
    for i in range(0, len(key), 32):
        if(i < len(key)/2):
            temp = key[i:i+32]
            keyList.append(temp)
        if(i >= len(key)/2):
            temp = key[i:i+32]
            addList.append(temp)

    blockList = []
    for j in range(0, len(keyList)):
        for i in range(0, len(msg), 32):
            temp = ""
            temp += msg[i:i+32]
            if(len(temp) != 32):
                temp = to32Bit(temp)
            blockList.append(temp)
            blockList.append(addList[j])
        
        for i in range(0, len(blockList), 2):
            blockList[i] = xOR(blockList[i], keyList[j])
            temp =  blockList[i]
            blockList[i] =  blockList[i+1]
            blockList[i+1] = temp
    
    result = ""
    for i in range(0, len(blockList)):
        result += blockList[i]

    result = toText(result)
    return result

'''
requires a string message and key, splits the key into two equal parts, the first half is
used for for XOR operations and the second half is used for doubling the amount of bytes
of the message. The decyrption works by XORing the first half and swaping the first and the
second half, do this with the same key and the same number of rounds of encryption and you
will have your origional message. You will have to cut off some characters from the end but
the origional message will show up first and in full.
'''
def decrypt(msg, key):
    msg = toBin(msg)
    key = toBin(key)

    keyList = []

    temp = ""
    for i in range(0, len(key), 32):
        if(i < len(key)/2):
            temp = key[i:i+32]
            keyList.append(temp)

    blockList = []
    for i in range(0, len(msg), 32):
        temp = ""
        temp += msg[i:i+32]
        blockList.append(temp)

    for j in range(0, len(keyList)):
        for i in range(0, len(blockList), 2):
            blockList[i+1] = xOR(blockList[i+1], keyList[j])
            temp =  blockList[i+1]
            blockList[i+1] =  blockList[i]
            blockList[i] = temp
    
    result = ""
    for i in range(0, len(blockList)):
        if(i%2 == 0):
            result += blockList[i]

    print(len(keyList)*8)
    result = toText(result)
    tot = len(result)/len(keyList)
    result = result[0:tot]

    return result

def main():
    msg = "Hello World"
    key = "this_is_my_awesome_key_it_should_be_long"
    print(msg)

    result = encrypt(msg, key)
    
    print('Encrypted(with ascii symbols):', repr(result))

    print('Encrypted(as raw string): ' + result)

    result = decrypt(result, key)
    
    print('Decrypted(with ascii symbols):', repr(result))

    print('Decrypted(as raw string): ' + result)
    
main()
#bigger the key, more rounds of encryption -- use first half of key
#keyList = ["01011110011111100111111001111110","01110001011111010111110101111101","01111011011110000111101101111011","01100000011110100111101001111010"]
#make longer -- use second half of key
#addList = ["01111110011111100111111001111110","01111101011111010111110101111101","01111011011110110111101101111011","01111010011110100111101001111010"]

