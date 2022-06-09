class Function:
    def __init__(self, name, offset, length, params):
        self.name = name
        if type(offset) == str:
            self.offset = int(offset, 16)
        else:
            self.offset = offset
        if type(length) == str:
            self.length = int(length)
        else:
            self.length = length
        self.params = {}
        for key in params.keys():
            self.params[key] = params[key]

    def rename(self, new_name):
        self.name = new_name

    def add_arg(self, reg, arg):
        self.params[reg] = arg

   # def add_args(self, args):
    #    for arg in args:
     #       self.add_arg(arg)

    def to_string(self):
        off = hex(self.offset)
        #print(off)
        tmp = f"Offset: {off}  Length: {self.length}  Name: {self.name}  Parameters known to the program: {self.params}"
        return tmp