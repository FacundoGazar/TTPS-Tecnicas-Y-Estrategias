from collections import deque

class Node:
    def __init__(self):
        self.outputs = set()
        self.children = {}
        self.failure_link = None

    def has_child(self, key):
        return key in self.children
    
    def get_child(self, key):
        return self.children.get(key)

    def set_child(self, key, node):
        self.children[key] = node

    def add_output(self, output):
        self.outputs.add(output)
    
    def copy_outputs(self, node):
        for o in node.outputs:
            self.outputs.add(o)

class AhoCorasick:
    def __init__(self, patterns):
        self.root = Node()

        for pattern in patterns:
            curr_node = self.root
            for key in pattern:
                if not curr_node.has_child(key):
                    curr_node.set_child(key, Node())
                curr_node = curr_node.get_child(key)
            curr_node.add_output(pattern)

        self.root.failure_link = self.root
        queue = deque()

        for child in self.root.children.values():
            child.failure_link = self.root
            queue.append(child)
        
        while queue:
            curr_node = queue.popleft()

            for key, child in curr_node.children.items():
                queue.append(child)

                n = curr_node.failure_link
                while not n.has_child(key) and n != self.root:
                    n = n.failure_link
                
                if n.has_child(key):
                    child.failure_link = n.get_child(key)
                else:
                    child.failure_link = self.root
                
                child.copy_outputs(child.failure_link)
    
    def search(self, text):
        found = []
        state = self.root
        i = 0

        while i < len(text):
            c = text[i]

            if state.has_child(c):
                state = state.get_child(c)
                i += 1
                
                if state.outputs:
                    for val in state.outputs:
                        found.append({
                            "pos": i - len(val),
                            "val": val
                        })
            
            elif state == self.root:
                i += 1
            else:
                state = state.failure_link

        return found