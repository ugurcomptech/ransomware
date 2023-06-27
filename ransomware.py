import os
from cryptography.fernet import Fernet

# Şifreleme anahtarını oluştur
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Şifreleme anahtarını yükle
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Dosyayı şifrele
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Dosyayı çöz
def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Belirlediğiniz klasördeki dosyaları şifrele veya çöz
def encrypt_or_decrypt_files(folder_path, key, encrypt=True):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if encrypt:
                encrypt_file(file_path, key)
            else:
                decrypt_file(file_path, key)

# Şifreleme anahtarını oluştur
generate_key()

# Şifreleme anahtarını yükle
key = load_key(e)

# Belirlediğiniz klasördeki dosyaları şifrele
encrypt_or_decrypt_files("C:/Users/uğur/Desktop/deneme", key, encrypt=True)
