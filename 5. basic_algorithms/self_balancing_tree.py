class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = "R" if self.color == "red" else "B"
        return "%d%s" % (self.value, print_color)


def grandparent(node):
    if node.parent is None:
        return None
    return node.parent.parent


# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp is None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, "red")

    def __iter__(self):
        yield from self.root.__iter__()

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):  # same logic used in binary tree
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            current.right = Node(new_val, current, "red")
            return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            current.left = Node(new_val, current, "red")
            return current.left

    def rebalance(self, node):
        # case 1 root node
        if node.parent is None:  # inserting the root node
            return

        # case 2 parent is black
        if node.parent.color == "black":
            # we inserted a red node beneath a black node
            # the new children (the NULL nodes) are black by definition
            # our red node replaced a black NULL node
            # so the number of black nodes for any paths from parents is unchanged
            # Nothing to do in this case
            return

        # case 3 red parent and red pibling
        if pibling(node) and pibling(node).color == "red":  # pibling == parent sibling
            # both parent and pibling are red,
            # change them to black
            # change grandparent - then recursion over grandparent
            pibling(node).color = "black"
            node.parent.color = "black"
            grandparent(node).color = "red"
            return self.rebalance(grandparent(node))

        gp = grandparent(node)
        # Small change, if there is no grandparent, cases 4 and 5
        # won't apply
        if gp is None:
            return

        # case 4, red parent, black pibling - inside case
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # case 5, red parent, black pibling - outside case
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = "black"
        gp.color = "red"

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p


# TODO
# Current implementation will add duplicates of the same value.
# Change the implementation to mark how many times the same value has been inserted.

# Implement search and see how it remains logarithmic for large data sets
# def search(self, find_val):
#     return False

# Tinker with the rotations and early escapes to see how they break (use `print_tree`)
# Consider adding deletion or sketching out how it should work
