class node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        print(self.data)

root = node(19)

root.PrintTree()
