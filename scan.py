#!/usr/bin/python
# coding=utf-8

"""Total Scan

Usage:
    scan.py plugins
    scan.py info <plugin>
    scan.py scan -n <thread_num> -t <target> -p <plugin>...
    scan.py scan -n <thread_num> -f <file> -p <plugin>...

Options:
    -h --help       Show help
    -v --version    Show version
"""
import importlib
import os
import threading
import configparser  # Python 3 uses configparser instead of ConfigParser
import time
from tqdm import tqdm
from docopt import docopt  # 用于解析命令行参数
from PySide6.QtCore import Signal, QObject, QThread

from plugins.alive import WebALive
from plugins.content import WebContent

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    """
    调用该函数时传入：
        iteration   - 当前的进度（Int）
        total       - 总进度（Int）
        prefix      - 前缀字符串（Str）
        suffix      - 后缀字符串（Str）
        decimals    - 正数的小数位数（Int）
        length      - 进度条长度（Int）
        fill        - 进度条填充字符（Str）
        print_end   - 结束字符（Str），默认是"\r"，表示进度条更新在同一行
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='')
    # 当完成进度时，打印一个换行符
    if iteration == total:
        print()

class MyThread(threading.Thread):
    """用于多线程执行任务的自定义线程类"""
    def __init__(self, func, args):
        threading.Thread.__init__(self)  # 调用父类构造函数
        self.func = func  # 保存要执行的函数
        self.args = args  # 保存函数参数

    def run(self):
        """线程启动后执行函数"""
        self.func(*self.args)  # 执行函数并传入参数


class WebScan(QObject):
    """核心类，负责插件管理与扫描操作"""

    stop_event = threading.Event()

    # 定义一个信号，传递数据
    data_signal = Signal(str, str)  # 定义信号，传递两个字符串参数

    def __init__(self):
        super().__init__()

        """初始化方法"""
        self.plugins = {"WebAlive": None, "WebContent": None}  # 用于存储加载的插件
        # self.plugin_confs = [
        #     {"name": "WebAlive", "module": "alive"},
        #     {"name": "WebContent", "module": "WebContent"},
        # ]
        # self.import_plugins()  # 导入插件
        self.length = 0
        self.id = 1
        # 从config读取配置信息
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    # def get_plugins_conf(self):
    #     """获取插件的配置信息"""
    #     confs = []
    #     conf_file = [f for f in os.listdir("plugins") if f.endswith(".conf")]  # 获取所有插件的配置文件
    #     cp = configparser.ConfigParser()  # 创建配置文件读取器
    #     for f in conf_file:
    #         cp.read(f"plugins/{f}")  # 读取每个配置文件
    #         conf = {}
    #         for i in cp.items("Documentation"):  # 获取插件文档部分
    #             conf[i[0]] = i[1]
    #         for i in cp.items("Core"):  # 获取插件核心部分
    #             conf[i[0]] = i[1]
    #         confs.append(conf)  # 将配置存入列表
    #
    #     return confs

    # def import_plugins(self):
    #     """动态导入所有插件"""
    #     for plugin_conf in self.plugin_confs:
    #         module_name = plugin_conf["module"].split(".")[0]  # 获取插件模块名
    #         try:
    #             exec(f"from plugins import {module_name}")  # 动态导入插件
    #             exec(f'self.plugins["{plugin_conf["name"]}"]={module_name}')  # 将插件加载到字典中
    #         except Exception as e:
    #             print(f"Failed to import plugin {plugin_conf['name']}: {e}")  # 导入失败时打印错误信息


    # def list_plugins(self):
    #     """列出所有插件的名称和描述"""
    #     print("-" * 80)
    #     print("| %-20s| %s" % ("Plugin", "Description"))  # 显示表头
    #     print("-" * 80)
    #     for plugin in self.plugin_confs:
    #         print("| %-20s| %s" % (plugin["name"], plugin["description"]))  # 显示每个插件的信息
    #         print("-" * 80)

    # def info_plugin(self, plugin):
    #     """
    #     显示指定插件的详细信息
    #     @plugin, str: 插件名
    #     """
    #     print("-" * 80)
    #     for p in self.plugin_confs:
    #         if p["name"] == plugin:
    #             print(f"Name: {p['name']}")
    #             print(f"Description: {p['description']}")
    #             print(f"Author: {p['author']}")
    #             print(f"Version: {p['version']}")
    #             print(f"Website: {p['website']}")
    #             print(f"License: {p['license']}")
    #             print(f"Module: {p['module']}")
    #     print("-" * 80)


    def exec_plugin_single_thread(self, plugin, target, u_id):
        """
        单线程执行插件
        @plugin, str: 插件名，通过self.plugins[plugin]引用插件
        @target, str: 目标网站域名
        """
        ret_result = {"序号": u_id, "网站": target}
        # try:
        if plugin == "WebContent":
            results = WebContent(target).run()  # 执行插件，传入目标
        elif plugin == "WebAlive":
            results = WebALive(target).run()
        else:
            results = None
        # results = {"网站状态": "test"}
        # time.sleep(0.5)
        ret_result.update(results)
        if results:
            with self.lock:
                if not self.stop_event.is_set():
                    self.results[plugin].append(ret_result)

                    # self.data_signal.emit("Done")  # 完成后发送一个完成信号

                    print(f"[{self.id}/{self.length}] - {plugin}: {ret_result}")
        # except Exception as e:
        #     print(f"Error executing plugin {plugin} on target {target}: {e}")  # 捕获执行错误并打印
        #     ret_result["网站状态"] = e
        self.id += 1
        progress = (self.id + 1) / self.length * 100
        self.data_signal.emit(str(progress), str(ret_result))  # 每隔1秒发射一次信号，传递数据
        # print_progress_bar(self.id, self.length, prefix='进度:', suffix='完成', length=50)

    def exec_plugin_threads(self, plugin, targets, thread_num):
        """
        多线程执行插件
        @plugin, str: 插件名
        @targets, list: 目标域名列表
        @thread_num, int: 线程数
        """
        threads = []  # 存储线程对象

        # 为每个目标创建一个线程
        for u_id in targets:
            threads.append(MyThread(self.exec_plugin_single_thread, (plugin, targets[u_id], u_id)))
            # worker_task = MyThread(self.exec_plugin_single_thread,(plugin, targets[u_id], u_id, gui))
            # worker_task.moveToThread(thread)
        self.length = len(threads)

        # 和下面注释选一个即可
        # for i in threads:
        #     i.start()
        #
        # for i in threads:
        #     i.join()

        # 控制线程数，按批次执行线程
        while len(threads) > int(thread_num):
            for i in range(thread_num):
                threads[i].start()  # 启动线程
                # time.sleep(0.05)

            for i in range(thread_num):
                threads[i].join()  # 等待线程执行完毕
            threads = threads[thread_num:]  # 处理下一个批次的线程

        # 启动剩余的线程
        for i in threads:
            i.start()

        for i in threads:
            i.join()

    def exec_plugins(self, plugins, targets, thread_num):
        """
        批量执行插件
        @plugins, list: 要执行的插件列表，'all'表示所有插件
        @targets, list: 目标域名列表
        """
        self.results = {}  # 存储每个插件的扫描结果
        self.lock = threading.Lock()  # 线程锁，防止多个线程同时写结果

        # 如果选择了所有插件，获取所有插件
        if plugins == ["all"]:
            plugins = [plugin for plugin in self.plugins]
        for plugin in plugins:
        # for plugin in tqdm(plugins, desc="Loading plugins", ncols=100, unit="plugin"):
            print(f"Loading Plugin <{plugin}>...")
            if plugin not in self.results:
                self.results[plugin] = []  # 初始化插件结果
            self.exec_plugin_threads(plugin, targets, thread_num)  # 执行插件扫描

    def report(self):
        """输出扫描报告"""
        print("\n\n\n")
        print("-" * 35 + "=" + " Report " + "=" + "-" * 35)
        with open("report.txt", "w") as f:
            split = "+" + "-" * 79  # 分隔线
            print(split)
            f.write(split + "\n")  # 写入分隔线
            for plugin in self.results:
                print(f"| %-18s| {len(self.results[plugin])}" % plugin)  # 输出每个插件的扫描结果数量
                print(split)
                f.write(f"| %-18s| {len(self.results[plugin])}" % plugin)
                f.write("\n" + split + "\n")
                for id, vul in enumerate(self.results[plugin]):
                    print(f"| {id + 1}. {vul}")  # 输出每个漏洞的详情
                    print(split)
                    f.write(f"| {id + 1}. {vul}\n")  # 写入漏洞信息到文件
                    f.write(split + "\n")


