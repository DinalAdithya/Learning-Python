from itertools import groupby

'''def smaler_than_3(x): #coment this becouse we use lambda below
    return x < 3'''


a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3) # function using lamda

for key, value in group_obj:
    print(key, list(value)) # according to the key list the value


# second example
ppls = [
    {"name": "tim", "age": 25},
    {"name": "dan", "age": 25},
    {"name": "lisa", "age": 27},
    {"name": "Claire", "age": 28}
]

gp_by = groupby(ppls, key=lambda x: x["age"])

print("\ngroup the same age ppl together")

for key, value in gp_by:
    print(key, list(value))
