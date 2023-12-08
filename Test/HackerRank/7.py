if __name__ == '__main__':
    _list = []
    N = int(input())

    for i in range(N):
        command = input().split()
        command_type = command[0]

        commands = {
            "insert": lambda: _list.insert(int(command[1]), int(command[2])),
            "print": lambda: print(_list),
            "remove": lambda: _list.remove(int(command[1])),
            "append": lambda: _list.append(int(command[1])),
            "sort": lambda: _list.sort(),
            "pop": lambda: _list.pop(),
            "reverse": lambda: _list.reverse(),

        }

        if command_type in commands:
            commands[command_type]()