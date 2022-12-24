import hashlib
import getpass
import os
import base64

def create_seed_phrase():
  # Generate a random 24-word seed phrase
  seed_phrase = ""
  words = ["word1", "word2", "word3", ..., "word24"]
  for i in range(24):
    seed_phrase += words[random.randint(0, len(words)-1)] + " "
  return seed_phrase.strip()

def create_password_vault():
  # Prompt the user to create a seed phrase
  print("Welcome to the password vault!")
  print("To create a new password vault, you will need to set up a 24-word seed phrase.")
  print("Please write down the following seed phrase and store it in a secure location:")
  seed_phrase = create_seed_phrase()
  print(seed_phrase)
  # Hash the seed phrase to use as the password for the password vault
  password = hashlib.sha256(seed_phrase.encode()).hexdigest()
  # Create a new password vault file
  with open("password_vault.txt", "w") as f:
    f.write(password)

def login_to_password_vault():
  # Prompt the user to enter the seed phrase
  print("Enter your seed phrase to access the password vault:")
  seed_phrase = getpass.getpass()
  # Hash the seed phrase to use as the password for the password vault
  password = hashlib.sha256(seed_phrase.encode()).hexdigest()
  # Open the password vault file and check the password
  with open("password_vault.txt", "r") as f:
    stored_password = f.read()
  if password == stored_password:
    print("Access granted. Welcome to the password vault.")
  else:
    print("Access denied. Incorrect seed phrase.")

def add_password(website, username, password):
  # Encrypt the password using the password vault password
  with open("password_vault.txt", "r") as f:
    password_vault_password = f.read()
  cipher = AES.new(password_vault_password, AES.MODE_EAX)
  ciphertext, tag = cipher.encrypt_and_digest(password.encode())
  # Store the encrypted password in the password vault file
  with open("password_vault.txt", "a") as f:
    data = [website, username, ciphertext, tag]
    f.write(base64.b64encode(pickle.dumps(data)).decode() + "\n")

def get_password(website, username):
  # Open the password vault file and search for the website and username
  with open("password_vault.txt", "r") as f:
    lines = f.readlines()
  for line in lines:
    data = pickle.loads(base64.b64decode(line))
    if data[0] == website and data[1] == username:
      # Decrypt the password using the password vault password
      password_vault_password = lines[0
