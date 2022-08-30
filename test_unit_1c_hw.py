from unit_1c_hw import *


def test_assign_1():
    assert assign_test_1() == 5, "X must be assigned to the integer 5"

def test_assign_2():
    assert assign_test_2 == "Hello NC State", "X must be assigned the string 'Hello NC State'"

def test_list_test_1():
    l = list_test_1()
    assert len(l) == 3, "List must only have 3 elements"
    assert l[0] == 3, "First index must have value 3"
    assert l[1] == 4, "Second index must have value 4"
    assert l[2] == 5, "Third Index must have value 5"

def test_list_test_2():
    l = list_test_3()
    assert len(l) == 3, "List must only have 3 elements"
    assert l[0] == 4, "First index must have value 3"
    assert l[1] == 3, "Second index must have value 4"
    assert l[2] == 7, "Third Index must have value 5"

def test_list_test_4():
    l = list_test_4()
    assert l == [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0], f"List was not sliced correctly, your list: {l}"

def test_dict_test_1():
    d = dict_test_1()
    assert len(d) == 3, "Dictionary must have 3 keys"
    assert d[0] == "A", "Key 0 must have value A"
    assert d[1] == "B", "Key 1 must have value B"
    assert d[2] == "C", "Key 2 must have value C"

def test_dict_test_2():
    noise = dict_test_2()
    assert noise == "meow" # Note to instructor check this test manually as well, make sure student did not just pass in the string "meow"

def test_dict_test3():
    milk_tax = dict_test_3()
    assert milk_tax == 0.25 # Note to instructor, check this test manually as well, make sure student did not pass in the value 0.25

def test_list_dict_test():
    colors = list_dict_test()
    warm_colors = colors["warm_colors"]
    cool_colors = colors["cool_colors"]
    assert len(colors) == 2
    assert len(warm_colors) == 3
    assert len(cool_colors) == 3

