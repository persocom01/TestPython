k = ['a', 'b', 'a']
v = [1, 2, 3]
d = {}
for k, v in zip(k, v):
    d.setdefault(k, []).append(v)

print(d)
