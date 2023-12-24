from src.utils import get_data, sort_operations, sort_descending_order, hide_requisites, correct_format_data
from config import ROOT_DIR, DATA_DIR
def test_get_data():
    assert type(get_data()) == list
    assert type(get_data()[1]) == dict

def test_sort_operations():
    operations = sort_operations()
    for operation in operations:
        assert "EXECUTED" in operation["state"]
        assert "CANCELED" not in operation["state"]

def test_sort_descending_order():
    operations = sort_descending_order()
    for i in range(len(operations) - 1):
        assert operations[i]["date"] > operations[i + 1]["date"]
        i += 1

def test_correct_format_data():
    assert correct_format_data("2018-01-21T01:10:28.317704") == "21.01.2018"
    assert correct_format_data("2018-04-04T17:33:34.701093") == "04.04.2018"
    assert correct_format_data("2019-05-19T12:51:49.023880") == "19.05.2019"

def test_hide_requisites():
    assert hide_requisites("Maestro 1596837868705199") == "Maestro 1596 83** ****5199"
    assert hide_requisites("Счет 64686473678894779589") == "Счет **9589"
    assert hide_requisites("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** ****5229"
    assert hide_requisites("MasterCard 3152479541115065") == "MasterCard 3152 47** ****5065"
    assert hide_requisites("МИР 8201420097886664") == "МИР 8201 42** ****6664"
