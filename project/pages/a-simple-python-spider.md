title: 一个简单的 Python 爬虫
date: 2016-04-10

&emsp;&emsp;由于我经常逛微博，看到某些博主的图片都很好看（你懂的），就想干脆下载到本地，于是萌生了搞个爬虫的想法。之前听说 Python 网络爬虫，听起来高大上，在实践了后感觉也不是什么难事，现在来看自己实现的爬虫都很简单，以后要实现更复杂的爬虫的话，看了这篇博客和代码，能让自己也能快速的捡起来，进行二次开发。

&emsp;&emsp;获取微博页面内容时使用cookie，从而不需要用户名和密码来登陆页面。除了需要 Python 环境外，还需要安装 requests、BeautifulSoup4等。

    pip install requests BeautifulSoup4

&emsp;&emsp;好了，准备工作基本OK。这个爬虫是从新浪微博上爬取某个博主的所有图片，在观察了新浪微博里图片URL的规律后，发现链接主要有3部分构成，如下。img-key 部分我估计是存取图片的唯一ID值，part2 取不同的值，会得到不同尺寸的图片，最大尺寸时，part2取值 ‘large’，有了这个规律就好办了，将页面所有图片满足3段式的链接中间那部分替换成'large'，再下载图片即可。


    http://ww2.sinaimg.cn/part2/img-key.jpg

&emsp;&emsp;另外，由于使用的是 *weibo.cn* 域名，从浏览器里得到是一张图片和一个**更多**作为链接，点了链接才看得到所有图片，所以爬每个页面有个二次请求，将更多的图片下载下来。为了避免重复下载导致图片难以维护，保存图片时，将日期作为图片的名字，再次运行爬虫时会检查该图片名字，避免重复下载。

&emsp;&emsp;下面是下载一个页面里所有图片的函数代码。


    def download_one_page(soup, user_id):
    '''
    download all pictures on the website
    :param soup: web page soup
    :param user_id: the weibo user id
    :return: None
    '''

    # 获取每页的十条微博
    div_c = [div for div in soup.find_all('div') if div.get('class', 'null') == ['c']]
    divs = [div for div in div_c if div.get('id') is not None]

    for div in divs:
        spans = div.find_all('span')

        wb_post_time = get_weibo_post_time(spans[1].text)

        all_img = div.find_all('img')
        img_link = filter(lambda x: x.endswith('.jpg'), [all_img[0].get('src')] if all_img else [])

        # 获取更多链接里的图片链接,如果存在则替换已有的图片链接列表
        more_links = [link['href'] for link in div.find_all('a') if link.get('href') is not None]
        more_links_real = [x for x in more_links if 'picAll' in x]
        if more_links_real:
            more_content = requests.get(more_links_real[0], cookies = cookie)
            more_soup = BeautifulSoup(more_content.content, 'html.parser')
            more_soup_urls = get_more_page_image_url(more_soup)
            img_link = more_soup_urls if more_soup_urls else img_link

        # 下载得到的每一张图片
        for idx, link in enumerate(img_link):
            image_name = wb_post_time + '>' + str(idx)
            if image_name not in exists:
                # 使用大图链接
                large_link = replace_part2_in_link(link)
                image_content = requests.get(large_link, cookies = cookie)
                with open('./downloads/{}/{}.jpg'.format(user_id, image_name), 'wb') as jpg:
                    jpg.write(image_content.content)

                    exists.append(image_name)
                    print('download', large_link, image_name, datetime.datetime.now())
            else:
                print('jump over:', image_name)


&emsp;&emsp;完整的代码示例[点这里](https://github.com/hsqs/spiders/blob/master/weibo/weibo_miner.py)。

&emsp;&emsp;顺便，贴一个 Python 爬虫常用技巧链接，以后或许可以用到，[点这里](http://my.oschina.net/jhao104/blog/647308?fromerr=KzH2VGaK)。




