# encrypt using ASCII offset
def encrypt(text, offset):
    # if offset is greater than 26, use modulo to get remainder
    if offset > 26:
        offset = offset % 26

    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + offset)

    print(encrypted)

txt = input("Enter text to encrypt: ")
offset = int(input("Enter offset: "))

encrypt(txt, offset)