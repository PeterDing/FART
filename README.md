# FART 源码注解

为了理解 FART 的工作原理，对 FART 源码加入了注解。

在 `android-src` 目录里是 FART 依赖的 `Android 6.0` 源码，其中也包含了 FART 插入的代码。这些代码在标识 `// fart start\n
// {{{` 和 `// }}}\n // fart end`  的内部。



## Dex Magic Code 缺失

有一些壳会会把 dexfile[:8] 的 magic code 抹去，让内存搜索 dex magic code 的方法失效。同时也会让 FART 脱壳出的 dex 文件失去 magic code。

运行 `fix-dex-magic-code.py /path/to/some.dex` 或 `fix-dex-magic-code.py /path/include_dex/directry` 能将抹去了 magic code 的 dex 文件还原。


# FART

ART 环境下基于主动调用的自动化脱壳方案，基于 Android 6.0 实现，理论上可以移植到任何 ART 系统上，现在已经移植到 Android 8.0，很快就将移植到 Android 10.0。具体原理和实现请移步看雪，系列文章共计 3 篇，对加固和对抗感兴趣的可以看看：

1、拨云见日：安卓 APP 脱壳的本质以及如何快速发现 ART 下的脱壳点 https://bbs.pediy.com/thread-254555.htm

2、FART 正餐前甜点：ART 下几个通用简单高效的 dump 内存中 dex 方法 https://bbs.pediy.com/thread-254028.htm

3、FART：ART 环境下基于主动调用的自动化脱壳方案 https://bbs.pediy.com/thread-252630.htm

此次更新修复函数体文件乱序问题，同时，提升 fart 运行效率问题。提供的压缩包中包含了一个可供测试的 apk 和对应的配置文件 fart。

脱壳流程：

1、安装待脱壳 apk，并到设置中授予 sd 卡读写权限

2、将 fart 配置文件 fart 复制到/data/fart（注意文件权限问题，和换行的问题），其中，fart 配置文件中为要脱壳的 app 包名

3、点击 app 图标，开始进入 fart 脱壳过程

接下来可以对 logcat 中的 tag 为 ActivityThread 的 log 进行过滤，等待出现"fart run over"，此时 fart 主动调用过程结束。脱壳下来的

dex 文件和函数体 bin 文件均在/sdcard/fart/app 包名的目录下

下面截图为 fart 的运行流程和脱壳结果

<p align="center">
  <img width="600" height="80" src="https://github.com/hanbinglengyue/img/blob/master/logcat.JPG">
</p>
 

<p align="center">
  <img width="600" height="400" src="https://github.com/hanbinglengyue/img/blob/master/fartresult.JPG">
</p>

这里将 arm 模拟器、nexus5 镜像合并为一个包，以供下载。

链接：https://pan.baidu.com/s/18QIdXKwp5VCYAL_jxXcwEA
提取码：wyxm

联系邮箱：edunwu@gmail.com 另外建立了个 qq 群方便交流,群内提供学术交流并上传最新相关资料，感兴趣的可以扫描二维码加群。

qq 群二维码

<p align="center">
  <img width="200" height="200" src="https://github.com/hanbinglengyue/img/blob/master/qq.JPG">
</p>

---

添加 frida 版的 fart 的两种不同实现，各有特色。可以实现具体到对某一个类下的所有函数甚至是对某一个函数的 CodeItem 的 dump。需要的可以去体验下其强大的脱壳能力。(注意，测试环境为 pixel Android8.0,frida-server 12.8.0)

<p align="center">
  <img width="600" height="400" src="https://github.com/hanbinglengyue/img/blob/master/frida-fart.png">
</p>
