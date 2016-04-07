import math


class ShapeError(Exception):
    pass


def shape(vector):
    return (len(vector),)


def vector_add(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        raise ShapeError
    return [x+y for x,y in zip(vector_1,vector_2)]


def vector_sub(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        raise ShapeError
    return [x-y for x,y in zip(vector_1,vector_2)]

def vector_sum(*arg):
    if len(set([shape(i) for i in arg]))> 1:
        raise ShapeError
    return [sum(i) for i in zip(*arg)]

def dot(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeError
    return sum(p*q for p,q in zip(vector1, vector2))

def vector_multiply(vector_1, scalar):
    return [x*scalar for x in vector_1]


def vector_mean(*args):
    return [sum(x)/len(x) for x in zip(*args)]


def magnitude(vector_1):
    return math.sqrt(sum([i*i for i in vector_1]))
