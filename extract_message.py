import cv2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Decryption function
def decrypt_message(encrypted_data, key):
    iv = encrypted_data[:16]  # First 16 bytes are IV
    ct = encrypted_data[16:]  # Rest is ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

# Extract data from image
def extract_data(image_path, key):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image.")
        return

    # Extract bits from LSB
    data_bin = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = img[i, j]
            for k in range(3):  # R, G, B
                data_bin += str(pixel[k] & 1)  # Get LSB

    # Convert binary to bytes
    data_bytes = bytearray()
    for i in range(0, len(data_bin), 8):
        byte = data_bin[i:i+8]
        if len(byte) == 8:
            data_bytes.append(int(byte, 2))

    # Find the 'END' marker
    end_index = data_bytes.find(b'END')
    if end_index == -1:
        print("Error: No hidden data found.")
        return
    encrypted_data = bytes(data_bytes[:end_index])

    # Decrypt and show the message
    message = decrypt_message(encrypted_data, key)
    print("Hidden Message:", message)

# Main execution
if __name__ == "__main__":
    image_path = "output.png"  # Image with hidden data
    key = bytes.fromhex("2f719ef0cd2e525bec826b606917e256")  # Replace with the key from Step 3

    extract_data(image_path, key)