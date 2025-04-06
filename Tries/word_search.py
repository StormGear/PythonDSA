# add and search words in a trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                char = word[i]
                
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                
            return curr.is_word

        return dfs(0, self.root)
        
        
if __name__ == "__main__":
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print(word_dict.search("pad"))
    print(word_dict.search("bad"))
    print(word_dict.search(".ad"))
    print(word_dict.search("b.."))
    
    
