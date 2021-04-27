class Trie_node:
    def __init__(self, char):
        # Pass as argument to make a node
        self.char = char
        # Initialize dictionary
        self.children = {}
        self.is_end_of_world = False


class Trie:
    def __init__(self):
        self.root = Trie_node("")
        self.arr = []

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]  # be the child of current node
            else:
                new_node = Trie_node(char)  # make new node
                # be children of current node
                node.children[char] = new_node
                node = new_node
        node.is_end_of_world = True

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.is_end_of_world:
            return True
        else:
            return False
