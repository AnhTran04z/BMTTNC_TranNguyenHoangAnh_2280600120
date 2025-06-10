from Crypto.Hash import SHA3_256  # Sửa "hash" thành "Hash"

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')  # Sửa "Nhap chuoi van ban" thành "Nhập chuỗi văn bản"
    hashed_text = sha3(text)
    
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))  # Sửa "Chuoi van ban da nhap" thành "Chuỗi văn bản đã nhập"
    print("SHA-3 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()
