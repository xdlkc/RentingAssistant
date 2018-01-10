## RentingAssistant
### 项目介绍
本项目爬取链家网等租房网站的房屋信息存储到数据库中,通过前端页面可视化展示数据,主要针对应届毕业生的工作地的房屋选择的难题,供毕业生参考
### 技术栈
- 虚拟化:Docker
- 爬虫:Python的Scrapy框架
- 数据库:PostgreSQL
- 后端服务器:Java的SSM框架(Spring Boot + Spring MVC + Mybatis)
- 前端页面:HTML+CSS+JavaScript+Bootstrap
### 目前进度
- 爬虫: 完成(58北京，链家北京)
- 存储数据: 完成
- 服务器搭建: 完成
- 前端页面展示: 完成
- docker容器配置:完成

### 模块说明  

#### 爬虫模块

- 58zf：58网的租房信息爬虫
- ljzf：链家网的租房信息爬虫
- zrzf：自如网的租房信息爬虫
- city：城市信息的爬虫


#### 容器模块

在DockerConf文件夹下运行 `docker-compose up`命令即可启动容器，要求数据库目录命名为`pgd`与yaml模板放在同一目录

### 运行说明



构建爬虫镜像: docker build -t lkc_spider . -f DockerConc/spider.dockerfile
构建数据库镜像:docker build -t lkc_db . -f DockerConc/db.dockerfile
构建服务器镜像:docker build -t lkc_web . -f DockerConc/web.dockerfile

