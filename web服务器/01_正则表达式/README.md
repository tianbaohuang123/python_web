# web服务器
正则表达式

> import re
> re.match(正则表达式, 需要处理的字符串)

# 匹配单个字符：
* .: 匹配任意1个字符（除了\n）   ---  包含\n: re.match(正则表达式, 需要处理的字符串, re.S)
* []: 匹配[]中列举的字符
* \d: 匹配数字，即0-9
* \D: 匹配非数字，即不是数字
* \s: 匹配空白，即 空格，tab建
* \S: 匹配非空白
* \w: 匹配单词字符，即a-z,A-Z,0-9,_,中文...
* \W: 匹配非单词字符

# 匹配多个字符：
* *: 匹配前一个字符出现0次或者无限次，即可有可无
* +: 匹配前一个字符出现1次或者无限次，即至少有1次
* ?: 匹配前一个字符出现1次或者0次，即 要么有1次，要么没有
* {m}: 匹配前一个字符出现m次
* {m,n}: 匹配前一个字符出现从m到n次

# 匹配开头结尾：
* ^: 匹配字符串开头
* $: 匹配字符串结尾

# 匹配分组：
* |: 匹配左右任意一个表达式
* (ab): 将括号中字符作为一个分组
* \num: 引用分组num匹配到的字符串
* (?p<name>): 分组起别名
* (?P=name): 引用别名为name分组匹配到的字符串

# re模块的高级用法：

* (1)需求：匹配出文章阅读的次数
'''
ret = re.search(r"\d+", "阅读次数为 9999")
re.group()
'''

* (2)需求：统计出python、c、c++相应文章阅读的次数
'''
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret) #直接返回数据不需要group
'''

* (3)sub将匹配到的数据进行替换
* * 需求：将匹配到的阅读次数加1
'''
ret = re.sub(r"\d+", '998', "python = 997")
print(ret)
'''
* 可传入函数
'''
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret = re.sub(r"\d+", add, "python = 99"
print(ret)
'''

# split根据匹配进行切割字符串，并返回一个列表
* * 需求：切割字符串"info:xiaoZhang 18 hangzhou"
'''
ret = re.split(r":| ", "info:xiaoZhang 18 hangzhou")
print(ret)
'''

