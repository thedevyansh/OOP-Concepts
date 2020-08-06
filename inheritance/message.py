class Message:
    MSG_TYPE_TEXT = 1
    MSG_TYPE_VOICE = 2
    MSG_TYPE_IMAGE = 3

    def __init__(self):
        # Common fields.
        self.__message_id = None
        self.__sender = None
        self.__receiver = None
        self.__message_type = None
        
    def set_sender(self, sender):
        self.__sender = sender

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver


class TextMessage(Message):
    def __init__(self):
      # Fields related to text message.
      self.__text_message_content = None
      self.__message_type = Message.MSG_TYPE_TEXT

    def set_text_message_content(self, text_message_content: str):
        self.__text_message_content = text_message_content

    def get_text_message_content(self):
        return self.__text_message_content

    def get_text_message_size(self):
        return len(self.__text_message_content)

class ImageMessage(Message):
    def __init__(self):
        # Fields related to image message.
        self.__image_message_content = None
        self.__image_resolution = None
        self.__image_metadata = None
        self.__message_type = Message.MSG_TYPE_IMAGE

    def set_image_message_content(self, image_message_content: bytes,
                                  image_resolution, image_metadata):
        self.__image_message_content = image_message_content
        self.__image_resolution = image_resolution
        self.__image_metadata = image_metadata

    def get_image_message_content(self):
        return self.__image_message_content

class VoiceMessage(Message):
    def __init__(self):
        # Fields related to voice message.
        self.__voice_message_content = None
        self.__voice_duration_in_sec = None
        self.__voice_quality_in_kbps = None
        self.__message_type = Message.MSG_TYPE_VOICE

    def set_voice_message_content(self, voice_message_content: str,
                                  voice_duration: int, voice_quality: int):
        self.__voice_message_content = voice_message_content
        self.__voice_duration_in_sec = voice_duration
        self.__voice_quality_in_kbps = voice_quality

    def get_voice_message_size(self):
        return len(self.__voice_message_content)
