学习笔记
在A环境生成requirements.txt文件
pip freeze > requirements.txt
在B环境克隆A环境：
pip install -r requirements.txt

1、requests在获取网页内容时，省去打开、编码的步骤，而且采用模拟浏览器的方式抓取，比urllib更加方便快捷
2、BeautifulSoup用于对抓取到的网页进行过滤，过滤根据网页的标签来进行，或者获取标签的class、sytle属性，或者获取标签之间的值text；
html.parser将网页内容解析出来，使用字典的数据结构进行存储，如：{'div': [...]}
3、XPath在抓取网页信息时，要转换成标准的xml文件格式，再使用类似于正则表达式去匹配需要的内容，模拟点击翻页需要自己实现
4、模拟浏览器进行数据请求，关键信息是：cookie和user-agent；cookie是登录后加密的信息，user-agent是告诉服务器端是什么浏览器发起的请求
5、爬虫框架scrapy，使用pip install scrapy进行安装，安装完成，使用scrapy startproject projectname创建爬虫工程，创建完成之后，进入工程文件夹（cd两次），使用scrapy genspider example example.com生成spider，其中example为爬虫名称（运行时需要），example.com为需要爬取的网页域名
6、使用scrapy，只需关注，需要爬取的内容（定义爬取的变量）、爬取页面的网址以及获取的数据存储
7、使用pandas模块，可以向csv、excel、sql等等写入数据
8、使用scrapy crawl example，其中example为当时生成的爬虫名字