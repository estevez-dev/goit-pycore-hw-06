from collections import UserDict
from exceptions import PhoneFormatException, DuplicateContactException, DuplicatePhoneException

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str):
        if value.isnumeric() and len(value) == 10:
            super().__init__(value)
        else:
            raise PhoneFormatException()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if self.find_phone(phone) != None:
            raise DuplicatePhoneException

        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        self.phones = list(filter(lambda p : p.value != phone, self.phones))

    def find_phone(self, query):
        return next((p for p in self.phones if p.value == query), None)

    def edit_phone(self, old_phone, new_phone):
        self.add_phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name in self.data:
            raise DuplicateContactException
        
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]

