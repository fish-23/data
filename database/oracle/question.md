### 1，ORA-12541：TNS：无监听程序
     解答：开始 -- 控制面板 -- 大图标 -- 管理工具 -- 服务(启动oracle的服务)
### 2，ora-12516：TNS监听程序找不到符合协议堆栈要求的可用处理程序
     解答：数据库线程数不够，alter system set processes=500 scope=spfile
