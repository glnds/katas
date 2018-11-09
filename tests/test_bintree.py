from bintree import get_visible_nodes, Treenode


def test_empty_tree():
    assert get_visible_nodes(None) == -1


def test_one_node():
    assert get_visible_nodes(Treenode(11, None, None)) == 1


def test_multiple_nodes():
    assert get_visible_nodes(Treenode(11, Treenode(12, None, None), None)) == 2
    assert get_visible_nodes(Treenode(11, Treenode(4, None, None), None)) == 1
    assert get_visible_nodes(Treenode(
        11, Treenode(4, Treenode(12, None, None), None), None)
    ) == 2
    assert get_visible_nodes(Treenode(
        11, Treenode(4, Treenode(12, None, None), Treenode(50, None, None)), None)
    ) == 3
