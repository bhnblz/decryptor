# Input the encrypted string
encrypted_str = input("The encrypted string is: ")

# Use def to define the function and to decrypt
def decrypt_str():
    decrypted_str = ""

# Check all the equivalent characters
    for j in encrypted_str:
    # If *, change to a
        if j == "*":
            decrypted_str += "a"
    # If &, change to e
        elif j == "&":
            decrypted_str += "e"
    # If #, change to i
        elif j == "#":
            decrypted_str += "i" 
    # If +, change to o
        elif j == "+":
            decrypted_str += "o"
    # If !, change to u
        elif j == "!":
            decrypted_str += "u"
        else:
            decrypted_str += j