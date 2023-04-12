from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1 
  for char in start_text:
    if char in alphabet: 
      position = alphabet.index(char)
      new_position = position + shift_amount
      new_char = alphabet[new_position]
      end_text += new_char
    else: 
      end_text += char 
  print(f"The {cipher_direction}d text is {end_text}")

end_of_program = False 
while not end_of_program: 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  answer = input("Do you want to restart the program? Type 'yes' or 'no'.\n")
  if answer == "no": 
    end_of_program = True
    print("Thank you for using the Caesar Cipher program.")
