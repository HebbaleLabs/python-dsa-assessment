from random import randint


def gen_random():
    al = []
    for x in range(10000):
        a = randint(0, 100*1000000)
        if a not in al:
            al.append(a)
    return al


def new_random():
    al = []
    for x in range(10000):
        a = randint(0, 100*1000000)
        if a not in al:
            al.append(a)
    return al


if __name__ == '__main__':
    ret_val = new_random()
    print(len(ret_val))
