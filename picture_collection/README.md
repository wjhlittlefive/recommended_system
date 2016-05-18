# 介绍

这里是图片搜集、贴标签部分。

思路：

* 爬虫采集图片
* 使用[neuraltalk2](https://github.com/karpathy/neuraltalk2)自动生成描述图片的文字
* 关键词提取

具体步骤：

1. `requests`单线程抓取图片链接，存至数据库
2. 多进程贴标签
