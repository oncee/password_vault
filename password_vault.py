import hashlib
import base64
import pickle
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password

def create_seed_phrase():
  # Generate a random 24-word seed phrase
  seed_phrase = ""
  words = ["word1", "word2", "word3", ..., "word24"]
  for i in range(24):
    seed_phrase += words[random.randint(0, len(words)-1)] + " "
  return seed_phrase.strip()

def create_password_vault(request):
  if request.method == "POST":
    # Hash the seed phrase and passphrase to use as the password for the password vault
    seed_phrase = request.POST.get("seed_phrase")
    passphrase = request.POST.get("passphrase")
    password = hashlib.sha256((seed_phrase + passphrase).encode()).hexdigest()
    # Create a new password vault file
    with open("password_vault.txt", "w") as f:
      f.write(password)
    return redirect("login")
  else:
    # Prompt the user to create a seed phrase and a passphrase
    context = {
      "seed_phrase": create_seed_phrase()
    }
    return render(request, "create_password_vault.html", context)

def login(request):
  if request.method == "POST":
    # Hash the seed phrase and passphrase to use as the password for the password vault
    seed_phrase = request.POST.get("seed_phrase")
    passphrase = request.POST.get("passphrase")
    password = hashlib.sha256((seed_phrase + passphrase).encode()).hexdigest()
    # Open the password vault file and check the password
    with open("password_vault.txt", "r") as f:
      stored_password = f.read()
    if check_password(password, stored_password):
      request.session["logged_in"] = True
      return redirect("home")
    else:
      return HttpResponse("Incorrect seed phrase or passphrase.")
  else:
    return render(request, "login.html")

def home(request):
  if not request.session.get("logged_in"):
    return redirect("login")
  return render(request, "home.html")

def add_password(request):
  if not request.session.get("logged_in"):
    return redirect("login")
  if request.method == "POST":
    # Encrypt the password using the password vault password
    with open("password_vault.txt", "r") as f:
      password_vault_password = f.read()
    cipher = AES.new(password_vault_password, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(request.POST.get("password").encode())
    #

