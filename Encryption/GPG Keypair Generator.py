#pip install python-gnupg
import gnupg

# Initialize GPG
gpg = gnupg.GPG()

# Define key input data
input_data = gpg.gen_key_input(
    name_email='user@example.com',
    passphrase='your_passphrase',
    key_type='RSA',
    key_length=4096,
)

# Generate the key
key = gpg.gen_key(input_data)

if not key:
    print("Key generation failed.")
    exit(1)

# Export the public key
public_key = gpg.export_keys(str(key))

# Export the private key
private_key = gpg.export_keys(str(key), secret=True, passphrase='your_passphrase')

# Output the keys
print("Public Key:\n")
print(public_key)
print("\nPrivate Key:\n")
print(private_key)
