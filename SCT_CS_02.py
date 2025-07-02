from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img_data = np.array(img)
    key = np.resize(key, img_data.shape)
    encrypted_data = np.bitwise_xor(img_data, key)
    Image.fromarray(encrypted_data).save('encrypted_image.png')
    print('✅ Encrypted image saved as encrypted_image.png')

def decrypt_image(encrypted_path, key):
    encrypted_img = Image.open(encrypted_path)
    encrypted_data = np.array(encrypted_img)
    key = np.resize(key, encrypted_data.shape)
    decrypted_data = np.bitwise_xor(encrypted_data, key)
    Image.fromarray(decrypted_data).save('decrypted_image.png')
    print('✅ Decrypted image saved as decrypted_image.png')

if __name__ == "__main__":
    image_path = input('Enter path to your image file: ')
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
    print('Generated key:', key)
    encrypt_image(image_path, key)
    decrypt_image('encrypted_image.png', key)
