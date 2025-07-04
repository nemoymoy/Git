documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]



def get_name(doc_number):
    # your code
    n = ""
    for my_name in documents:
        if my_name["number"] == doc_number:
            n = my_name["name"]
    if n == "":
        n = "Документ не найден"
    return n

class Directory:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

    def get_directory(self, doc_number):
        # your code
        my_check = ""
        for k in self.directories:
            if doc_number in self.directories[k]:
                my_check = k
        if my_check == "":
            my_check = "Полки с таким документом не найдено"
        return my_check

    def add(self, document_type, number, name, shelf_number):
        # your code
        documents.append({"type" : document_type, "number" : number, "name" : name})
        self.directories.setdefault(shelf_number, number)
        return len(documents), len(self.directories)

if __name__ == '__main__':
    directory = Directory('Base')
    # print(get_name("10006"))
    print(directory.get_directory("11-2"))
    # print(get_name("101"))
    directory.add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(directory.get_directory("311 020203"))
    # print(get_name("311 020203"))
    print(directory.get_directory("311 020204"))