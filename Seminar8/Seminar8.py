import json

FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
PHONE = 'phone'
ID = 'id'
PEOPLE = 'people'

class PhoneBook():
    def __init__(self, path):
        self.path = path
        self.data:dict = self.read()
       
    def read(self):
        with open(self.path, 'r') as data:
            return json.load(data)

    def save(self):
        with open(self.path, 'w') as data:
            json.dump(self.data, data)

    def append(self):
        person = {}
        person[ID] = self.data[ID] = self.data[ID] + 1
        person[FIRST_NAME] = input('Введите имя: ')
        person[LAST_NAME] = input('Введите фамилию: ')
        person[PHONE] = input('Введите телефон: ')
        self.data[PEOPLE].append(person)
        self.save()

    def print_all(self):
        for person in self.data[PEOPLE]:
            self.print_concrete(person)

    def print_concrete(self, person):
        print(f'{person[ID]}, {person[FIRST_NAME]} {person[LAST_NAME]}, {person[PHONE]}')

    def find(self, substring:str):
        for person in self.data[PEOPLE]:
            if substring in person[FIRST_NAME] or substring in person[LAST_NAME]:
                self.print_concrete(person)

    def delete(self, id:int):
        for person in self.data[PEOPLE]:           
            if person[ID] == id:             
                self.data[PEOPLE].remove(person)
                self.save()

    def change(self, id:int):
        for person in self.data[PEOPLE]:           
            if person[ID] == id:
                name = input(f'Input lastname: ')             
                if name != '': person[LAST_NAME] = name
                name = input(f'Input firstname: ')             
                if name != '': person[FIRST_NAME] = name
                phone = input(f'Input phone number: ')             
                if phone != '': person[PHONE] = phone
                self.save()
                

def welcome():
    print('1 - Show all items')    
    print('2 - Add item')    
    print('3 - find item')    
    print('4 - Delete item by id') 
    print('5 - Change item by id')
    print('6. Exit')

def main():
    book = PhoneBook('Seminar8/file.json') 
    while True:
        welcome()    
        command = input('> ')
        if command == '1':
            book.print_all()
        elif command == '2':
            book.append()
        elif command == '3':
            substring = input('Input name: ')
            book.find(substring)
        elif command == '4':
            id = int(input('Input id: '))
            book.delete(id)
        elif command == '5':
            id = int(input('Input id: '))
            book.change(id)
        elif command == '6':
            break
        else: print('Error\n', '\r>')

main()