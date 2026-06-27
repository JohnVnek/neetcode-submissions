class PrefixTree:

    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        if not word:
            self.is_word = True
            return
        next_node = None
        char = word[0]
        if char in self.children:
            next_node = self.children[char]
        else:
            next_node = PrefixTree()
            self.children[char] = next_node
        next_node.insert(word=word[1:])
        

    def search(self, word: str) -> bool:
        if not word:
            return self.is_word
        char = word[0]

        if char in self.children:
            return self.children[char].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        char = prefix[0]

        if char in self.children:
            return self.children[char].startsWith(prefix[1:])
        return False
        
        