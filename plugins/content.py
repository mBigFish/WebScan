import configparser
import datetime
import os
import re
import time
import json
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait
import requests
import urllib3
from bs4 import BeautifulSoup

from config import MyConfig

DEBUG = True
# DEBUG = False
# 禁用 InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""网站错误关键词"""
Errors = ['tengine', 'Apache Tomcat', '站点创建成功', '不存在', '访问报错', 'Domain has expired', '网站建设中',
          '官网登录入口', '502', '网站维护', '温馨提示', '无标题文档', '阻断页面', 'CentOS', '阻止', '无法访问', '域名',
          '站点已暂停', '404', '没有找到站点', '未获取到网站标题', '到期', 'nginx', 'IIS', '恭喜',]

"""网站违法关键词"""
Illegal = ['综合体育', '安全加密检测', '安全检测..', '无码', 'A片', '官方入口', '在线体育', '半岛', '体育彩票',
           '太阳成集团',
           'ios/安卓/手机版app', '官网(中国)', '快三官网', '金博体育', '(中国)官方网站', '真人下注', 'Loading....',
           '体育(中国)',
           'ios', '官网登录入口', 'bwin必赢', '太阳商城', '中欧体育', '愉拍', '日本', '澳门', 'OB体育', '开云',
           'Im体育',
           '必威betway', '亚博', 'AV', '彩票',',好吊视频', '一区二区三区', '国产SUV', '久久蜜', '精品日产', '麻豆',
           '皇冠体育', '三级黄色', '茄子视频', '视频色版', '威尼斯', '小鸡鸡', '骚逼逼', '视频污版', '欧美', '性爽',
           '硬汉视频', '性爱', '人妻', '少妇', '精品视频', '污污', '香蕉视频', '喷水', '啪啪', '91', '污视频', '荔枝视频']

