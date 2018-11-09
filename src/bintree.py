

# define a class
class Treenode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def get_visible_nodes(tree):
    if not tree:
        return -1
    threshold = tree.value

    i = 0
    for n in traverse(tree, threshold):
        i += 1
    return i


def traverse(tree, threshold):
    if tree.left is not None and tree.value <= threshold:
        yield from traverse(tree.left, threshold)

    if tree.value >= threshold:
        yield tree.value

    if tree.right is not None and tree.value <= threshold:
        yield from traverse(tree.right, threshold)
