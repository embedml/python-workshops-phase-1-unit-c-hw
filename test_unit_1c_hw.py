
import random
from unit_1c_hw import *

def test_assign_1():
    assert assign_test_1() == 5, "X must be assigned to the integer 5"

def test_assign_2():
    assert assign_test_2() == "Hello NC State", "X must be assigned the string 'Hello NC State'"

def test_list_test_1():
    l = list_test_1()
    assert len(l) == 3, "List must only have 3 elements"
    assert l[0] == 3, "First index must have value 3"
    assert l[1] == 4, "Second index must have value 4"
    assert l[2] == 5, "Third Index must have value 5"

def test_list_test_2():
    l = list_test_2()
    assert len(l) == 3, "List must only have 3 elements"
    assert l[0] == 4, "First index must have value 4"
    assert l[1] == 7, "Second index must have value 7"
    assert l[2] == 9, "Third Index must have value 9"

def test_list_test_3():
    l = list_test_3()
    assert len(l) == 3, "List must only have 3 elements"
    assert l[0] == 4, "First index must have value 4"
    assert l[1] == 3, "Second index must have value 3"
    assert l[2] == 7, "Third Index must have value 7"

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
    assert noise == "meow", f"Noise was not the sounds of a cat: '{noise}'" # Note to instructor check this test manually as well, make sure student did not just pass in the string "meow"

def test_dict_test3():
    milk_tax = dict_test_3()
    assert milk_tax == 0.25, f"Value was not the milk tax: '{milk_tax}" # Note to instructor, check this test manually as well, make sure student did not pass in the value 0.25

def test_list_dict_test():
    colors = list_dict_test()
    assert "warm_colors" in colors, "warm_colors was not in the color dict "
    assert "cool_colors" in colors, "cool_colors was not in the color dict"
    warm_colors = colors["warm_colors"]
    cool_colors = colors["cool_colors"]
    assert len(colors) == 2, "You may have more than warm_colors and cool_colors as dict keys"
    assert len(warm_colors) == 3, "You must have 3 colors in the warm_colors list"
    assert len(cool_colors) == 3, "You must have 3 colors in teh cool_colors list"
    assert "yellow" in warm_colors, "yellow was not in warm colors"
    assert "orange" in warm_colors, "orange was not in warm colors"
    assert "red" in warm_colors, "red was not in warm colors"
    assert "green" in cool_colors, "green was not in cool colors"
    assert "blue" in cool_colors, "blue was not in cool colors"
    assert "purple" in cool_colors, "purple was not in cool colors"

def test_if_test():
    assert if_test(5) == "X is 5!", "When X is 5 must print 'X is 5!'"
    assert if_test(6) == "X is 6!", "When X is 6 must print 'X is 6!'"
    assert if_test(random.randint(7,100)) == "X is not 5 or 6!"
    assert if_test(random.randint(-100, 3)) == "X is not 5 or 6!"

def test_for_loop_test():
    l = for_loop_test()
    for num in l[1::4]:
        assert num == 2, "1 must be replaced with 2, did not find a 2 where a 1 was before"

def test_while_loop_test():
    break_num = while_loop_test()
    assert break_num == 5, f"Can only break on the num 5, you broke on the num '{break_num}'"
