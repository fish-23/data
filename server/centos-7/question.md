### 1，yum源配置
      解答：
        (1) 备份之前的源文件
	    mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
	(2) 下载163的源文件
	    wget -P /etc/yum.repos.d http://mirrors.163.com/.help/CentOS7-Base-163.repo
	(3) 清除yum的本地缓存
	    yum clean all
	(4) 缓存服务器上的安装包
            yum makecache
### 2，yum安装时出现：Cannot retrieve metalink for repository: epel. Please verify its path and try again
      解答：
        把/etc/yum.repos.d/epel.repo，文件第3行注释去掉，把第四行注释掉。
        baseurl=http://download.fedoraproject.org/pub/epel/6/$basearch
        #mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=$basearch
### 3，centos7 yum安装pip
      解答：
        (1) sudo yum install epel-release 
        (2) sudo yum install python-pip 
        (3) pip install --upgrade pip 更新pip
### 4，centos7 yum安装pip3
      解答：
        (1) 安装 epel-release扩展yum源(存在就不需要安装了)
            yum install -y epel-release
            yum clean all
            yum makecache
        (2) 安装setuptools
            yum install -y python34-setuptools
        (3) 安装pip3
            easy_install-3.4 pip
### 5，查看版本号
      解答：
        (1) cat /etc/redhat-release
### 6，pip查看安装的软件及详情
      解答：
        (1) 查看安装的软件列表
            pip list
        (2) 查看某一个软件的详情(例如：wxpy)
            pip  show wxpy
