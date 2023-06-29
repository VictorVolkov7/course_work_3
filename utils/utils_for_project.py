# импорты стандартных библиотек для работы с датой и json
import datetime
import json

# импорт пути до данных
from settings.project_path import OPERATIONS_JSON_PATH


def load_json() -> list[dict]:
    """
    загружает json файл и
    возвращает список
    """
    with open(OPERATIONS_JSON_PATH) as file:
        return json.load(file)


def get_list_processing(transactions_list: list[dict]) -> list[dict]:
    """
    принимает список транзакций,
    возвращает только успешные переводы
    """
    executed_list = []
    for transaction in transactions_list:
        if 'state' not in transaction:
            continue
        elif transaction['state'] == 'EXECUTED':
            executed_list.append(transaction)
    return executed_list


def get_list_formatting(executed_transactions_list: list[dict]) -> list[dict]:
    """
    принимает обработанный список успешных переводов
    и вытаскивает дату из строки
    возвращает отформатированный список
    """
    for transaction in executed_transactions_list:
        transaction['date'] = datetime.datetime.fromisoformat(transaction['date'])
    return executed_transactions_list


def get_sorted_list(formatting_list: list[dict]) -> list[dict]:
    """
    принимает отформатированный список успешных операций и
    возвращает отсортированный список по дате
    """
    sorted_operations = sorted(formatting_list, key=lambda op: op['date'], reverse=True)
    return sorted_operations


def get_last_five_transactions(sorted_transaction_list: list[dict]) -> list[dict]:
    """
    принимает отсортированный список и
    возвращает список последних успешных транзакций
    """
    return sorted_transaction_list[:5]


def hide_requisites_from(last_transaction) -> str:
    """
    принимает реквизиты(получателя/отправителя),
    сплитит его на слова,
    далее идет проверка по первому слову для определения карты или счета
    возвращает скрытые реквизиты
    """
    if last_transaction is None:
        return 'Пополнение'

    requisites: str = last_transaction.split(' ')[-1]
    payment_system: str = ' '.join(last_transaction.split(' ')[:-1])
    if payment_system == 'Счет':
        hide_requisites = f'{payment_system} **{requisites[-4:]}'
    else:
        first_four_elements: str = requisites[:4]
        second_two_elements: str = requisites[4:6]
        last_four_elements: str = requisites[-4:]
        hide_requisites = f'{payment_system} {first_four_elements} {second_two_elements}** **** {last_four_elements}'
    return hide_requisites
