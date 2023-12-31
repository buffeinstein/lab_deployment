from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):

    def __init__(self, xs=None, left=None, right=None):
        super().__init__()
        if type(xs) == int:
            self.insert(xs)

        if type(xs) == list:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.
        '''
        lst1 = self.inorder(self.root, [])
        lst2 = self.inorder(t2.root, [])
        if lst1 == lst2:
            return True
        return False

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''

        lst = self.inorder(self.root, [])
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False

        if self.root:
            return BST._is_bst_satisfied(self.root)

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:
        it only checks if the children of the current node are less than/greater than,
        rather than ensuring that all nodes to the left/right are less than/greater than.

        HINT:
        Use the _find_smallest and _find_largest functions to fix the bug.
        You should use the _ prefixed methods because those are static methods just like this one.
        '''

    def insert(self, value):
        if self.root:
            return self._insert(value, self.root)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                BST._insert(value, node.left)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                BST._insert(value, node.right)

    def insert_list(self, xs):
        if len(xs) != 0:
            for num in xs:
                self.insert(num)

    def __contains__(self, value):
        return self.find(value)

    def find(self, value):
        if self.root:
            return self._find(value, self.root)
        else:
            return False

    @staticmethod
    def _find(value, node):
        ret = True
        if value == node.value:
            return True

        elif value < node.value:
            if node.left is None:
                return False
            else:
                ret &= BST._find(value, node.left)
        elif value > node.value:
            if node.right is None:
                return False
            else:
                ret &= BST._find(value, node.right)

        return ret

    def find_smallest(self):
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        HINT:
        You should have everything else working before you implement this function.

        '''
        if not self.root:
            return
        self.root = BST._remove(self.root, value)

    @staticmethod
    def _remove(node, value):
        if not node:
            return node
        if value < node.value:
            node.left = BST._remove(node.left, value)
        elif value > node.value:
            node.right = BST._remove(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = BST._find_smallest(node.right)
            node.value = temp
            node.right = BST._remove(node.right, temp)

        return node

    def remove_list(self, xs):
        for x in xs:
            self.remove(x)

    def __iter__(self):
        for x in self.to_list('inorder'):
            yield x
