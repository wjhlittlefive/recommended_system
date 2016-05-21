## 什么是协同过滤

协同过滤一般是在海量的用户中发掘出一小部分和你品位比较类似的，在协同过滤中，这些用户成为邻居，然后根据他们喜欢的其他东西组织成一个排序的目录作为推荐给你。

核心问题：

* 如何确定一个用户是不是和你有相似的品位？
* 如何将邻居们的喜好组织成一个排序的目录？

## 协同过滤的核心

* 收集用户偏好
* 找到相似的用户或物品
* 计算推荐

## 收集用户偏好

pass

## 找到相似的用户或物品

根据用户喜好计算相似用户和物品，然后基于相似用户或物品进行推荐。评价标准：相似度。

#### 相似度的计算

相似度的计算是基于向量的。计算两个向量的距离，距离越近相似度越大。

<<<<<<< HEAD
相似度：

* 将一个用户对所有物品的偏好作为一个向量
* 所有用户对某个物品的偏好

计算方法：

* 欧几里德距离
* 皮尔逊相关系数
* Cosine 相似度
* Tanimoto 系数

#### 相似邻居的计算

固定数量的邻居：

* K-neighborhoods
* Fix-size neighborhoods
=======
* [欧几里得距离](http://baike.baidu.com/link?url=olt1___-dlFEOpdRbGWYtWHxmEtnZ7TsAMNSY1u_NxpQSVruAVAl8dZ2stwWyJ_qLX48CES7ChMxX9b3If7Sk3Xu5g6F04hBoXPb10BLIcP8bJcABt2cEivD4YNJDh3JZlggo3CtU-QtWYqdbfNWq66BSoeW4hpGAHO_WosZG4U2mmcmlaVhAb2u-ZTiGfDZKYWLJ184jDxhwWnAzy7x9K)

* [皮尔逊相关系数](http://baike.baidu.com/link?url=xnMeqHNBQfd4_zDJKy6CwaUlMfb7txvA3EbS99QlYvQGL1EmmqcW6Edtx1qsP3JDXsxnVyr1X3hOG-IUdHhBh_)
>>>>>>> refs/remotes/origin/master

基于相似度门槛的邻居

* Threshold-based neightborhoods

## 计算推荐

#### 基于用户的CF

基于用户对物品的偏好找到相邻邻居用户，然后将相邻用户喜欢的推荐给当前用户。

# 参考资料

[探索推荐引擎内部的秘密，第 2 部分: 深入推荐引擎相关算法 - 协同过滤](https://www.ibm.com/developerworks/cn/web/1103_zhaoct_recommstudy2/)  
[推荐算法]基于用户的协同过滤算法](http://blog.csdn.net/ygrx/article/details/15501679)
## socket5 proxy

ip: 10.170.4.60 port:1080
