import operator

def zero(args=None):
    if args:
        return args[0](0,args[1])
    else:
        return 0


def one(args=None):
    if args:
        return args[0](1,args[1])
    else:
        return 1


def two(args=None):
    if args:
        return args[0](2,args[1])
    else:
        return 2


def three(args=None):
    if args:
        return args[0](3,args[1])
    else:
        return 3


def four(args=None):
    if args:
        return args[0](4,args[1])
    else:
        return 4


def five(args=None):
    if args:
        return args[0](5,args[1])
    else:
        return 5


def six(args=None):
    if args:
        return args[0](6,args[1])
    else:
        return 6


def seven(args=None):
    if args:
        return args[0](7,args[1])
    else:
        return 7


def eight(args=None):
    if args:
        return args[0](8,args[1])
    else:
        return 8


def nine(args=None):
    if args:
        return args[0](9,args[1])
    else:
        return 9


def plus(number):
    return (operator.add, number)


def minus(number):
    return (operator.sub, number)


def times(number):
    return (operator.mul, number)


def divided_by(number):
    return (operator.floordiv, number)
