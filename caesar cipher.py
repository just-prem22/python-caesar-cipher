alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar():
    option=input("Type encode to encrypt or type decode to decrypt...")
    message=input("What is the message\n").lower()
    shift=int(input("How many digits shift you want to do..."))
    def encrypt(original_text,shift_number):
        cipher=""
        for letter in original_text:
            if letter not in alphabet:
                cipher+=letter
            else:
                shifted_position=alphabet.index(letter) + shift_number
                shifted_position%=len(alphabet)
                cipher+=alphabet[shifted_position]
        print("Here is your encoded text: ",cipher)
    def decrypt(original_text,shift_amount):
        decrypted_text=""
        for letter in original_text:
            if letter not in alphabet:
                decrypted_text+=letter
            else:
                shifted_position=alphabet.index(letter) - shift_amount
                shifted_position%=len(alphabet)
                decrypted_text+=alphabet[shifted_position]
        print("Here is your decoded text: ",decrypted_text)
    if option=="encode":
        encrypt(original_text=message,shift_number=shift)
    else:
        decrypt(original_text=message,shift_amount=shift)
caesar()
again=True
while again:
    ask=input("Do you want to use it again type yes for using it again...").lower()
    if ask=="yes":
        caesar()
    else:
        again=False

    





