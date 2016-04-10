title: 一个简单的 Python 爬虫
date: 2016-04-10

&emsp;&emsp;由于我经常逛微博，看到某些博主的图片都很好看（你懂的），就想干脆下载到本地，于是萌生了搞个爬虫的想法。之前听说 Python 网络爬虫，听起来高大上，在实践了后感觉也不是什么难事，现在来看自己实现的爬虫都很简单，以后要实现更复杂的爬虫的话，看了这篇博客和代码，能让自己也能快速的捡起来，进行二次开发。
&emsp;&emsp;除了需要 Python 环境外，还需要安装 requests、BeautifulSoup4等。

    pip install requests BeautifulSoup4

&emsp;&emsp;好了，准备工作基本OK。这个爬虫是从新浪微博上爬取某个博主的所有图片，在观察了新浪微博里图片URL的规律后，发现链接主要有3部分构成，如下。img-key 部分我估计是存取图片的唯一ID值，part2 取不同的值，会得到不同尺寸的图片，最大尺寸时，part2取值 ‘mw690’，有了这个规律就好办了，将页面所有图片满足3段式的链接中间那部分替换成mw690，再下载图片即可。


    http://ww2.sinaimg.cn/part2/img-key.jpg

&emsp;&emsp;另外，由于使用的是 *weibo.cn* 域名，从浏览器里得到是一张图片和一个**更多**作为链接，点了链接才看得到所有图片，所以爬每个页面有个二次请求，将更多的图片下载下来。为了避免重复下载导致图片难以维护，保存图片时，将图片内容做32位哈希值后作为图片的名字，再次运行爬虫时会检查该图片名字，避免重复下载。

&emsp;&emsp;下面是下载一个页面里所有图片的函数代码。


    def download_one_page(soup, user_id):
        img_urls = soup.find_all('img')
        for img_tag in img_urls:
            img_url = img_tag['src']
            if not img_url.endswith('.jpg'):
                continue

            # remove http:// in head
            img_url = img_url[7:]
            url_subs = img_url.split("/")
            if len(url_subs) != 3:
                continue
            url_subs[1] = 'mw690'
            final_url = 'http://' + '/'.join(url_subs)

            image_src = requests.get(final_url, cookies = cookie)
            # use hash value as the image name to avoid duplicate downloading
            name = get_img_name(image_src.content)
            if name not in exists:
                with open('./downloads/{}/{}.jpg'.format(user_id, name), 'wb') as jpg:
                    jpg.write(image_src.content)
                    exists.append(name)
                    print('downloading...')
            print('one page downloaded.')


&emsp;&emsp;完整的代码示例[点这里](https://github.com/hsqs/spiders/blob/master/weibo/weibo_miner.py)。

&emsp;&emsp;顺便，贴一个 Python 爬虫常用技巧链接，以后或许可以用到，[点这里](http://my.oschina.net/jhao104/blog/647308?fromerr=KzH2VGaK)。




