title: 一个简单的 Python 爬虫
date: 2016-04-10

&emsp;&emsp;由于我经常逛微博，看到某些博主的图片都很好看（你懂的），就想干脆下载到本地，于是萌生了搞个爬虫的想法。之前听说 Python 网络爬虫，听起来高大上，在实践了后感觉也不是什么难事，现在来看自己实现的爬虫都很简单，以后要实现更复杂的爬虫的话，看了这篇博客和代码，能让自己也能快速的捡起来，进行二次开发。

&emsp;&emsp;除了需要 Python 环境外，还需要安装 requests、BeautifulSoup4等。获取微博页面内容时使用cookie的方式，这样不需要用户名和密码就可以请求到微博。

    pip install requests BeautifulSoup4

&emsp;&emsp;好了，准备工作基本OK。这个爬虫是从新浪微博上爬取某个博主的所有图片，在观察了新浪微博里图片URL的规律后，发现链接主要有3部分构成，如下。img-key 部分我估计是存取图片的唯一ID值，part2 取不同的值，会得到不同尺寸的图片，最大尺寸时，part2取值 ‘large’，有了这个规律就好办了，将页面所有图片满足3段式的链接中间那部分替换成'large'，再下载图片即可。


    http://ww2.sinaimg.cn/part2/img-key.jpg

&emsp;&emsp;另外，由于使用的是 *weibo.cn* 域名，从浏览器里得到是一张图片和一个**更多**作为链接，点了链接才看得到所有图片，所以爬每个页面有个二次请求，将更多的图片下载下来。为了避免重复下载导致图片难以维护，保存图片时，将微博的发布日期和图片链接的MD5值组合成图片名称，这样下载到本地后，图片会以在微博上发布的日期排序，同时，再次运行爬虫时，将图片名称后半截的MD5值提取出来，在下载时候对比该图片的链接MD5值是否已经存在，避免重复下载。

&emsp;&emsp;下面是下载一个页面里所有图片的函数代码。


    def download_one_page(soup, user_id, exists):
    """
    download all pictures on the website
    :param soup: web page soup
    :param user_id: the weibo user id
    :param exists exists pic names
    :return: find weibo divs, return True, else False
    """

    # ten weibo div in every page
    divs = soup.find_all(div_filter_func)

    if not divs:
        return False

    for div in divs:
        spans = div.find_all('span')
        wb_post_time = get_weibo_post_time(spans[1].text)

        # abstract a link
        all_img = div.find_all('img')
        img_link = filter(lambda x: x.endswith('.jpg'), [all_img[0].get('src')] if all_img else [])

        # abstract more links
        more_links = [link['href'] for link in div.find_all('a') if link.get('href') is not None]
        more_links_real = [x for x in more_links if 'picAll' in x]
        if more_links_real:
            more_content = requests.get(more_links_real[0], cookies = get_cookie())
            more_soup = BeautifulSoup(more_content.content, 'html.parser')
            more_soup_urls = get_more_page_image_url(more_soup)
            img_link = more_soup_urls if more_soup_urls else img_link

        # download
        for idx, link in enumerate(img_link):
            md5 = calculate_md5(link)
            if md5 not in exists:
                large_link = replace_part2_in_link(link)
                image_content = requests.get(large_link, cookies = get_cookie())

                image_name = "{}>{}_{}".format(wb_post_time, str(idx), md5)
                with open('./downloads/{}/{}.jpg'.format(user_id, image_name), 'wb') as jpg:
                    jpg.write(image_content.content)

                    exists.add(image_name)
                    print('download', large_link, image_name, datetime.datetime.now())
                    time.sleep(random.random())
            else:
                print('jump over:', link)

    sleep = 8 * random.random()
    print('sleep', sleep, 'seconds')
    time.sleep(sleep)
    return True


&emsp;&emsp;在某次打算爬取大量某个博主的图片时，出现了请求失败，查了资料发现是网站有反爬虫功能，于是使用了一些简单的策略，比如请求加上头消息：

    header = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
    }
    
&emsp;&emsp;除此之外，对请求的cookie也在末尾添加随机数，每次用不同的cookie去请求，并且，每爬取完一个页面的内容，随机休眠0-8秒，这样做虽然抓取速度慢了点，但至少能保证每次抓取不会半途报错。

&emsp;&emsp;完整的代码示例[点这里](https://github.com/hsqs/spiders/blob/master/weibo/weibo_miner.py)。    





