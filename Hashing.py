import hashlib

filename = 'vault.txt'

sha256_hash = hashlib.sha256()

with open(filename, "rb") as f:

    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096), b""):

        sha256_hash.update(byte_block)

        key = open('vaultKey.txt', 'a')
        key.write(f"{sha256_hash.hexdigest()}\n")
        key.close()

    print(sha256_hash.hexdigest())