# def main():
#     """主函数，解析命令行参数并执行相应操作"""
#     args = docopt(__doc__, version="2014/01/30")  # 解析命令行参数
#     ts = TotalScan()  # 创建TotalScan实例
#
#     if args["plugins"]:
#         ts.list_plugins()  # 列出所有插件
#     elif args["info"]:
#         plugin = args["<plugin>"][0]  # 获取插件名
#         ts.info_plugin(plugin)  # 显示插件信息
#     elif args["scan"]:
#         thread_num = int(args["<thread_num>"])  # 获取线程数
#         if args["-t"]:
#             targets = [args["<target>"]]  # 获取目标域名
#         elif args["-f"]:
#             targets = [target.strip() for target in open(args["<file>"], encoding="utf-8") if not target.isspace()]  # 从文件中读取目标域名
#         plugins = args["<plugin>"]  # 获取插件列表
#         print(plugins)
#         ts.exec_plugins(plugins, targets, thread_num)  # 执行插件扫描
#         ts.report()  # 输出报告
def readfile(fname):
    targets = {}
    if fname.endswith(".txt"):
        with open("test.txt", "r", encoding="utf-8") as fp:
            for u_id, url in enumerate(fp):
                url = url.replace("\n", "")
                targets[u_id] = url
    elif fname.endwith(".xlsx"):
        pass

    return targets


def main():
    ts = WebScan()  # 创建WebScan实例

    thread_num = 2000
    targets = readfile("test.txt")

    plugins = ['WebAlive']
    ts.exec_plugins(plugins, targets, thread_num)  # 执行插件扫描

BANNER = """\
\033[95m_    _      _     _____   
\033[94m| |  | |    | |   /  ___|      
\033[93m| |  | | ___| |__ \ `--.  ___ __ _ _ __  
\033[92m| |/\| |/ _ \ '_ \ `--. \/ __/ _` | '_ \ 
\033[91m\  /\  /  __/ |_) /\__/ / (_| (_| | | | |
\033[95m \/  \/ \___|_.__/\____/ \___\__,_|_| |_| \033[1mV1.0.4\033[0m

\033[90mAuthor: mbigfish
GitHub: https://github.com/mBigFish/WebScan
\033[0m
"""

if __name__ == "__main__":
    start = time.time()
    main()  # 启动程序
    # print(BANNER)
    end = time.time()
    print(end - start)