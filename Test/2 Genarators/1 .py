def get_values():
    yield "123"
    yield "gg"
    yield 456


values = get_values()

for i in values:
    print(i)
