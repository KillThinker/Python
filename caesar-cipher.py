alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipher = []
def caesar(encode_or_decode, original_text, shift_amount):
    cipher_message = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            index_number = alphabet.index(letter) + shift_amount
            index_number %= len(alphabet)
            letter_after_shift = alphabet[index_number]
            cipher.append(letter_after_shift)
        elif letter not in alphabet:
            cipher.append(letter)
        cipher_message = "".join(cipher)
    print(f"Here is {encode_or_decode}d result: {cipher_message}")
    cipher.clear()


should_continue = True
while should_continue:
    print(logo)
    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = ""
    shift = 0
    if user_choice != "encode" and user_choice != "decode":
        print("You typed the wrong inputs. Check again!")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(encode_or_decode=user_choice, original_text=text, shift_amount=shift)
        restart = input("Do you want to restart this program (yes/no)? ").lower()
        if restart == "no":
            should_continue = False
            print("Goodbye.")
