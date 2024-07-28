import hashlib
import os

def validate_hash(hash, text, password_text):
    salted_data = (text).encode('utf-8')
    hash_object = hashlib.sha1(salted_data).hexdigest()
    if hash == hash_object:
        return password_text
    return ''

def read_passwords():
    file_path = 'top-10000-passwords.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def read_salts(use_salts):
    if use_salts:
        file_path = 'known-salts.txt'
        with open(file_path, 'r') as file:
            salts = file.readlines()
        return salts
    return ''

def crack_sha1_hash(hash, use_salts = False): 
    passwords = read_passwords()
    salts = read_salts(use_salts)

    for password in passwords:
        if use_salts:
            for salt in salts:
                prefix_salt = validate_hash(hash, salt.rstrip() + password.rstrip(), password.rstrip())
                if prefix_salt != '':
                    return prefix_salt

                sufix_salt = validate_hash(hash, password.rstrip() + salt.rstrip(), password.rstrip())
                if sufix_salt != '':
                    return sufix_salt
        else:
            no_salt = validate_hash(hash, password.rstrip(), password.rstrip())
            if no_salt != '':
                return no_salt

    return 'PASSWORD NOT IN DATABASE'