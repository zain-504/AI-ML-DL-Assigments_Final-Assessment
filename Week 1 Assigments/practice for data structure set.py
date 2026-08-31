mobileset = {"Iphone", 70000, 12.2, True}
print(mobileset)
print(type(mobileset))

for mo in mobileset:
    print(mo)

mobileset.add("USA")
print(mobileset)
mobileset.discard("USA")
print(mobileset)

