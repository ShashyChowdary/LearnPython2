def makeArrayConsecutive2(statues):
    return len([i for i in range(min(statues), max(statues)+1) if i not in statues])
print(makeArrayConsecutive2([2,4,7,9]))


