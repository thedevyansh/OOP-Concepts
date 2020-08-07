from PIL import Image

from message import Message

def send_message(message: Message):
    # 1. Discard invalid messages.
    if not message.is_valid():
        raise Exception('Invalid message')

    # 2. Ensure content is not offensive.
    check_for_offensive_content(message)

    # 3. Store the message safely.
    store_message(message)

    # 4. Deliver the message to the receiver.
    deliver_message_to_receiver(message)

def store_message(message: Message):
    print ('Message {} stored successfully'.format(message))

def check_for_offensive_content(message: Message):
    if (message.is_offensive()):
        raise Exception('Abusive language used; Discard')

def deliver_message_to_receiver(message: Message):
  
    if (message.is_too_large()):
        raise Exception('Message too large to send {}', message.get_message_size())

    print ('Message "{}" delivered successfully to {}'.format(message.get_message_content(),
                                                              message.get_receiver()))
