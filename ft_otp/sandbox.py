from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# f = Fernet(key=key)

# message = "Text secret".encode()
# print(f"message = {message}")
# encrypted = f.encrypt(message)
# print(f"encrypted message = {encrypted.decode()}")

# code =input("msg codé : ")
# try:
#     decrypted = f.decrypt(code.encode())
#     print(f"decrypted message = {decrypted.decode()}")
# except Exception as e:
#     print(f"Error : {e}")

# finally:
#     print("end")

def retrieve_original_key(fernet_key_file="fernet.key", encrypted_key_file="ft_otp.key"):
    """
    Retrieves and displays the original content of 'key.hex' from 'ft_otp.key'.
    
    Args:
    fernet_key_file (str): The file containing the Fernet key used for encryption.
    encrypted_key_file (str): The file containing the encrypted key.

    Returns:
    None
    """
    try:
        # Lire la clé Fernet
        with open(fernet_key_file, "rb") as file:
            fernet_key = file.read()

        # Créer une instance de Fernet avec la clé lue
        fernet = Fernet(fernet_key)

        # Lire le contenu chiffré de 'ft_otp.key'
        with open(encrypted_key_file, "rb") as file:
            encrypted_key = file.read()

        # Déchiffrer le contenu
        decrypted_key = fernet.decrypt(encrypted_key).decode()

        # Afficher le contenu déchiffré
        print(decrypted_key)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Appel de la fonction
retrieve_original_key()