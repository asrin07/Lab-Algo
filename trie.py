class Trie_node:
    def __init__(self, char):
        #Pass as argument to make a node
        self.char = char
        #Initialize dictionary
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Trie_node("")
        self.arr = []

    def insert(self, word):
        print("Inserting...", word)
        for char in word:
            self.arr.append(char)
        for y in range(len(self.arr)):

            #Cut the word one by one
            x = slice(y, len(self.arr))
            word = ''.join(map(str, self.arr[x]))
            
            #start from root again
            node = self.root

            print(word)
            for char in word:
                if char in node.children:
                    node = node.children[char] #be the child of current node
                else:
                    new_node = Trie_node(char) #make new node
                    node.children[char] = new_node #be children of current node
                    node = new_node

    def search(self, word):
        print("Searching...", word)
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                print("Not Found")
                return False
        print("Found")
        return True


t = Trie()
t.insert("algorithmisfun")
t.search("thm")
