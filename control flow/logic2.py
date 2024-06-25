first = "Keith"
last = ""
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")

last = "Thompson"
if first and last:
    print(f"Full name: {first} {last}")


g = 0 and 1
print(g)

h = 1 and 2
print(h)