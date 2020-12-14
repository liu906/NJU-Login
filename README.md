# NJU-
自动打开校园网认证页面并登录
没有人（我的别的设备）可以把我实验室的服务器挤掉！

配合crontab命令实现每三分钟检测一下网络，如果连不到外网（ping百度失败），就打开浏览器重新登录。

DISPLAY=:0

*/3 * * * * python3 /home/username/login.py
