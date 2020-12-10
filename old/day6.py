class Planet:
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.children = children