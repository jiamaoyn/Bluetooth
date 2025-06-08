from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

# AES 参数（与 ESP32 端保持一致）
AES_KEY = b"1234567890abcdef"  # 16字节
AES_IV = b"abcdef1234567890"  # 16字节

# 文件路径
INPUT_FOLDER = "/Users/wangjiamao/code/esp32s3/mp3qq/U盘/mp3"
OUTPUT_FOLDER = "/Users/wangjiamao/code/esp32s3/mp3qq/U盘/mp3_encrypted"


def aes_encrypt(data: bytes) -> bytes:
    ctr = Counter.new(128, initial_value=int.from_bytes(AES_IV, byteorder='big'))
    cipher = AES.new(AES_KEY, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(data)


def encrypt_file(input_path, output_path):
    with open(input_path, "rb") as f:
        raw_data = f.read()

    encrypted_data = aes_encrypt(raw_data)

    with open(output_path, "wb") as f:
        f.write(encrypted_data)

    print(f"✅ 加密成功: {output_path}")


def process_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".mp3"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            encrypt_file(input_path, output_path)


if __name__ == "__main__":
    process_folder(INPUT_FOLDER, OUTPUT_FOLDER)
