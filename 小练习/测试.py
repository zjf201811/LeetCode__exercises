
def lcm(x, y):
    greater = max(x, y)
    while True:
        print(greater)
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
print(lcm(39999,40000))