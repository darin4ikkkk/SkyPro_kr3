import json
from datetime import date


# Функция открывает файл и загружает данные из него
def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


loaded_file = load_file('operations.json')


# Фильтрация УСПЕШНЫХ операций
def sort_executed(data):
    executed = []
    for item in data:
        key = item.get('state')
        if key == "EXECUTED":
            executed.append(item)
    return executed


sorted_executed_oper = sort_executed(loaded_file)


def sorted_by_date(data):
    return data.get('date')

# Сортировка операций по дате
def data_sort(data):
    sorted_operations = sorted(data, key=sorted_by_date, reverse=True)
    return sorted_operations


sorted_operations = data_sort(sorted_executed_oper)
sorted_operations = sorted_operations[:5]


# Форматируем дату
def format_date(data):
    thedate = date.fromisoformat(data[:10])
    date_formatted = thedate.strftime("%d.%m.%Y")  # День Месяц Год
    return date_formatted


# Маскируем номер карты или счёта
def card_num_mask(card_num):
    len_num = len(card_num)
    if "Счет" in card_num:
        card_num_masked = card_num.replace(card_num[(len_num-20):(len_num-4)],"****************")
    else:
        card_num_masked = card_num.replace(card_num[(len_num - 10):(len_num - 4)], "** **** ")
    return card_num_masked




