alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(encode_or_decode, original_text, shift_amount):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alpabet:
            cipher_text += letter
        else:
            
            shifted_position = alpabet.index(letter) + shift_amount
            shifted_position %= len(alpabet)
            cipher_text += alpabet[shifted_position]
        
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")

while(True):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        break
