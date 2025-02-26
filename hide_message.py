import cv2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Encryption function
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ct_bytes  # IV + ciphertext

# Hide data in image
def hide_data(image_path, secret_message, output_path, key):
    # Read the image
    img = cv2.imread("Screenshot 2025-01-10 180616.png")
    if img is None:
        print("Error: Could not load image.")
        return

    # Encrypt the message
    encrypted_data = encrypt_message(secret_message, key)
    data = encrypted_data + b'END'  # Add a marker to know where data ends

    # Check if image can hold the data
    height, width, _ = img.shape
    max_bytes = (height * width * 3) // 8
    if len(data) > max_bytes:
        print("Error: Message too large for this image.")
        return

    # Convert data to binary
    data_bin = ''.join(format(byte, '08b') for byte in data)
    data_index = 0

    # Hide data in LSB of each pixel
    for i in range(height):
        for j in range(width):
            pixel = list(img[i, j])
            for k in range(3):  # R, G, B channels
                if data_index < len(data_bin):
                    # Replace LSB with data bit
                    pixel[k] = (pixel[k] & 0xFE) | int(data_bin[data_index])
                    data_index += 1
            img[i, j] = tuple(pixel)
            if data_index >= len(data_bin):
                break
        if data_index >= len(data_bin):
            break

    # Save the new image
    cv2.imwrite(output_path, img)
    print(f"Message hidden successfully in {output_path}")

# Main execution
if __name__ == "__main__":
    image_path = "host.png"           # Your input image
    secret_message = "hi my name is sudnyesh"  # Your secret message
    output_path = "output.png"        # Output image with hidden data
    key = get_random_bytes(16)        # 16-byte key for AES-128

    hide_data(image_path, secret_message, output_path, key)
    print("Key (keep this safe!):", key.hex())  # Save this key for decoding