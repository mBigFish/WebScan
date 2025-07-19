import configparser
import json
import requests
import urllib3
from config import MyConfig
# 禁用 InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WebALive(object):
    def __init__(self, target):
        self.target = target
        config = MyConfig()
        config_section = "web_requests"
        self.config = config.get_config(config_section)
        self.ALLOW_REDIRECT = self.config["ALLOW_REDIRECT"]
        self.OUTFILE = False
        self.VERITY = self.config["VERITY"]
        self.TRYAGAIN = self.config["TRYAGAIN"]
        self.TIMEOUT = int(self.config["TIMEOUT"])
        self.PROXY = {}
        self.header = self.__get_header()

    def run(self):
        # 如果URL不以'http://'或'https://'开头，则默认加上'http://'
        if not self.target.startswith('http://') and not self.target.startswith('https://'):
            self.target = 'http://' + self.target
        return self.__scan()

    def __callback(self, state):

        result = {"网站状态": state}
        return result

    def __scan(self):
        try:
            # 发送HTTP请求判断网站是否存活
            if self.ALLOW_REDIRECT:
                # 允许重定向时的处理逻辑
                r = requests.get(url=self.target, headers=self.header,
                                 timeout=self.TIMEOUT, verify=False, proxies=self.PROXY)
                state = r.status_code
            else:
                # 不允许重定向时的处理逻辑
                r = requests.get(url=self.target, headers=self.header, allow_redirects=False,
                                 timeout=self.TIMEOUT, verify=self.VERITY, proxies=self.PROXY)
                state = r.status_code

            # 处理各种异常情况
        except requests.exceptions.ConnectTimeout as e:
            state = '连接超时'

        except requests.exceptions.ReadTimeout as e:
            state = '读取超时'

        except requests.exceptions.ConnectionError as e:
            state = '连接错误'

        except Exception as e:
            # 如果设置了重试标志，尝试再次扫描该 URL
            if self.TRYAGAIN:
                self.TRYAGAIN = False
                self.__scan()
            state = f"未知错误, {e}"
            # 调用回调函数，通知处理结果
        return self.__callback(state)

    def __get_header(self):
        # if self.RANDOM_HEADER:
        #     header = HeaderGenerator.get_headers()
        # else:
        #     header = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        # }  # 请求的 HTTP 头部信息
        # return header)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Referer': 'https://www.google.com/'
        }
        return headers


def run(target):
    a = WebALive(target)
    a = a.run()
    return a


if __name__ == '__main__':
    b = run("baidu.com")
    print(b)
