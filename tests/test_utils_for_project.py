from utils.utils_for_project import *


def test_get_list_processing(tests_data):
    assert len(get_list_processing(tests_data)) == 2


def test_get_list_formatting(tests_data):
    assert len(get_list_formatting(tests_data)) == 3


def test_get_sorted_list(tests_data):
    assert len(get_sorted_list(tests_data)) == 3


def test_get_last_five_transactions(tests_data):
    assert len(get_last_five_transactions(tests_data[:2])) == 2


def test_hide_requisites_from(tests_data):
    assert hide_requisites_from("Visa Platinum 2241653116508487") == 'Visa Platinum 2241 65** **** 8487'
    assert hide_requisites_from("МИР 8201420097886664") == 'МИР 8201 42** **** 6664'
    assert hide_requisites_from("Счет 44238164562083919420") == 'Счет **9420'
    assert hide_requisites_from("Visa Gold 6527183396477720") == 'Visa Gold 6527 18** **** 7720'
    assert hide_requisites_from("Maestro 7810846596785568") == 'Maestro 7810 84** **** 5568'
    assert hide_requisites_from("MasterCard 1435442169918409") == 'MasterCard 1435 44** **** 8409'
    assert hide_requisites_from(tests_data[0]['from']) == 'Maestro 1596 83** **** 5199'
    assert hide_requisites_from(tests_data[0]['to']) == 'Счет **9589'
    assert hide_requisites_from(None) == 'Пополнение'
