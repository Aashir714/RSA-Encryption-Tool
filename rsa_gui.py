import tkinter as tk
from sympy import randprime
import random

# RSA key generation and encryption/decryption functions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    global p, q, n, phi_n, e, d
    p = randprime(128, 256)
    q = randprime(128, 256)
    while p == q:
        q = randprime(128, 256)

    n = p * q
    phi_n = (p - 1) * (q - 1)
    e_values = [3, 5, 65537]
    e = next((val for val in e_values if gcd(val, phi_n) == 1), None)
    d = pow(e, -1, phi_n)
    public_key_label.config(text=f"Public Key: (e={e}, n={n})")
    private_key_label.config(text=f"Private Key: (d={d}, n={n})")

def encrypt_message():
    global encrypted_message
    message = message_entry.get()
    encrypted_message = [pow(ord(char), e, n) for char in message]
    encrypted_label.config(text=f"Encrypted Message: {encrypted_message}")

def decrypt_message():
    decrypted_message = ''.join(chr(pow(char, d, n)) for char in encrypted_message)
    decrypted_label.config(text=f"Decrypted Message: {decrypted_message}")

# Set up the main window
root = tk.Tk()
root.title("RSA Encryption Tool")

# Key generation section
key_frame = tk.Frame(root)
key_frame.pack(pady=10)
tk.Label(key_frame, text="Generate RSA Keys").pack()
generate_button = tk.Button(key_frame, text="Generate Keys", command=generate_keys)
generate_button.pack()
public_key_label = tk.Label(key_frame, text="Public Key: ")
public_key_label.pack()
private_key_label = tk.Label(key_frame, text="Private Key: ")
private_key_label.pack()

# Message encryption section
message_frame = tk.Frame(root)
message_frame.pack(pady=10)
tk.Label(message_frame, text="Enter Message to Encrypt:").pack()
message_entry = tk.Entry(message_frame, width=50)
message_entry.pack()
encrypt_button = tk.Button(message_frame, text="Encrypt Message", command=encrypt_message)
encrypt_button.pack()
encrypted_label = tk.Label(message_frame, text="Encrypted Message: ")
encrypted_label.pack()

# Message decryption section
decrypt_button = tk.Button(root, text="Decrypt Message", command=decrypt_message)
decrypt_button.pack(pady=10)
decrypted_label = tk.Label(root, text="Decrypted Message: ")
decrypted_label.pack()

# Start the Tkinter event loop
root.mainloop()
