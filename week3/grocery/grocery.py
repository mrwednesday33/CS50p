import sys

items = {}

try:
    while True:
        item = input().strip().lower()
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
except EOFError:
    pass

for item, count in sorted(items.items()):
    print(f"{count} {item.upper()}")
