class computer:
    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def calling(self):
        print("This is your ram", self.ram, self.cpu)


call1 = computer('1', 2)
call2 = computer('3', 4)

call1.calling()
call2.calling()