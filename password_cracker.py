import hashlib

def crack_sha1_hash(hash, use_salts = False): #TODO salt reading known-salts.txt
    file_path = 'top-10000-passwords.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        hash_object = hashlib.sha1(line.rstrip().encode('utf-8')).hexdigest()
        if hash == hash_object:
            return line.rstrip()
        # print(line.strip())

    return 'PASSWORD NOT IN DATABASE'

# print(crack_sha1_hash("b80abc2feeb1e37c66477b0824ac046f9e2e84a0")) #bubbles1
print(crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True)) #bubbles1