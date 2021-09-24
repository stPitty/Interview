class Stack():
    def __init__(self):
        self.stack = {}

    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True

    def push(self, new_element):
        if self.stack != {}:
            keys_list = list(self.stack.keys())
            keys_list.sort(reverse=True)
            for key in keys_list:
                self.stack[key + 1] = self.stack[key]
                self.stack.pop(key)
        self.stack[1] = new_element

    def pop(self):
        if self.stack == {}:
            return None
        else:
            keys_list = list(self.stack.keys())
            keys_list.sort()
            upper_element = self.stack[min(keys_list)]
            for key in keys_list:
                try:
                    self.stack[key] = self.stack[key + 1]
                except KeyError:
                    self.stack.pop(keys_list[-1])
            return upper_element

    def peek(self):
        return self.stack[1]

    def size(self):
        return len(self.stack)
