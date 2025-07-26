alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
"""def encrypt(text,shift):
    encrypt=""
    for i in text:
        e_index=int(alphabet.index(i))
        n_index = shift + e_index
        a=alphabet[n_index]
        encrypt+=a
    print(encrypt)
def decrypt(text,shift):
    decrypt=""
    for i in text:
        e_index=int(alphabet.index(i))
        n_index = e_index - shift
        a=alphabet[n_index]
        decrypt+=a
    print(decrypt)"""
def encrypt_or_decrypt(text,shift):
    code=""
    if direction=="decode":
        shift*=-1
    for i in text:
        e_index=int(alphabet.index(i))
        n_index = shift + e_index
        a=alphabet[n_index]
        code+=a
    print(code)
while True:
    choice=input("enter 1 to continue conversion")
    if choice not in "1":
        print("thank you!")
        break
    else:
        direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text=input("type your message:\n").lower()
        shift=int(input("Type the shift number:\n"))
        encrypt_or_decrypt(text,shift)
        
