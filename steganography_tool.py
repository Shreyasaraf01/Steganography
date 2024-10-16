from PIL import Image

def encode(image_path, message):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to RGB mode if it isn't already
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Make a copy of the image for encoding
    encoded_image = image.copy()

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # End of message delimiter
    data_index = 0

    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            pixel = list(encoded_image.getpixel((x, y)))

            # Modify the least significant bit of each color channel
            for i in range(3):  # For R, G, B channels
                if data_index < len(binary_message):
                    # Set the LSB of the pixel color
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])
                    data_index += 1

            # Update the pixel in the encoded image
            encoded_image.putpixel((x, y), tuple(pixel))

            # Break if the entire message has been encoded
            if data_index >= len(binary_message):
                break

    # Save the encoded image
    encoded_image.save("encoded_image.png")
    print("Message hidden successfully!")

def decode(image_path):
    # Open the encoded image file
    image = Image.open(image_path)

    binary_message = ""
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            # Get the LSB from each color channel
            for i in range(3):
                binary_message += str(pixel[i] & 1)

    # Split the binary message by the end delimiter
    message_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_message = ""

    for byte in message_bytes:
        if byte == "11111111":  # Stop if the delimiter is reached
            break
        decoded_message += chr(int(byte, 2))

    return decoded_message

def main():
    action = input("Would you like to (e)ncode or (d)ecode? ")
    if action.lower() == 'e':
        image_path = input("Enter the path to the image: ")
        message = input("Enter the message to hide: ")
        encode(image_path, message)
    elif action.lower() == 'd':
        image_path = input("Enter the path to the encoded image: ")
        print("Decoded message:", decode(image_path))
    else:
        print("Invalid action. Please choose 'e' to encode or 'd' to decode.")

if __name__ == "__main__":
    main()
