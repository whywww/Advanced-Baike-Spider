# BaikeSpider Project

#### 面向百度百科数据采集的网络爬虫

爬取目标：[https://baike.baidu.com/](https://baike.baidu.com/ ) 

##### 采集内容：
1. 词条访问URL地址(itemUrls)
2. 词条名称(itemTitle)
3. 词条简介(itemSummary)
4. 词条基本信息(itemBasicInfo)
5. 词条目录及内容(itemCat)(itemInfo)
6. 词条更新时间(itemUpdateTime)
7. 参考资料(itemReferance)
8. 词条标签等信息(itemTag)

##### 指标：
词条数≥1000000个

##### 技术难点：
全站数据采集中需要构造合适的词条访问地址，可能的网站反爬虫策略

##### 实现方法：

python2.7+scrapy框架+mySQL

##### 配置：
1. 安装beautifulsoup4库: `pip install beautifulsoup4`

2. 安装scrapy库: `pip install scrapy`

3. 安装mySQLdb库: （可能会比较复杂）
    win64请下载：MySQL-python-1.2.3.win-amd64-py2.7.exe 
    win32请下载：MySQL-python-1.2.3.win32-py2.7.exe
    直接安装即可，在安装中可能会碰到找不到路径的问题，一定要在系统环境中配置好python的环境！并且这个是针对python2.7版本的

4. mySQL数据库配置: 新建数据库baidu 以及表items，添加如下属性字段：

  | 名           | 类型           | 主键/外键 |
  | ----------- | ------------ | ----- |
  | itemTitle   | text         |       |
  | itemUrl     | varchar(255) | 主键    |
  | itemSummary | text         |       |

  ```python
  # 数据库配置信息>>settings.py
  MYSQL_HOST = '127.0.0.1'
  MYSQL_DBNAME = 'baidu'         # 数据库名字
  MYSQL_USER = 'dqq'             # 数据库账号
  MYSQL_PASSWD = '123456'         # 数据库密码

  MYSQL_PORT = 3306               # 数据库端口
  ```


文件结构：

----- BaikeSpider.py # 爬虫程序

----- run.py # 运行程序

items.py # 需要存储的字段

middlewares.py # 代理池（反爬虫）

settings.py # 项目配置