class WebContent(object):
    def __init__(self, target):

        # 从config读取request配置信息
        config = MyConfig()
        config_section = "web_requests"
        self.config = config.get_config(config_section)
        self.ALLOW_REDIRECT = eval(self.config["ALLOW_REDIRECT"])
        self.OUTFILE = False
        self.VERITY = eval(self.config["VERITY"])
        self.TRYAGAIN = eval(self.config["TRYAGAIN"])
        self.TIMEOUT = int(self.config["TIMEOUT"])
        self.PROXY = {}

        config_section = "WebContent"
        self.config = config.get_config(config_section)
        self.GET_WEB_TITLE = eval(self.config["GET_WEB_TITLE"])
        self.GET_WEB_LENGTH = eval(self.config["GET_WEB_LENGTH"])
        self.GET_WEB_LEGAL = eval(self.config["GET_WEB_LEGAL"])
        self.GET_WEB_SERVER = eval(self.config["GET_WEB_SERVER"])
        self.GET_WEB_ICP = eval(self.config["GET_WEB_ICP"])
        self.GET_WEB_GN_ICP =eval(self.config["GET_WEB_GN_ICP"])
        self.GET_WEB_LEGAL_MODE = self.config["GET_WEB_LEGAL_MODE"]


        self.header = self.__get_header()
        self.target = target
        self.tableheader = ['no', 'url', 'ip', 'state',
                            'state_code', 'title', 'server', 'length', 'other']  # CSV 输出的表头
        self.completed_url = -1  # 已完成扫描的 URL 计数器

        if self.OUTFILE:
            self.timenow = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 当前时间戳
            self.outfilename = f'{self.timenow}.csv'  # 输出的 CSV 文件名
            self.errorfilename = f'error_{self.timenow}.txt'  # 错误日志文件名

    def run(self):
        if self.target.startswith('http://') or self.target.startswith('https://'):
            pass
        else:
            self.target = "http://" + self.target
        return self.__scan()

    def __callback(self, state, response):

        result = {"网站状态": state}
        if response:
            if self.GET_WEB_TITLE:
                result["网站标题"] = self.__get_web_title(response)
            if self.GET_WEB_LENGTH:
                result["网页长度"] = self.__get_web_length(response)
            if self.GET_WEB_LEGAL:
                result["研判违规"] = self.__get_web_legal(result["网站标题"])
            if self.GET_WEB_SERVER:
                result["网站服务"] = self.__get_web_server(response)
            if self.GET_WEB_ICP:
                result["ICP备案"] = self.__get_web_icp(response)
            if self.GET_WEB_GN_ICP:
                result["公安备案"] = self.__get_web_gn_icp(response)
        else:
            if self.GET_WEB_TITLE:
                result["网站标题"] = ''
            if self.GET_WEB_LENGTH:
                result["网页长度"] = ''
            if self.GET_WEB_LEGAL:
                result["研判违规"] = '无法打开'
            if self.GET_WEB_SERVER:
                result["网站服务"] = ''
            if self.GET_WEB_ICP:
                result["ICP备案"] = ''
            if self.GET_WEB_GN_ICP:
                result["公安备案"] = ''
        return result

    def __scan(self):
        response = None
        try:
            # 发起 GET 请求
            response = requests.get(
                self.target,
                headers=self.header,
                allow_redirects=self.ALLOW_REDIRECT,  # 跟随重定向
                timeout=self.TIMEOUT,  # 设置超时
                verify=self.VERITY,  # 禁用 SSL 验证
                proxies=self.PROXY
            )

            # 获取 HTTP 状态码
            state = response.status_code
            if not state:
                state = "可能跳转"
            # 调用回调函数处理扫描结果

        except requests.RequestException as e:
            # 捕获所有请求错误（包括网络问题、超时、DNS 查找失败等）
            if DEBUG:
                # print(f"[ERROR] | [请求出错] | {self.target} | [原因{e}]")
                pass
            state = '请求出错'

        except requests.Timeout as e:
            # 请求超时异常
            print(f"请求超时: {e}")
            if DEBUG:
                # print(f"[ERROR] | [请求超时] | {self.target} | [原因{e}]")
                pass
            state = '请求超时'

        except requests.HTTPError as e:
            # HTTP 状态码错误（4xx 和 5xx）
            if DEBUG:
                print(f"[ERROR] | [状态码错误] | {self.target} | [原因{e}]")
            state = '状态码错误'

        except Exception as e:
            # 捕获所有其他异常
            if DEBUG:
                print(f"[ERROR] | [未知错误] | {self.target} | [原因{e}]")
            if self.TRYAGAIN:
                # 如果设置了重试标志，尝试再次扫描该 URL
                self.__scan()
                self.TRYAGAIN = False
            state = "未知错误"
        return self.__callback(state, response)

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

    # @staticmethod
    # def __get_web_title(self, r) -> str:
    #     try:
    #         # 检查响应头中是否包含 Content-Type
    #         if r.headers.get('Content-Type'):
    #             try:
    #                 # 尝试从 Content-Type 中获取字符集信息
    #                 if "charset=" in r.headers.get('Content-Type'):
    #                     charset = r.headers.get('Content-Type').split('charset=')[1]
    #                 # 如果 Content-Type 中没有字符集信息，尝试从 meta 标签中获取
    #                 elif re.findall(r'charset=(.*?)>', r.text)[0].replace('\'', '').replace('"', ''):
    #                     charset = re.findall(r'charset=(.*?)>', r.text)[0].replace('\'', '').replace('"', '')
    #                 else:
    #                     charset = 'utf-8'
    #             except Exception as e:
    #                 if DEBUG:
    #                     # print(f"[ERROR] ｜ [获取标题错误] | [原因{e}]")
    #                     pass
    #                 charset = 'utf-8'
    #         else:
    #             charset = 'utf-8'  # 如果没有 Content-Type，默认使用 utf-8 编码
    #         # 使用获取到的字符集解码响应内容，并从中提取网页标题
    #         return re.findall(r'<title.*?>([^<]*)</title>', r.content.decode(charset))[0]
    #     except Exception as e:
    #         if DEBUG:
    #             print(f"[ERROR]  ｜ [获取标题错误] | [{self.target}原因{e}]")
    #         return "未获取到网站标题"

    def __get_web_title(self, r) -> str:
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        # 提取基础信息示例
        title = soup.title.string if soup.title else '未获取到标题'
        # 去除所有的换行符、制表符等空白字符
        # clean_title = re.sub(r'[\r\n\t]+', ' ', title).strip()
        clean_title = re.sub(r'[\r\n\t]+', ' ', title or "").strip()
        return clean_title

    @staticmethod
    def __get_web_length(r) -> str:
        try:
            return str(len(r.content))
        except AttributeError:
            return "未获取到网页长度"

    def __get_web_legal(self, title) -> str:
        """判断网站是否异常或违法"""
        web_status = "正常网站"
        if self.GET_WEB_LEGAL_MODE == "API":
            if title:
                import requests

                url = "https://v.api.aa1.cn/api/api-mgc/index.php?msg=" + str(title)

                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

                if "存在敏感词" in response.text:
                    web_status = "违法网站"
            else:
                web_status = "异常网站"

        elif self.GET_WEB_LEGAL_MODE == "LOCAL":
            if title:
                web_status = "异常网站" if any(item in title for item in Errors) else web_status
                web_status = "违法网站" if any(item in title for item in Illegal) else web_status
                web_status = "域名出售" if self.target in title and "官网首页" in title else web_status
            else:
                web_status = "异常网站"

        return web_status


    @staticmethod
    def __get_web_server(r) -> str:
        try:
            return r.headers.get('server')
        except AttributeError:
            return "未获取到网站服务"

    @staticmethod
    def __get_web_icp(r) -> str:
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        # 找到包含 ICP 备案关键字的元素
        icp_elements = soup.find_all(string=re.compile(r'ICP备\d'))
        # 提取备案信息
        icp_number = "未找到icp备案"
        for element in icp_elements:
            # 进一步处理字符串，提取具体备案信息
            # icp_match = re.search(r'ICP备[^\d]*(\d+)[^\u4e00-\u9fa5]*([\u4e00-\u9fa5]+)', element)
            # icp_match = re.search(r'([\u4e00-\u9fa5]*ICP备[^\d]*\d+[^\u4e00-\u9fa5]*[\u4e00-\u9fa5]+-*\d*)', element)
            icp_match = re.search(r'([\u4e00-\u9fa5]?ICP备\d+[^\u4e00-\u9fa5]*[\u4e00-\u9fa5]+-*\d*)', element)
            if icp_match:
                icp_number = icp_match.group(1)
            else:
                icp_number = "可能存在icp备案，但未爬取到"
        icp_number = icp_number.replace(" ", "")
        return icp_number
    @staticmethod
    def __get_web_gn_icp(r) -> str:
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        # 找到包含公安备案关键字的元素
        public_security_elements = soup.find_all(string=re.compile(r'公网安备'))
        # 提取公安备案信息
        public_security_number = "未找到公安备案"
        for element in public_security_elements:
            # 进一步处理字符串，提取具体备案信息
            public_security_match = re.search(r'([\u4e00-\u9fa5]?公网安备\s*\d+号)', element)
            if public_security_match:
                public_security_number = public_security_match.group(1)
            else:
                public_security_number = "可能存在公安备案，但未爬取到"
        public_security_number = public_security_number.replace(" ", "")
        return public_security_number

def run(target):
    w = WebContent(target)
    a = w.run()
    return a

if __name__ == '__main__':
    a = run("www.cque.edu.cn")
    print(a)