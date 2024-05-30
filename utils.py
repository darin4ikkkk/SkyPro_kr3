import json
from datetime import date


# Функция открывает файл и загружает данные из него
def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


# Фильтрация УСПЕШНЫХ операций
def sort_executed(data):
    executed = []
    for item in data:
        key = item.get('state')
        if key == "EXECUTED":
            executed.append(item)
    return executed


def sorted_by_date(data):
    return data.get('date')

# Сортировка операций по дате
def data_sort(data):
    sorted_operations = sorted(data, key=sorted_by_date, reverse=True)
    return sorted_operations


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
    elif card_num == "None":
        card_num_masked = "Неизвестный отправитель"
    else:
        card_num_maska = card_num.replace(card_num[(len_num - 10):(len_num - 4)], "** **** ")
        new_len = len(card_num_maska)
        num_list = list(card_num_maska)
        num_list[new_len - 15] = card_num_maska[new_len - 15] + " "
        card_num_masked = ''.join(num_list)

    return card_num_masked


# Выводит данные об операции
def print_data(sorted_operations):
    res = ''
    for i in sorted_operations:
        date = format_date(i["date"])
        card_num_from = str(i.get('from'))
        card_num_to = str(i.get('to'))
        masked_num_from = card_num_mask(card_num_from)
        masked_num_to = card_num_mask(card_num_to)
        operation_sum = i["operationAmount"]["amount"]
        currency = i["operationAmount"]["currency"]["name"]
        res = res + f'''{date} Перевод организации
{masked_num_from} -> {masked_num_to}
{operation_sum} {currency}

'''
    return res

