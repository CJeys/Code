example = set()
print(dir(example))
help(example.add)

example.add(420)
example.add(False)
example.add(3.12312310)
example.add("Astamamahacka")

print(example)
print(len(example))

example.remove(False)
print(example)

example.add(False)
print(example)

example.discard(520)
print(example)

example.discard(False)
print(example)

example.clear()
print(example)

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])
print(odds.union(evens))
print(evens.union(odds))
print(odds.intersection(evens))
print(evens.intersection(composites))

print(2 in primes)
print(dir(set))