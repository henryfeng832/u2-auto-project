### adb常用命令
```shell
# 检查设备
$ adb devices
# 终止服务
$ adb kill-server
# wifi连接设备
$ adb connect youip:5555
# 权限提权
$ adb root
# adb shell模式
$ adb shell [content]
# 设置adb服务端口为5555， 打开adb网络调试功能
HWAQM-H:/ $ setprop service.adb.tcp.port 5555
```
### 参考文章
- [uiautomator2 官方地址](https://github.com/openatx/uiautomator2)
- [adbutils 官方地址](https://github.com/openatx/adbutils)
- [weditor 官方地址](https://github.com/alibaba/web-editor/blob/master/README_ZH.md)
- [appium-server-gui调试器](https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)
- [adb链接时报错误10061解决方法_loveyou19_的博客](https://www.myypi.com/news/%C2%B710061.html)
