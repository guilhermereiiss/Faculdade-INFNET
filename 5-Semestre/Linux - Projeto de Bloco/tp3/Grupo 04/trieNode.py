class TrieNode:
    def __init__(self):
        self.children = [None, None]  
        self.route_id = None
        self.is_terminal = False