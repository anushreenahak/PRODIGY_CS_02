from PIL import Image
import numpy as np

# Encrypt Function
def encrypt_image(image_path, output_image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Apply basic pixel manipulation (e.g., add a constant or use XOR)
    key = np.random.randint(0, 256, size=img_array.shape, dtype=np.uint8)
    encrypted_array = np.bitwise_xor(img_array, key)  # XOR operation with key

    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Encrypted image saved at {output_image_path}")

    # Return the key for decryption
    return key

# Decrypt Function
def decrypt_image(encrypted_image_path, output_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img)

    # Decrypt the image using XOR with the same key
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Decrypted image saved at {output_image_path}")

# Main function
def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    # Paths to input and output images
    input_image_path = "C:/Users/Anushree Nahak/Desktop/Prodigy Infotech/encrypted_img.png"
    encrypted_image_path = "C:/Users/Anushree Nahak/Desktop/Prodigy Infotech/encrypted_output.png"
    decrypted_image_path = "C:/Users/Anushree Nahak/Downloads/decrypted_output.png"

    # Encrypt the image
    key = encrypt_image(input_image_path, encrypted_image_path)
    
    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path, key)

if __name__ == "__main__":
    main()