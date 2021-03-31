class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):

        for i in range(len(word)):
            curr_root = self.root
            for i in word:
                if i not in curr_root.children:
                    curr_root.children[i] = TrieNode()

                curr_root = curr_root.children[i]
                curr_root.isWord = True
            word = word[1:]

    def search(self, word):
        curr_root = self.root

        for i in word:
            if i not in curr_root.children:
                return False
            else:
                curr_root = curr_root.children[i]

        return curr_root.isWord


trie = Trie()
trie.add_word("char")
trie.add_word("chan")
print(trie.search("cha"))
