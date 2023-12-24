import json
from operator import itemgetter
from config import DATA_DIR


def get_data():
    """
    Считывает данные из JSON и возвращает список словарей
    """
    with open(DATA_DIR, encoding="utf8") as file:
        json_data = file.read()
        data_operation = json.loads(json_data)
    return data_operation

def sort_operations():
    """
    Возвращает новый список только с выполненными (EXECUTED) операциями
    """
    sorted_list = []
    unsorted_list = get_data()
    for operation in unsorted_list:
        for key, value in operation.items():
            if value == "EXECUTED":
                sorted_list.append(operation)
    return sorted_list

def sort_descending_order():
    """
    Возвращает отсортированный по дате (по убыванию) новый список
    """
    unsorted_list = sort_operations()
    sorted_data_list = sorted(unsorted_list, key=itemgetter("date"), reverse=True)
    return sorted_data_list

def correct_format_data(date):
    """
    Возвращает дату операции в формате ДД.ММ.ГГГГ
    """
    original_data = date[:10]
    data_list = original_data.split("-")
    correct_data = '.'.join(data_list[::-1])
    return correct_data

def hide_requisites(requisites:str):
    """
    Возвращает замаскированный номер карты
    (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом)
    или
    возвращает замаскированный номер счета
    (видны только последние 4 цифры)
    """
    parts = requisites.split()
    number = parts[-1]
    if requisites.lower().startswith('счет'):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** ****{number[-4:]}"
    parts[-1] = hided_number
    return ' '.join(parts)
def get_formated_operation(operation):
    """
    Функция формирования строк на вывод
    """
    # Line_1
    formated_data = correct_format_data(operation['date'])
    type_operation = operation['description']
    line_one = f"{formated_data} {type_operation}"

    # Line_2
    if operation.get('from'):
        hided_from = hide_requisites(operation.get('from'))
    else:
        hided_from = 'Нет данных'
    hided_to = hide_requisites(operation.get('to'))
    line_two = f"{hided_from} -> {hided_to}"

    # Line_3
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    line_three = f"{amount} {currency}"

    return f"{line_one}\n{line_two}\n{line_three}\n"


def output_screen():
    """
    Выводит на экран данные по последним 5 выполненным операциям
    """
    operations = sort_descending_order()
    for operation in operations[:5]:
        print(get_formated_operation(operation))

