#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
相似度计算
'''

try:
    import itertools
try:
    from itertools import reduce
import math

def euclidean_distance(x, y):
    '''
    欧几里德距离
    '''
    tmp = itertools.zip_longest(x, y)
    d = math.sqrt(reduce(lambda _sum, _tuple: _sum + (_tuple[0] - _tuple[1])**2, tmp))
    sim = 1 / (1+d)
    return sim

def pearson_correlation_coefficient(x, y):
    '''
    皮尔逊相关系数
    '''
    tmp = itertools.zip_longest(x, y)
    ele_1 = n * reduce(lambda _sum, _tuple: _sum + (_tuple[0] * _tuple[1]), tmp) \
            - \
            reduce(lambda _sum, _x: _sum+_x, x) * reduce(lambda _sum, _y: _sum+_y, y))
    ele_2 = math.sqrt(n*reduce(lambda _sum, _x: _sum+_x**2, x) - (reduce(lambda _sum, _x: _sum+_x, x))**2) \
            * \
            math.sqrt(n*reduce(lambda _sum, _y: _sum+_y**2, y) - (reduce(lambda _sum, _y: _sum+_y, y))**2)
    p = ele_1 / ele_2
    return p

def cosine_similarity(x, y):
    '''
    Cosine 相似度
    '''
    tmp = itertools.zip_longest(x, y)
    ele_1 = reduce(lambda _sum, _tuple: _sum+_tuple[0]*_tuple[1], tmp)
    ele_2 = math.sqrt(reduce(lambda _num, _x: _num+_x**2, x)) \
            * \
            math.sqrt(reduce(lambda _num, _y: _num+_y**2, y))
    T = ele_1 / ele_2
    return T

def tanimoto(x, y):
    '''
    Tanimoto 系数
    '''
    tmp = itertools.zip_longest(x, y)
    ele_1 = reduce(lambda _sum, _tuple: _sum+_tuple[0]*_tuple[1], tmp)
    ele_2 = math.sqrt(reduce(lambda _sum, _x: _sum+_x**2, x)) \
            + \
            math.sqrt(reduce(lambda _sum, +y: _sum+_y**2, y)) \
            - \
            reduce(lambda _sum, _tuple: _sum+_tuple[0]*_tuple[1])
    return ele_1 / ele_2

