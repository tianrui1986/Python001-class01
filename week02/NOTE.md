学习笔记

1、异常三部分：Traceback函数报错、异常开始发生文件的位置到最终真正报异常的文件与位置、报的什么类型的异常
2、异常分为：系统定义好的6类异常与自定义异常（继承自Exception）
3、使用pretty_errors捕获的异常可以更加清晰
4、使用with open(filename, mode='w', endcoding='utf-8') as f来读写文件，不用写异常捕获，会自动处理

# 数据库连接，连接不同的数据库使用的模块不同
5、使用pymysql连接数据库，连接的步骤:创建连接connect-创建游标cur-使用cur进行增删改查-关闭cur-关闭connect

6、模拟浏览器去请求加request-header参数，包括：user-agent(浏览器)、referer(跳转来源)、Host(网站域名)
7、模拟登陆，需要用到Cookie，使用request.Session来保存cookie信息
8、使用webdirve来模拟点击页面，包括javascript进行加密的链接