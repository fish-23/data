### 1，ORA-12541：TNS：无监听程序
     解答：开始 -- 控制面板 -- 大图标 -- 管理工具 -- 服务(启动oracle的服务)
           如果oracleconsoleorcl服务不能启动，关闭网络，关闭所有Oracle服务，重启电脑即可
           参考地址  https://jingyan.baidu.com/article/5d368d1ed09ef13f60c05737.html
### 2，ora-12516：TNS监听程序找不到符合协议堆栈要求的可用处理程序
     解答：数据库线程数不够，alter system set processes=500 scope=spfile   增加完线程需要重启
### 3，ora-01017 登录失败
     解答：ora配置的问题，windows系统的配置有两方面，一个是系统环境配置，一个是注册表的配置
          看看注册表填写的登录信息是否有错误，特别注意大小写
### 4，ora-12154 客户端报错
     解答：查看环境配置，path的配置是否有问题

