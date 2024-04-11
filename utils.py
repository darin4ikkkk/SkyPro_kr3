import json

# Функция открывает файл и загружает данные из него
def load_file(filename):
    file = open(filename, 'r')
    json_loaded = json.load(file)
    return json_loaded

# Фильтрация УСПЕШНЫХ операций
