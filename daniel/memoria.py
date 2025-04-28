import copy

# Investigar un poco mas de asignacion por referencia.
a = [1, 2, 3]

b = copy.copy(a)

# print(id(a))
# print(id(b))

b.append(20)

# print('a', a)
# print('b', b)

# print(a is b)
c = [
    [1, 2],
    [3, 4]
]

b7 = copy.copy(c)

print(b7)

b8 = copy.deepcopy(c)

print(b8)
