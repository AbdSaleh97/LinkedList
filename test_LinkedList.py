import pytest
from LinkedList import LinkedList
from Node import Node

def test_linked_list_initialization():
    ll = LinkedList()
    assert ll.head is None
    assert len(ll) == 0
    assert str(ll) == ""

def test_str_empty_list():
    ll = LinkedList()
    assert str(ll) == ""

def test_len_empty_list():
    ll = LinkedList()
    assert len(ll) == 0

def test_len_after_appending_elements():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert len(ll) == 3

def test_getitem_valid_index():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll[0] == 10
    assert ll[1] == 20
    assert ll[2] == 30

def test_getitem_invalid_index():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    with pytest.raises(IndexError):
        ll[3]
    with pytest.raises(IndexError):
        ll[-1]

def test_getitem_first_element():
    ll = LinkedList()
    ll.append(100)
    ll.append(200)
    ll.append(300)
    assert ll[0] == 100

def test_getitem_last_element():
    ll = LinkedList()
    ll.append(100)
    ll.append(200)
    ll.append(300)
    assert ll[2] == 300

def test_getitem_negative_index():
    ll = LinkedList()
    ll.append(100)
    ll.append(200)
    ll.append(300)
    with pytest.raises(IndexError):
        ll[-1]

def test_getitem_index_out_of_range():
    ll = LinkedList()
    ll.append(100)
    ll.append(200)
    with pytest.raises(IndexError):
        ll[5]

def test_getitem_single_element_list():
    ll = LinkedList()
    ll.append(50)
    assert ll[0] == 50
    with pytest.raises(IndexError):
        ll[1]

def test_getitem_empty_list():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll[0]

if __name__ == "__main__":
    pytest.main()
