titles: 关于这个网站
dates: 2016-03-27


&emsp;&emsp;欢迎来到我的个人小站:-)

&emsp;&emsp;整个网站是在github-pages的基础上搭建的，起初，所有的网页代码都是手工编写（我居然这么干了！），每弄一次简直有砸电脑的冲动，然后就好久没有想写任何东西。搭建流程也是参考了一篇教程[使用Github Pages建独立博客](http://beiyuu.com/github-pages/)。当然，要先到[godaddy.com](https://www.godaddy.com/)注册一个域名，国内的话[万网](https://wanwang.aliyun.com/)也可以，不过万网这货有点烦，刚注册没几天，客服就开始打我电话推销，而且万网注册一般都要备案，有点繁琐。

&emsp;&emsp;后来开始自学Python后，发现Python有很多搭建网站的框架，就开始看[Flask](http://flask.pocoo.org/)，但是开发的网站要服务器才能部署，看了下服务器的价格，不算贵，但是为了搭建个个人网站，买的话有点不划算，这个事情又搁浅了一段时间。

&emsp;&emsp;直到有一天，我想，既然github-pages上可以上传网页，可不可以把Flask也一起上传什么的（haha我也是够了），结果发现这个干是不行滴。但是却发现了[Frozen-Flask](http://pythonhosted.org/Frozen-Flask/)这个么东东，可以将Flask的开发好的网页APP，转换为静态网页，上传到github-pages，voila~整个过程都有解决方案了，而且你只用注册一个域名。

&emsp;&emsp;现在整个网站是 github-pages + Flask + Frozen-Flask + markdown + bootstrap 搭建起来的，可以将编写好的markdown转换为网页形式，目前来看，转换的不是很好，有些纯markdown预览的格式，经过这么一转换，样式并不会完全一致，如果将来有更好的方案，可能就不用这种方式了。

&emsp;&emsp;那可能会问，github免费提供空间有限制吗？把别人提供的功能拿来搭建自己的网站道德吗？其实，官方有这样的说明，github-pages提供不受限制的空间，而且允许你做任何事情，他们也并不会干涉。