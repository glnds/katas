from bintree import get_visible_nodes, Treenode


def test_empty_tree():
    assert get_visible_nodes(None) == -1


def test_one_node():
    assert get_visible_nodes(Treenode(11, None, None)) == 1


def test_multiple_nodes():
    n15 = Treenode(7, None, None)
    n14 = Treenode(4, None, None)
    n13 = Treenode(33, None, None)
    n12 = Treenode(49, None, n15)
    n11 = Treenode(21, n13, n14)
    n10 = Treenode(31, None, None)
    n9 = Treenode(37, None, None)
    n8 = Treenode(6, None, n12)
    n7 = Treenode(12, None, None)
    n6 = Treenode(2, None, n11)
    n5 = Treenode(3, n9, n10)
    n4 = Treenode(9, n7, n8)
    n3 = Treenode(7, None, n6)
    n2 = Treenode(4, n4, n5)
    root = Treenode(8, n2, n3)  # Btw let's play with merkle threes some day ;)

    assert get_visible_nodes(Treenode(11, Treenode(12, None, None), None)) == 2
    assert get_visible_nodes(Treenode(11, Treenode(4, None, None), None)) == 1
    assert get_visible_nodes(Treenode(
        11, Treenode(4, Treenode(12, None, None), None), None)
    ) == 2

    assert get_visible_nodes(Treenode(
        11, Treenode(4, Treenode(12, None, None), Treenode(50, None, None)), None)
    ) == 3

    assert get_visible_nodes(Treenode(
        11, Treenode(40, Treenode(12, None, None), Treenode(50, None, None)), None)
    ) == 2

    # Let's put it that way: for the algorithm in my head this is the expected result :)
    assert get_visible_nodes(root) == 5
