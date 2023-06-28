# импорты функций из utils/utils_for_project.py
from utils.utils_for_project import load_json, get_list_processing, get_list_formatting, get_sorted_list, \
    get_last_five_transactions, hide_requisites_from


# оснвной блок, с вызовами функций и выводом статистики
def main():
    raw_transactions_list = load_json()
    executed_transactions_list = get_list_processing(raw_transactions_list)
    formatting_transactions_list = get_list_formatting(executed_transactions_list)
    sorted_transactions_list = get_sorted_list(formatting_transactions_list)
    last_transactions = get_last_five_transactions(sorted_transactions_list)
    for transaction in last_transactions:
        date_format = transaction['date'].strftime('%d.%m.%Y')
        print(f"{date_format} {transaction['description']}\n \
              \r{hide_requisites_from(transaction['from'])} -> {hide_requisites_from(transaction['to'])}\n \
              \r{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}\n")


if __name__ == '__main__':
    main()
