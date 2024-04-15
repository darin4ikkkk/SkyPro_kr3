import json


# Функция открывает файл и загружает данные из него
def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
        # print(data)


loaded_file = load_file('operations.json')


# Фильтрация УСПЕШНЫХ операций
def sort_executed(filename):
    executed = []
    for item in filename:
        if item['state'] == "EXECUTED":
            executed_oper = executed.append(item)

    #return executed_oper
    print(executed_oper)


sort_executed(loaded_file)
