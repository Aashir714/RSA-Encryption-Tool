from sympy import randprime
import random

# Define the GCD function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Step 1: Generate random primes for p and q
p = randprime(128, 256)  # Generates a random 8-bit prime
q = randprime(128, 256)
while p == q:  # Ensure p and q are different
    q = randprime(128, 256)

print(f"Generated primes p: {p}, q: {q}")

# Step 2: Calculate n and phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Step 3: Choose e, ensuring it’s coprime with phi_n
e_values = [3, 5, 65537]
e = next((val for val in e_values if gcd(val, phi_n) == 1), None)
if e is None:
    raise ValueError("Failed to find a valid e that is coprime with phi_n.")
print("Chosen public exponent e:", e)

# Step 4: Calculate the private key d
d = pow(e, -1, phi_n)
print("Calculated private key d:", d)

# Step 5: Define encryption and decryption functions
def encrypt_char(char, e, n):
    ascii_value = ord(char)
    return pow(ascii_value, e, n)

def decrypt_char(cipher_char, d, n):
    return chr(pow(cipher_char, d, n))  # Convert back to character after decryption

# Step 6: Prompt user for a message
message = input("Enter the message you want to encrypt: ")

# Step 7: Encrypt each character in the user’s message
encrypted_message = [encrypt_char(char, e, n) for char in message]
print("Encrypted message:", encrypted_message)

# Step 8: Decrypt the message
decrypted_message = ''.join(decrypt_char(c, d, n) for c in encrypted_message)
print("Decrypted message:", decrypted_message)

# Step 9: Save the keys and encrypted message to files
with open("public_key.txt", "w") as f:
    f.write(f"Public Key (e, n): ({e}, {n})\n")

with open("private_key.txt", "w") as f:
    f.write(f"Private Key (d, n): ({d}, {n})\n")

with open("encrypted_message.txt", "w") as f:
    f.write(" ".join(map(str, encrypted_message)))

print("Keys and encrypted message have been saved to files.")
