"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    return frequencies

test1 = frequencies(['a', 'a', 'b', 'b', 'b', 'c'])
print(test1)

test2 = frequencies([100, 'Hello', '100', '100', 100])
print(test2)






