from PIL import Image
from android_client_handler import send_text_message, send_image_message
from message import Message, TextMessage, ImageMessage

if __name__== "__main__":

    # Devyansh sends a text message.
    message_1 = TextMessage()
    message_1.set_sender('SENDER_Devyansh')
    message_1.set_receiver('RECEIVER_Rohan')
    message_1.set_text_message_content('Hello, How are you doing?')

    send_text_message(message_1)

    # Rodric sends an image message.
    message_2 = ImageMessage()
    message_2.set_sender('SENDER_Rodric')
    message_2.set_receiver('RECEIVER_Steve')

    img_path = 'CrioLogo.png'
    img = Image.open(img_path)
    with open(img_path, "rb") as image:
        f = image.read()
        image_byte = bytes(f)
    message_2.set_image_message_content(image_byte,
                                        image_resolution=img.size, image_metadata=img.mode)
    send_image_message(message_2)

