title: 在 OS X 上使用 virtualenv
date: 2016-03-27



### 1，理解virtualenv
&emsp;&emsp;virtualenv从字面意思来理解的话，就是虚拟环境的意思，这个第一印象容易对我们产生误导，其实并不是虚拟环境，以我的理解是一个**独立**环境。什么意思呢？好比一台电脑上装好Python以后，可以把安装的Python拷贝到另一个目录(官方:其实并没有真正安装多个 Python 副本，但是它确实提供了一种巧妙的方式来让各项目环境保持独立)，这样两个Python环境相互独立，互不影响，那有了多个Python环境，在什么时候启用谁禁用谁呢？virtualenv这个时候就派上用场了。官方对virtualenv的解释：[virtualenv is a tool to create isolated Python environments](https://virtualenv.pypa.io/).



### 2，安装virtualenv
&emsp;&emsp;安装就太简单了，使用pip安装即可：


    pip install virtualenv


&emsp;&emsp;如果有权限问题，前面加一个sudo


    sudo pip install virtualenv



### 3，使用virtualenv

&emsp;&emsp;首先找到一个合适的空文件夹，在终端里输入如下命令，创建一个虚拟环境（Python已经安装到电脑上）：

    virtualenv [-p python3] dir-name


&emsp;&emsp;如果电脑上安装了多个版本的Python，默认会使用OS X自带的2.7版本，如果想创建3.0以上的版本的话，指定版本参数即可。输入完成回车，可以到Finder里查看目录dir-name，里面有bin、include、lib三个目录。最后一步，继续在终端里输入如下命令，激活这个刚刚创建的环境：


    source dir-name/bin/activate


&emsp;&emsp;这个时候，当前Python环境就激活了，终端也会有相应的变化，在最前面会出现当前环境的名字：


    (dir-name)your-computer-name $:


&emsp;&emsp;hah，这个时候就可以使用了，比如在这个而环境里开发Flask应用，执行：

    pip install Flask


&emsp;&emsp;此时，Flask会安装在dir-name里，而不会安装在其他环境，这样就达到了isolated的效果。如果不再使用当前环境，使用如下命令即可退出：


    deactivate


### 4，删除virtualenv

    rmvirtualenv env-name
