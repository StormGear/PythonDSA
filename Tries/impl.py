class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True
        
        # print children in the trie
        curr = self.root.children[word[0]]    
        print(self.root.children)
        for i in range(1, len(word)):
            print(curr.children)
            curr = curr.children[word[i]]
        print("Successfully inserted", word)

        
    
    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            node = current.children.get(char)
            if not node:
                return False
            current = current.children[char]
        return current.end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Example usage:
if __name__ == "__main__":
    # trie = Trie()
    # trie.insert("apple")
    # trie.insert("app")
    # print(trie.search("apple"))    # True
    # print(trie.search("app"))      # False
    # print(trie.starts_with("app")) # True
    phones = {
        'a':1,
        'b':2
    }
    