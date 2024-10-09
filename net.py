import urllib.request
def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.baidu.com')
        return True
    except urllib.error.URLError as e:
        return False
