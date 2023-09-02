class Data:


    def __init__(self, expression):
        self.expression = expression
        self.stack = []

    def is_balanced(self):

        #  Setting uo the dictionaries to keep the objects inorder to iterate each 
        data_structure = {')' : '(', '}':'{', '[' : ']', }

        for i in self.expression:
            #  if the type is an opening bracket append it
            if i in data_structure.values():
                self.stack.append(i)
            #  if the type is a closing structure
            elif i in data_structure.keys():

                if not self.stack or self.stack.pop() != data_structure[i]:
                    return False
        return not self.stack
    






    
    


