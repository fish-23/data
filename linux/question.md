### 1,用户切换
    （1）输入su 用户名 回车 root用户需要设置密码。普通用户“$”，root用户“#”
### 2，yum 安装软件时错误 Errno 14 Couldn't resolve host
    （1）需要开启网络服务   vi 进入 /etc/sysconfig/network-scripts/ifcfg-ens33  将onboot 改成yes
    （2）更改后重启网络服务 service network restart

### 3，用vnc连接centos7
    （1）下载后安装：https://www.realvnc.com/en/connect/download/viewer/
     （2）VMware开启vnc服务：虚拟机---设置---选项---vnc连接

### 4，ifconfig 报错 ifconfig command not found
    （1）确保sbin文件夹存在，并且没有ifconfig     # cd /sbin
    （2）安装net-tool插件    # sudo yum install net-tools
         备注：如果安装时报错连接地址无法连接，重启下网络服务service network restart
    （3）参考：https://blog.csdn.net/Hanani_Jia/article/details/78732033

### 5，Xshell 连接 VMware里安装的centos7
    （1）在centos 7 里面 输入 ifconfig -a  查看ip地址inet后面的地址就是
    （2）用xshell直接输入地址，22端口，用户名，密码进行登录
