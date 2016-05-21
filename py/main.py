#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
基于用户的推荐
基于物品的推荐
数据来源：http://grouplens.org/datasets/movielens/
参考资料：集体智慧编程
'''

import math
import re

def read_item(file):
    '''
    读取u.item文件
    u.item 数据格式
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
    '''
    movie_items = dict()
    with open(file, 'r') as f:
        for item in f:
            movie_item = dict()
            tmp = item.rstrip('\n').split('|')
            movie_item['title'] = tmp[1]
            movie_item['release_date'] = tmp[2]
            movie_item['video_release_date'] = tmp[3]
            movie_item['IMDb_URL'] = tmp[4]
            movie_item['unknown'] = tmp[5]
            movie_item['Action'] = tmp[6]
            movie_item['Adventure'] = tmp[7]
            movie_item['Animation'] = tmp[8]
            movie_item["Children's"] = tmp[9]
            movie_item['Comedy'] = tmp[10]
            movie_item['Crime'] = tmp[11]
            movie_item['Documentary'] = tmp[12]
            movie_item['Drama'] = tmp[13]
            movie_item['Fantasy'] = tmp[14]
            movie_item['Film-Noir'] = tmp[15]
            movie_item['Horror'] = tmp[16]
            movie_item['Musical'] = tmp[17]
            movie_item['Mystery'] = tmp[18]
            movie_item['Romance'] = tmp[19]
            movie_item['Sci-Fi'] = tmp[20]
            movie_item['Thriller'] = tmp[21]
            movie_item['War'] = tmp[22]
            movie_item['Western'] = tmp[23]
            movie_items[movie_item['id']] = movie_item
    return movie_items

def read_data(file):
    ''' 
    读取u.data文件
    u.data 数据格式
              user id | item id | rating | timestamp
    返回字典：
    { user id: { item id : rating ... }
    '''
    critics = dict()
    item = dict()
    with open(file, 'r') as f:
        for line in f:
            tmp = line.split()
            try:
                critics[tmp[0]][tmp[1]] = tmp[2]
            except:
                critics[tmp[0]] = {tmp[1]: tmp[2]}
    return critics

def euclidean_distance(prefs, person1, person2): 
    ''' 
    欧几里德距离
	返回一个有关 person1 与 person2 的基于距离的相似度评价
    '''
    si = dict()
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0 # 两者没有共同之处，则返回 0
    distance = sum([pow( \
            int(prefs[person1][item]) - int(prefs[person2][item]), 2) \
            for item in si.keys()])
    return 1/(1+math.sqrt(distance))

def calculateSimilarItems(prefs, n=10):
    '''
    计算物品相关度
    返回字典
    '''
    result = dict()
    itemPrefs = transformPrefs(prefs)
    c = 0
    fpr item in itemPrefs:
        c += 1
        score = topMatches(itemPrefs, item, n=n, similarity=euclidean_distance)
        result[item] = scores
    return result

def getRecommendedUsers(prefs, person, similarity=euclidean_distance):
    '''
    基于用户推荐物品
    '''
    totals = dict()
    simSums = dict()
    for other in prefs:
        if other == person:
            continue # 去掉本身
        sim = similarity(prefs, person, other)
        if sim <= 0:
            continue # 忽略评价值未0或小于0的情况
        for item in prefs[other]:
            if (item not in prefs[person]) or  (prefs[person][item] == 0):
                # 相似度评价值
                totals.setdefault(item, 0)
                totals[item] += int(prefs[other][item])*sim
                # 相似度之和
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # 建立归一化列表
    rankings = [(total/simSums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = dict()
    totalSim = dict()
    for item, rating in userRatings.items():
        # 遍历循环与当前物品相近的物品
        if item2 in userRatings:
            continue # 若用户对当前物品做过评价，忽略
        scores.setdefault(item2, 0)
        scores[item2] += similarity * rating
        totalSim.setdefault(item2, 0)
        totalSim[item2] += similarity

    rankings = [(score/totalSim[item], item) for item, score in scores.items()]

    rankings.sort()
    rankings.reverse()
    return rankings


if __name__ == "__main__":
    items = read_item('u.item')
    while True:
        prefs = read_data("u.data")
        person = input("input the id.\n")
        if re.match(r"[0-9]+", person):
            rankings = getRecommendedUsers(prefs, person)
            for i in range(20):
                print("id:{} title:{}".format(rankings[i][1], items[rankings[i][1]]['title']))
        else:
            break
