from PIL import Image
from android_client_handler import send_message
from message import Message, TextMessage, ImageMessage

if __name__== "__main__":

    # Amar sends a text message.
    message_1 = TextMessage()
    message_1.set_sender('SENDER_Amar')
    message_1.set_receiver('RECEIVER_Abhinaya')
    message_1.set_message_content('Hello, How are you doing?')

    send_message(message_1)

    # Amulya sends an image message.
    message_2 = ImageMessage()
    message_2.set_sender('SENDER_Amulya')
    message_2.set_receiver('RECEIVER_Cratos')

    img_path = 'CrioLogo.png'
    img = Image.open(img_path)
    with open(img_path, "rb") as image:
        f = image.read()
        image_byte = bytes(f)
    message_2.set_message_content(image_byte,
                                  image_resolution=img.size, image_metadata=img.mode)
    send_message(message_2)

