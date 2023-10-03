alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or quit:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
    secret_message = ""
    for a in text:
        message_index = alphabet.index(a)
        enc_message = int(message_index) + int(shift)
        alphabet_enc = alphabet[enc_message]
        secret_message += alphabet_enc
    print(''.join(secret_message))


def decrypt(text2,shift):
    de_crypt = ""
    for i in text:
        message_index = alphabet.index(i)
        enc_message = int(message_index) - int(shift)
        alphabet_enc = alphabet[enc_message]
        de_crypt += alphabet_enc
    print(de_crypt)


if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)

