import gevent
import urllib.request
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(downloader, "3.jpg", ""),
        gevent.spawn(downloader, "4.jpg", "")
    ])

if __name__ == '__main__':
    main()

