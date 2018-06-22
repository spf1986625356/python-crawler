#coding=utf-8
# import urllib
#
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# html = getHtml("http://tieba.baidu.com/p/2738151262")
#
# print html






# urllib.urlopen()方法用于打开一个URL地址。
# 　　read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。执行程序就会把整个网页打印输出。

#
# #coding=utf-8
# # 引入依赖
# import re
# import urllib
#
# # 获取页面
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# #　　我们又创建了getImg()函数，用于在获取的整个页面中筛选需要的图片连接。re模块主要包含了正则表达式：
# # 　　re.compile() 可以把正则表达式编译成一个正则表达式对象.
# # 　　re.findall() 方法读取html 中包含 imgre（正则表达式）的数据。
# # 　　 运行脚本将得到整个页面中包含图片的URL地址。
#
#
# # 对页面进行赛选
# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html)
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl, '%s.jpg' % x)
#         x += 1
#         return imglist
#
#     # 　这里的核心是用到了urllib.urlretrieve()方法，直接将远程数据下载到本地。
# # 　　通过一个for循环对获取的图片连接进行遍历，为了使图片的文件名看上去更规范，对其进行重命名，命名规则通过x变量加1。保存的位置默认为程序的存放目录。
#
# html = getHtml("http://tieba.baidu.com/p/2460150866")
# print getImg(html)


