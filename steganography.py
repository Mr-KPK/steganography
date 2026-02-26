from PIL import Image

# Function to convert message to binary
def message_to_binary(message):
    return ''.join(format(ord(i), '08b') for i in message)

# Function to convert binary to message
def binary_to_message(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''.join(chr(int(char, 2)) for char in chars)
    return message

# Function to hide message in image
def encode_image(image_path, secret_message, output_path):
    image = Image.open(image_path)
    binary_message = message_to_binary(secret_message) + '1111111111111110'  # End delimiter
    
    data_index = 0
    pixels = list(image.getdata())
    
    new_pixels = []
    
    for pixel in pixels:
        r, g, b = pixel
        
        if data_index < len(binary_message):
            r = (r & ~1) | int(binary_message[data_index])
            data_index += 1
        
        if data_index < len(binary_message):
            g = (g & ~1) | int(binary_message[data_index])
            data_index += 1
        
        if data_index < len(binary_message):
            b = (b & ~1) | int(binary_message[data_index])
            data_index += 1
        
        new_pixels.append((r, g, b))
    
    image.putdata(new_pixels)
    image.save(output_path)
    print(" Message encoded successfully!")

# Function to extract message from image
def decode_image(image_path):
    image = Image.open(image_path)
    binary_data = ""
    
    pixels = list(image.getdata())
    
    for pixel in pixels:
        for color in pixel[:3]:
            binary_data += str(color & 1)
    
    # Split by delimiter
    delimiter = '1111111111111110'
    message_binary = binary_data.split(delimiter)[0]
    
    message = binary_to_message(message_binary)
    return message

# Menu
def main():
    print("🔐 Image Steganography Tool")
    print("1. Encode Message")
    print("2. Decode Message")
    
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        image_path = input("Enter input image path (PNG): ")
        secret_message = input("Enter secret message: ")
        output_path = input("Enter output image path: ")
        encode_image(image_path, secret_message, output_path)
    
    elif choice == '2':
        image_path = input("Enter encoded image path: ")
        message = decode_image(image_path)
        print("🔓 Hidden Message:", message)
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()