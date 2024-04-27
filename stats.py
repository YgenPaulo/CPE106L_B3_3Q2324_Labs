def median (l):
    if not l:
        return 0
    l.sort()
    length = len(1)
    if length % 2 == 0:
        return (l[(length//2)-1])
    else:
        return (l[length//2])
def mode (l):
    if not l:
        return 0
    dictionary = {}
    for num in l:
        number = dictionary.get(num, None)
        if number == None:
            dictionary[num] = 1
        else:
            dictionary[num] = number + 1
    theMax = max(dictionary.values())
    for key in dictionary:
        if dictionary[key] == theMax:
            return (key)
def mean (l):
    if not l:
        return 0
    return (sum(1)/len(1))

        