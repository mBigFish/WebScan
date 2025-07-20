import json
import os
from threading import Thread

import openpyxl
import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation, Qt, QThread, QTimer
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QButtonGroup, QLabel, QTableWidgetItem, QAbstractItemView, QHeaderView, QSpinBox, \
    QPushButton, QFileDialog, QApplication

import plugins
from gui.core.json_themes import Themes
from gui.uis.windows.main_window import UI_MainWindow
from gui.widgets import *
from core.icp.GetIcp import ICP
from config import MyConfig
from scan import WebScan


class UiPageScan:
    """废物函数，只是为了可以让下面函数给出提示"""
    def __init__(self):
        self.themes = Themes().items
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.THREAD_POOL_SIZE = None
        self.GET_WEB_LEGAL = None
        self.GET_WEB_SERVER = None
        self.GET_WEB_ICP = None
        self.GET_WEB_GN_ICP = None
        self.targets = {}
        self.button_group_plugins_name = None

    def setup_ui(self):
        self.targets = {}
        # 插件选择模块设置按钮背景
        def __set_plugins_button_bg_color():
            # 默认背景颜色
            self.push_button_scan_plugins_row1.set_bg_color(self.themes["app_color"]["dark_one"])
            self.push_button_scan_plugins_row2.set_bg_color(self.themes["app_color"]["dark_one"])
            # self.push_button_scan_plugins_row3.set_bg_color(self.themes["app_color"]["dark_one"])

        # 插件选择模块按钮点击函数
        def __plugins_button_clicked(button):
            # 设置所有按钮为默认背景
            __set_plugins_button_bg_color()
            # 修改选中按钮的背景颜色
            button.set_bg_color("#278ea5")
            params_result = {}
            if button.text() == "网站存活检测":
                params_result["SCAN_FUNCTION"] = "WebAlive"
            elif button.text() == "网站内容爬取":
                params_result["SCAN_FUNCTION"] = "WebContent"
            # elif button.text() == "获取网站IP":
            #     params_result["SCAN_FUNCTION"] = "IPLocation"
            self.config.change_config("main", params_result)
            self.button_group_plugins_name = params_result["SCAN_FUNCTION"]

        # 参数模块初始化
        def scan_initialize():
            # params requests
            web_requests_values = self.config.get_config("web_requests")
            self.toggle_params_allow_redirect.setChecked(eval(web_requests_values["ALLOW_REDIRECT"]))
            self.toggle_params_verity.setChecked(eval(web_requests_values["VERITY"]))
            self.toggle_params_tryagain.setChecked(eval(web_requests_values["TRYAGAIN"]))
            self.spingbox_params_timeout.setValue(int(web_requests_values["TIMEOUT"]))
            self.config_get_section = self.config.get_config("web_requests")
            # params content
            WebContent_values = self.config.get_config("WebContent")
            self.GET_WEB_LEGAL = eval(WebContent_values["GET_WEB_LEGAL"])
            self.GET_WEB_SERVER = eval(WebContent_values["GET_WEB_SERVER"])
            self.GET_WEB_ICP = eval(WebContent_values["GET_WEB_ICP"])
            self.GET_WEB_GN_ICP = eval(WebContent_values["GET_WEB_GN_ICP"])
            self.toggle_params_get_web_legal.setChecked(self.GET_WEB_LEGAL)
            self.toggle_params_get_web_server.setChecked(self.GET_WEB_SERVER)
            self.toggle_params_get_web_icp.setChecked(self.GET_WEB_ICP)
            self.toggle_params_get_web_gnicp.setChecked(self.GET_WEB_GN_ICP)
            # params main
            main = self.config.get_config("main")
            self.THREAD_POOL_SIZE = int(main["THREAD_POOL_SIZE"])
            self.vertical_params_thread_pool_size.setValue(self.THREAD_POOL_SIZE)
            self.label_params_thread_pool_size.setText(str(self.THREAD_POOL_SIZE))
            self.button_group_plugins_name = main["SCAN_FUNCTION"]
            if self.button_group_plugins_name == "WebAlive":
                __plugins_button_clicked(self.push_button_scan_plugins_row1)
            elif self.button_group_plugins_name == "WebContent":
                __plugins_button_clicked(self.push_button_scan_plugins_row2)
            # elif self.button_group_plugins_name == "IPLocation":
            #     __plugins_button_clicked(self.push_button_scan_plugins_row3)

        # 参数模块选择函数
        def __scan_params_changed(section_name):
            params_result = {}
            if section_name == "web_requests":
                ALLOW_REDIRECT = self.toggle_params_allow_redirect.isChecked()
                VERITY = self.toggle_params_verity.isChecked()
                TIMEOUT = self.spingbox_params_timeout.value()
                TRYAGAIN = self.toggle_params_tryagain.isChecked()
                params_result["ALLOW_REDIRECT"] = ALLOW_REDIRECT
                params_result["VERITY"] = VERITY
                params_result["TIMEOUT"] = TIMEOUT
                params_result["TRYAGAIN"] = TRYAGAIN
            elif section_name == "WebContent":
                self.GET_WEB_LEGAL = self.toggle_params_get_web_legal.isChecked()
                self.GET_WEB_SERVER = self.toggle_params_get_web_server.isChecked()
                self.GET_WEB_ICP = self.toggle_params_get_web_icp.isChecked()
                self.GET_WEB_GN_ICP = self.toggle_params_get_web_gnicp.isChecked()
                params_result["GET_WEB_LEGAL"] = self.GET_WEB_LEGAL
                params_result["GET_WEB_SERVER"] = self.GET_WEB_SERVER
                params_result["GET_WEB_ICP"] = self.GET_WEB_ICP
                params_result["GET_WEB_GN_ICP"] = self.GET_WEB_GN_ICP
            elif section_name == "main":
                self.THREAD_POOL_SIZE = str(self.vertical_params_thread_pool_size.value())
                params_result["THREAD_POOL_SIZE"] = self.THREAD_POOL_SIZE
                self.label_params_thread_pool_size.setText(self.THREAD_POOL_SIZE)
            print(params_result)
            self.config.change_config(section_name, params_result)

        def __start_scan():
            thread_num = self.THREAD_POOL_SIZE
            plugins = []
            plugins.append(self.button_group_plugins_name)
            thread = Thread(target=self.worker.exec_plugins, args=(plugins, self.targets, int(thread_num)))
            # self.worker.data_signal.connect(__updata_signal)  # 将 Worker 的信号连接到槽
            thread.start()

        def __updata_signal(progress, data):
            progress = int(float(progress))
            self.circular_progress_scan.set_value(progress)
            data = eval(data)
            # 更新UI，实时显示从 Worker 收到的数据
            __table_add_result(data)
            if progress == 100:
                self.push_button_scan_params_start.setEnabled(True)
                self.push_button_scan_params_start.set_bg_color(self.themes["app_color"]["dark_one"])
                self.push_button_scan_params_start.setText("开始运行")
                self.ui.load_pages.label_hint.setText("程序运行结束！")

        # 参数模块按钮函数
        def __params__button_clicked(btn_name):
            if btn_name == "start":
                if not self.targets:
                    self.ui.load_pages.label_hint.setText("请先选择文件！")
                    return
                self.push_button_scan_params_start.setEnabled(False)
                self.push_button_scan_params_start.set_bg_color(self.themes["app_color"]["pink"])
                self.push_button_scan_params_start.setText("正在运行")
                self.ui.load_pages.label_hint.setText("程序正在运行过程中，请等待....")
                __start_scan()
            # elif btn_name == "select_file":
            #     self.table_scan_result.clearContents()
            #     __select_file()
            #     __table_add_url()
            elif btn_name == "export":
                __exporting_file()

        # def __table_set():
        #
        #     # if self.button_group_plugins_name == "WebAlive":
        #     #     self.table_scan_result.setColumnCount(2)
        #     #     self.table_scan_result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #     #     self.table_scan_result.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #     #     self.table_scan_result.setSelectionBehavior(QAbstractItemView.SelectRows)
        #     #
        #     #     # 列 / 表头
        #     #     self.column_0 = QTableWidgetItem()
        #     #     self.column_0.setTextAlignment(Qt.AlignCenter)
        #     #     self.column_0.setText("网站域名")
        #     #
        #     #     self.column_1 = QTableWidgetItem()
        #     #     self.column_1.setTextAlignment(Qt.AlignCenter)
        #     #     self.column_1.setText("网站状态")
        #     #
        #     #     # 设置列
        #     #     self.table_scan_result.setHorizontalHeaderItem(0, self.column_0)
        #     #     self.table_scan_result.setHorizontalHeaderItem(1, self.column_1)
        #     self.table_scan_result.setColumnCount(7)
        #     self.table_scan_result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #     self.table_scan_result.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #     self.table_scan_result.setSelectionBehavior(QAbstractItemView.SelectRows)
        #
        #     # 列 / 表头
        #     self.column_0 = QTableWidgetItem()
        #     self.column_0.setTextAlignment(Qt.AlignCenter)
        #     self.column_0.setText("网站域名")
        #
        #     self.column_1 = QTableWidgetItem()
        #     self.column_1.setTextAlignment(Qt.AlignCenter)
        #     self.column_1.setText("网站状态")
        #
        #     self.column_2 = QTableWidgetItem()
        #     self.column_2.setTextAlignment(Qt.AlignCenter)
        #     self.column_2.setText("网站标题")
        #
        #     self.column_3 = QTableWidgetItem()
        #     self.column_3.setTextAlignment(Qt.AlignCenter)
        #     self.column_3.setText("网页长度")
        #
        #     self.column_4 = QTableWidgetItem()
        #     self.column_4.setTextAlignment(Qt.AlignCenter)
        #     self.column_4.setText("是否违规")
        #
        #     self.column_5 = QTableWidgetItem()
        #     self.column_5.setTextAlignment(Qt.AlignCenter)
        #     self.column_5.setText("网站服务")
        #
        #     self.column_6 = QTableWidgetItem()
        #     self.column_6.setTextAlignment(Qt.AlignCenter)
        #     self.column_6.setText("ICP备案")
        #
        #     self.column_7 = QTableWidgetItem()
        #     self.column_7.setTextAlignment(Qt.AlignCenter)
        #     self.column_7.setText("公安备案")
        #
        #     # 设置列
        #     # self.table_scan_result.setHorizontalHeaderItem(0, self.column_0)
        #     self.table_scan_result.setHorizontalHeaderItem(0, self.column_0)
        #     self.table_scan_result.setHorizontalHeaderItem(1, self.column_1)
        #     self.table_scan_result.setHorizontalHeaderItem(2, self.column_2)
        #     self.table_scan_result.setHorizontalHeaderItem(3, self.column_3)
        #     self.table_scan_result.setHorizontalHeaderItem(4, self.column_4)
        #     self.table_scan_result.setHorizontalHeaderItem(5, self.column_5)
        #     self.table_scan_result.setHorizontalHeaderItem(6, self.column_6)
        #     self.table_scan_result.setHorizontalHeaderItem(7, self.column_7)



        # 表格添加URL

        def __table_add_url():
            for u_id in self.targets:
                row_number = self.table_scan_result.rowCount()
                item = QTableWidgetItem(str(self.targets[u_id]))
                item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                self.table_scan_result.insertRow(row_number)  # 插入行
                self.table_scan_result.setItem(row_number, 0, item)  # 添加域名
                self.table_scan_result.setRowHeight(row_number, 20)

        # 表格添加结果
        def __table_add_result(result):
            if self.button_group_plugins_name == "WebAlive":
                u_id = int(result["序号"])
                u_status = result["网站状态"]
                item = QTableWidgetItem(str(u_status))
                item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                self.table_scan_result.setItem(u_id, 1, item)  # 添加域名
            elif self.button_group_plugins_name == "WebContent":
                u_id = int(result["序号"])
                u_status = result["网站状态"]
                u_title = result["网站标题"]
                u_length = result["网页长度"]
                item = QTableWidgetItem(str(u_status))
                item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                self.table_scan_result.setItem(u_id, 1, item)  # 添加网站状态
                item = QTableWidgetItem(str(u_title))
                item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                self.table_scan_result.setItem(u_id, 2, item)  # 添加网站标题
                item = QTableWidgetItem(str(u_length))
                item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                self.table_scan_result.setItem(u_id, 3, item)  # 添加网页长度
                if "研判违规" in result:
                    u_content = result["研判违规"]
                    item = QTableWidgetItem(str(u_content))
                    item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                    self.table_scan_result.setItem(u_id, 4, item)  # 网站标题
                if "网站服务" in result:
                    u_content = result["网站服务"]
                    item = QTableWidgetItem(str(u_content))
                    item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                    self.table_scan_result.setItem(u_id, 5, item)  # 网站标题
                if "ICP备案" in result:
                    u_content = result["ICP备案"]
                    item = QTableWidgetItem(str(u_content))
                    item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                    self.table_scan_result.setItem(u_id, 6, item)  # 网站标题
                if "公安备案" in result:
                    u_content = result["公安备案"]
                    item = QTableWidgetItem(str(u_content))
                    item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                    self.table_scan_result.setItem(u_id, 7, item)  # 网站标题

        # 参数模块选择文件
        def __select_file(file_form):
            self.table_scan_result.clearContents()
            file_path = ''
            if file_form == 'txt':
                file_dialog = QFileDialog()
                file_path = file_dialog.getOpenFileName(self, "选择txt文件", "", "文本文件 (*.txt)")[0]
            elif file_form == 'excel':
                file_dialog = QFileDialog()
                file_path = file_dialog.getOpenFileName(self, "选择Excel文件", "", "文本文件 (*.xlsx)")[0]
            elif file_form == 'history':
                main = self.config.get_config("main")
                file_path = main["FILE_PATH"]
            self.ui.load_pages.label_hint.setText(file_path)
            __read_file(file_path)
            __table_add_url()

            # 写入config
            params_result = {"FILE_PATH": file_path}
            self.config.change_config("main", params_result)

        def __read_file(file_path):
            self.targets = {}
            if not os.path.exists(file_path):
                self.ui.load_pages.label_hint.setText("文件不存在，请重新选择！")
                return
            if file_path.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as fp:
                    for u_id, url in enumerate(fp):
                        url = url.replace("\n", "")
                        self.targets[u_id] = url
            elif file_path.endswith(".xlsx"):
                self.targets = {}
                try:
                    # 打开 Excel 文件
                    workbook = openpyxl.load_workbook(file_path)
                    # 选择第一个工作表
                    sheet = workbook.active
                    # 遍历行
                    for u_id, row in enumerate(sheet.iter_rows(values_only=True)):
                        url = row[0]  # 无http头
                        # print(u_id, url)
                        self.targets[u_id] = url
                except FileNotFoundError:
                    print("文件未找到，请检查文件路径是否正确。")
                except Exception as e:
                    print(f"发生了其他错误: {e}")
                return self.targets

        # 停止扫描
        def __stop_scan():
            WebScan.stop_event.set()


        # 导出表格
        def __exporting_file():
            file_path, _ = QFileDialog.getSaveFileName(self, "保存 Excel 文件", "", "Excel 文件 (*.xlsx)")
            if not file_path:
                return

            # 读取表格数据
            data = []
            headers = [self.table_scan_result.horizontalHeaderItem(i).text() for i in range(self.table_scan_result.columnCount())]
            for row in range(self.table_scan_result.rowCount()):
                row_data = []
                for col in range(self.table_scan_result.columnCount()):
                    item = self.table_scan_result.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)

            # 使用 pandas 处理
            df = pd.DataFrame(data, columns=headers)
            df.to_excel(file_path, index=False, engine="openpyxl")

            print(f"Excel 导出成功：{file_path}")

        self.config = MyConfig()
        # self.worker = WebScan()  # 创建 Worker 实例

        # 创建 Worker 实例
        self.worker = WebScan()
        # self.thread = QThread()
        #
        # # 将 Worker 移动到线程
        # self.worker.moveToThread(self.thread)

        # 连接信号与槽
        self.worker.data_signal.connect(__updata_signal)


        """左侧-上侧-左侧"""
        # scan_plugins_row1开关
        self.push_button_scan_plugins_row1 = PyPushButton(
            text="网站存活检测",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_width=2,
            border_style="solid",
            border_color="#568AF2",
            border_color_hover="#72A2FF",  # 悬停时边框变亮
            border_color_pressed="#3B5B92"  # 按下时边框变暗
        )
        self.push_button_scan_plugins_row1.setMinimumHeight(30)
        self.ui.load_pages.scan_plugins_layout_row1.addWidget(self.push_button_scan_plugins_row1)

        # scan_plugins_row2开关
        self.push_button_scan_plugins_row2 = PyPushButton(
            text="网站内容爬取",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_width=2,
            border_style="solid",
            border_color="#568AF2",
            border_color_hover="#72A2FF",  # 悬停时边框变亮
            border_color_pressed="#3B5B92"  # 按下时边框变暗
        )
        self.push_button_scan_plugins_row2.setMinimumHeight(30)
        self.ui.load_pages.scan_plugins_layout_row2.addWidget(self.push_button_scan_plugins_row2)

        # scan_plugins_row3开关
        # self.push_button_scan_plugins_row3 = PyPushButton(
        #     text="获取网站IP",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"],
        #     border_width=2,
        #     border_style="solid",
        #     border_color="#568AF2",
        #     border_color_hover="#72A2FF",  # 悬停时边框变亮
        #     border_color_pressed="#3B5B92"  # 按下时边框变暗
        # )
        # self.push_button_scan_plugins_row3.setMinimumHeight(30)
        # self.ui.load_pages.scan_plugins_layout_row3.addWidget(self.push_button_scan_plugins_row3)

        # 创建一个QButtonGroup
        self.button_group_plugins = QButtonGroup(self)

        # 将按钮添加到QButtonGroup
        self.button_group_plugins.addButton(self.push_button_scan_plugins_row1)
        self.button_group_plugins.addButton(self.push_button_scan_plugins_row2)
        # self.button_group_plugins.addButton(self.push_button_scan_plugins_row3)

        # 设置按钮点击后的行为
        self.button_group_plugins.buttonClicked.connect(__plugins_button_clicked)


        """左侧-上侧-右侧"""
        # 网络请求参数
        # 允许跳转
        self.label_params_allow_redirect = QLabel()
        self.label_params_allow_redirect.setMaximumWidth(65)
        self.label_params_allow_redirect.setMaximumHeight(40)
        self.label_params_allow_redirect.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_allow_redirect.setText("允许跳转")
        self.toggle_params_allow_redirect = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.label_params_allow_redirect)
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.toggle_params_allow_redirect)
        #SSL验证
        self.label_params_verity = QLabel()
        self.label_params_verity.setMaximumWidth(65)
        self.label_params_verity.setMaximumHeight(40)
        self.label_params_verity.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_verity.setText("SSL验证")
        self.toggle_params_verity = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.label_params_verity)
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.toggle_params_verity)
        # 错误重试
        self.label_params_tryagain = QLabel()
        self.label_params_tryagain.setMaximumWidth(65)
        self.label_params_tryagain.setMaximumHeight(40)
        self.label_params_tryagain.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_tryagain.setText("错误重试")
        self.toggle_params_tryagain = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.label_params_tryagain)
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.toggle_params_tryagain)
        # 超时时间
        self.label_params_timeout = QLabel()
        self.label_params_timeout.setMaximumWidth(65)
        self.label_params_timeout.setMaximumHeight(40)
        self.label_params_timeout.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_timeout.setText("超时时间")
        self.spingbox_params_timeout = QSpinBox(
            minimum=3,
            maximum=15,
        )
        self.spingbox_params_timeout.setStyleSheet("""
            QSpinBox {
                background-color: #1b1e23;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                color: #8a95aa;
            }
            QSpinBox:focus {
                border-color: #0099ff;
                background-color: #1b1e23;
            }
            QSpinBox::up-button {
                background-color: #568AF2;
                border: 1px solid #568AF2;
            }
            QSpinBox::down-button {
                background-color: #cccccc;
                border: 1px solid #aaa;
            }
        """)

        #     width=50,
        #     bg_color=self.themes["app_color"]["dark_two"],
        #     circle_color=self.themes["app_color"]["icon_color"],
        #     active_color=self.themes["app_color"]["context_color"]
        # )
        self.spingbox_params_timeout.setMaximumWidth(50)
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.label_params_timeout)
        self.ui.load_pages.scan_params_layout_row1_1.addWidget(self.spingbox_params_timeout)

        # 内容爬取模块
        # 研判违规
        self.label_params_get_web_legal = QLabel()
        self.label_params_get_web_legal.setMaximumWidth(65)
        self.label_params_get_web_legal.setMaximumHeight(40)
        self.label_params_get_web_legal.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_get_web_legal.setText("研判违规")
        self.toggle_params_get_web_legal = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.label_params_get_web_legal)
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.toggle_params_get_web_legal)
        # 网站服务
        self.label_params_get_web_server = QLabel()
        self.label_params_get_web_server.setMaximumWidth(65)
        self.label_params_get_web_server.setMaximumHeight(40)
        self.label_params_get_web_server.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_get_web_server.setText("网站服务")
        self.toggle_params_get_web_server = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.label_params_get_web_server)
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.toggle_params_get_web_server)
        # 网站备案
        self.label_params_get_web_icp = QLabel()
        self.label_params_get_web_icp.setMaximumWidth(65)
        self.label_params_get_web_icp.setMaximumHeight(40)
        self.label_params_get_web_icp.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_get_web_icp.setText("网站备案")
        self.toggle_params_get_web_icp = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.label_params_get_web_icp)
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.toggle_params_get_web_icp)
        # 公安备案
        self.label_params_get_web_gnicp = QLabel()
        self.label_params_get_web_gnicp.setMaximumWidth(65)
        self.label_params_get_web_gnicp.setMaximumHeight(40)
        self.label_params_get_web_gnicp.setStyleSheet("QLabel { border: none; }")  # 去掉标签的边框
        self.label_params_get_web_gnicp.setText("公安备案")
        self.toggle_params_get_web_gnicp = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.label_params_get_web_gnicp)
        self.ui.load_pages.scan_params_layout_row2_1.addWidget(self.toggle_params_get_web_gnicp)


        # main
        # 线程数量
        self.vertical_params_thread_pool_size = PySlider(
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_params_thread_pool_size.setOrientation(Qt.Horizontal)
        self.vertical_params_thread_pool_size.setMinimumWidth(300)
        self.vertical_params_thread_pool_size.setMaximumWidth(600)
        self.vertical_params_thread_pool_size.setMaximum(1000)
        self.vertical_params_thread_pool_size.setMinimum(1)


        self.label_params_thread_pool_size = QLabel()
        self.label_params_thread_pool_size.setMinimumWidth(42)
        self.label_params_thread_pool_size.setMaximumWidth(42)

        self.label_params_thread_pool_size.setMaximumHeight(40)

        self.ui.load_pages.scan_params_layout_row3_1.addWidget(self.vertical_params_thread_pool_size)
        self.ui.load_pages.scan_params_layout_row3_1.addWidget(self.label_params_thread_pool_size)

        # 提示标签  设置文本居中
        self.ui.load_pages.label_hint.setAlignment(Qt.AlignCenter)

        # 信号连接
        # web_requests
        self.toggle_params_allow_redirect.clicked.connect(lambda: __scan_params_changed("web_requests"))
        self.toggle_params_verity.clicked.connect(lambda: __scan_params_changed("web_requests"))
        self.toggle_params_tryagain.clicked.connect(lambda: __scan_params_changed("web_requests"))
        self.spingbox_params_timeout.valueChanged.connect(lambda: __scan_params_changed("web_requests"))

        # WebContent
        self.toggle_params_get_web_legal.clicked.connect(lambda: __scan_params_changed("WebContent"))
        self.toggle_params_get_web_server.clicked.connect(lambda: __scan_params_changed("WebContent"))
        self.toggle_params_get_web_icp.clicked.connect(lambda: __scan_params_changed("WebContent"))
        self.toggle_params_get_web_gnicp.clicked.connect(lambda: __scan_params_changed("WebContent"))

        # main1
        self.vertical_params_thread_pool_size.valueChanged.connect(lambda: __scan_params_changed("main"))


        """左侧-下侧"""
        # 表格控件
        self.table_scan_result = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_scan_result.setColumnCount(8)
        self.table_scan_result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_scan_result.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_scan_result.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 列 / 表头
        self.column_0 = QTableWidgetItem()
        self.column_0.setTextAlignment(Qt.AlignCenter)
        self.column_0.setText("网站域名")

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("网站状态")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("网站标题")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("网页长度")

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText("研判违规")

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText("网站服务")

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText("ICP备案")

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText("公安备案")

        # 设置列
        # self.table_scan_result.setHorizontalHeaderItem(0, self.column_0)
        self.table_scan_result.setHorizontalHeaderItem(0, self.column_0)
        self.table_scan_result.setHorizontalHeaderItem(1, self.column_1)
        self.table_scan_result.setHorizontalHeaderItem(2, self.column_2)
        self.table_scan_result.setHorizontalHeaderItem(3, self.column_3)
        self.table_scan_result.setHorizontalHeaderItem(4, self.column_4)
        self.table_scan_result.setHorizontalHeaderItem(5, self.column_5)
        self.table_scan_result.setHorizontalHeaderItem(6, self.column_6)
        self.table_scan_result.setHorizontalHeaderItem(7, self.column_7)

        # # self.table_scan_result.verticalHeader().setVisible(False)
        # # self.table_scan_result.resizeColumnToContents(0)
        # self.table_scan_result.setColumnWidth(0, 20)

        # 添加控件
        self.ui.load_pages.scan_left_down_layout.addWidget(self.table_scan_result)




        """右侧"""
        # 圆形进度条
        self.circular_progress_scan = PyCircularProgress(
            value=0,
            progress_width=4,
            progress_color=self.themes["app_color"]["pink"],
            text_color=self.themes["app_color"]["context_color"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_scan.setFixedSize(160, 160)
        self.ui.load_pages.scan_right_layout_row1.addWidget(self.circular_progress_scan)

        # label
        # self.test_label = QLabel()
        # self.test_label.setText("测试")
        # self.ui.load_pages.scan_right_layout.addWidget(self.test_label)

        # main2
        self.push_button_scan_params_select_file_txt = PyPushButton(
            text="选择文件（txt）",
            radius=20,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_color="#408ab4"
        )
        self.push_button_scan_params_select_file_txt.setMinimumWidth(80)
        self.push_button_scan_params_select_file_txt.setMinimumHeight(40)
        self.push_button_scan_params_select_file_excel = PyPushButton(
            text="选择文件（excel）",
            radius=20,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_color="#408ab4"
        )
        self.push_button_scan_params_select_file_excel.setMinimumWidth(80)
        self.push_button_scan_params_select_file_excel.setMinimumHeight(40)
        self.push_button_scan_params_select_file_history = PyPushButton(
            text="选择文件（上次）",
            radius=20,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_color="#408ab4"
        )
        self.push_button_scan_params_select_file_history.setMinimumWidth(80)
        self.push_button_scan_params_select_file_history.setMinimumHeight(40)
        self.push_button_scan_params_start = PyPushButton(
            text="开始运行",
            radius=20,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_color="#408ab4"
        )
        self.push_button_scan_params_start.setMinimumWidth(80)
        self.push_button_scan_params_start.setMinimumHeight(40)
        self.push_button_scan_params_stop = PyPushButton(
            text="停止运行",
            radius=20,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_color="#408ab4"
        )
        self.push_button_scan_params_stop.setMinimumWidth(80)
        self.push_button_scan_params_stop.setMinimumHeight(40)
        self.push_button_scan_params_exporting_file = PyPushButton(
            text="导出表格",
            radius=20,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            border_color="#408ab4"
        )
        self.push_button_scan_params_exporting_file.setMinimumWidth(80)
        self.push_button_scan_params_exporting_file.setMinimumHeight(40)

        self.ui.load_pages.scan_right_layout_row2.addWidget(self.push_button_scan_params_select_file_txt)
        self.ui.load_pages.scan_right_layout_row2.addWidget(self.push_button_scan_params_select_file_excel)
        self.ui.load_pages.scan_right_layout_row2.addWidget(self.push_button_scan_params_select_file_history)
        self.ui.load_pages.scan_right_layout_row3.addWidget(self.push_button_scan_params_start)
        self.ui.load_pages.scan_right_layout_row3.addWidget(self.push_button_scan_params_stop)
        self.ui.load_pages.scan_right_layout_row3.addWidget(self.push_button_scan_params_exporting_file)
        # 连接信号
        self.push_button_scan_params_select_file_txt.clicked.connect(lambda: __select_file("txt"))
        self.push_button_scan_params_select_file_excel.clicked.connect(lambda: __select_file("excel"))
        self.push_button_scan_params_select_file_history.clicked.connect(lambda: __select_file("history"))
        self.push_button_scan_params_start.clicked.connect(lambda: __params__button_clicked("start"))
        self.push_button_scan_params_stop.clicked.connect(lambda: __stop_scan())
        self.push_button_scan_params_exporting_file.clicked.connect(lambda: __params__button_clicked("export"))

        # 初始化
        scan_initialize()













        # test
        # self.test = QLabel(self)
        # self.test.setStyleSheet("""
        #      border: 1px solid purple;         /* 设置边框颜色为蓝色，宽度为3px */
        #      border-radius: 20px;            /* 设置圆角边框 */
        #      padding: 10px;                  /* 设置内边距 */
        #  """)
        #
        # self.ui.load_pages.scan_left_down_layout.addWidget(self.test)


        """test"""
        # self.button_test = PyPushButton(
        #     text="网站内容爬取",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"],
        #     border_width=2,
        #     border_style="solid",
        #     border_color="#568AF2",
        #     border_color_hover="#72A2FF",  # 悬停时边框变亮
        #     border_color_pressed="#3B5B92"  # 按下时边框变暗
        # )
        # self.button_test.setMinimumHeight(30)
        # self.ui.load_pages.scan_plugins_layout_row3.addWidget(self.button_test)