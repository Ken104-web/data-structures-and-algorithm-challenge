class Data:
    def __init__(self, expression):
        self.expression = expression
        self.stack = []

    def is_balanced(self):
        data_structure = {')': '(', '}': '{', ']': '['}

        for i in self.expression:
            if i in data_structure.values():
                self.stack.append(i)
            elif i in data_structure.keys():
                if not self.stack or self.stack.pop() != data_structure[i]:
                    return False
        return not self.stack

    def remove_duplicates(self):
        my_list = []
        seen_elements = set()

        for i in self.expression:
            if i not in seen_elements:
                my_list.append(i)
                seen_elements.add(i)

        return my_list


