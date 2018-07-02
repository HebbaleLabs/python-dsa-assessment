from random import randint


def genRandom():
    al = []
    for x in range(10000):
        a = randint(0, 100*1000000)
        if a not in al:
            al.append(a)
    return al


def newRandom():
    al = []
    for x in range(10000):
        a = randint(0, 100*1000000)
        if a not in al:
            al.append(a)
    return al

if __name__ == '__main__':
    ret_val = newRandom()
    print(len(ret_val))
