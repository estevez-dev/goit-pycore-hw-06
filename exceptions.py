class PhoneFormatException(Exception):
    def __init__(self):
        super().__init__('Wrong phone number format')

class DuplicateContactException(Exception):
    def __init__(self):
        super().__init__('Contact already exist')

class DuplicatePhoneException(Exception):
    def __init__(self):
        super().__init__('Phone already added')