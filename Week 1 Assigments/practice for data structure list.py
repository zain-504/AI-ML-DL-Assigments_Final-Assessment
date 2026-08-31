mobilelist = ["Iphone", 70000, 12, True]
print(mobilelist)
print(type(mobilelist))

for mo in mobilelist:
    print(mo)

mobilelist.append("USA")
print(mobilelist)
mobilelist.insert(2, 6.6)
print(mobilelist)
print(mobilelist[1])
print(type(mobilelist[2]))

mobilelist.remove(70000)
print(mobilelist)

mobilelist.pop(0)
print(mobilelist)

                                                                                                                                    