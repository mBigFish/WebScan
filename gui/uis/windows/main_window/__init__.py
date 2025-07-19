from threading import Thread

# 导入包和模块
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
# from .functions_main_window import *
import sys
import os

# 导入Qt核心模块
# ///////////////////////////////////////////////////////////////
from qt_core import *

# 导入设置
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# 导入主题颜色
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# import models

# 导入Py One Dark小部件
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
# from . import page_scan

# 加载主界面
# ///////////////////////////////////////////////////////////////
from .ui_main import *

# 主函数
# ///////////////////////////////////////////////////////////////
from .functions_main_window import MainFunctions


# Py窗口
# ///////////////////////////////////////////////////////////////

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
# from . ui_main import UI_MainWindow

# SETUP MAIN WINDOW
# ///////////////////////////////////////////////////////////////
# from . setup_main_window import SetupMainWindow
from . page_icp import UiPageIcp
from .page_home import UiPageHome
from . page_test import UiPageTest
from . page_scan import UiPageScan

class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # 设置主窗口
        # 从 "gui\uis\main_window\ui_main.py" 加载小部件
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # 添加左侧菜单
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "程序主页",
            "btn_tooltip": "主页",
            "show_top": True,
            "is_active": True
        },
        # {
        #     "btn_icon": "icon_widgets.svg",
        #     "btn_id": "btn_widgets",
        #     "btn_text": "显示自定义小部件",
        #     "btn_tooltip": "显示自定义小部件",
        #     "show_top": True,
        #     "is_active": False
        # },
        {
            "btn_icon": "icon_emoticons.svg",
            "btn_id": "btn_get_icp",
            "btn_text": "备案查询",
            "btn_tooltip": "备案查询",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_signal.svg",
            "btn_id": "btn_web_scan",
            "btn_text": "网站检测",
            "btn_tooltip": "网站检测",
            "show_top": True,
            "is_active": False
        },
        # {
        #     "btn_icon": "icon_folder_open.svg",
        #     "btn_id": "btn_open_file",
        #     "btn_text": "打开文件",
        #     "btn_tooltip": "打开文件",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_save.svg",
        #     "btn_id": "btn_save",
        #     "btn_text": "保存文件",
        #     "btn_tooltip": "保存文件",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_info.svg",
        #     "btn_id": "btn_info",
        #     "btn_text": "信息",
        #     "btn_tooltip": "打开信息",
        #     "show_top": False,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_settings.svg",
        #     "btn_id": "btn_settings",
        #     "btn_text": "设置",
        #     "btn_tooltip": "打开设置",
        #     "show_top": False,
        #     "is_active": False
        # }
    ]

    # 添加标题栏菜单
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "还没有写哦",
            "is_active": False
        }
    ]

    # 设置自定义按钮的处理函数
    # 获取点击按钮时的发送者 (sender) 函数
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # 使用自定义参数设置主窗口
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        page_icp.UiPageIcp.setup_ui(self)
        page_home.UiPageHome.setup_ui(self)
        page_test.UiPageTest.setup_ui(self)
        page_scan.UiPageScan.setup_ui(self)

        # 应用程序标题
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # 移除标题栏
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # 添加窗口调整手柄
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # 左侧菜单 / 获取点击/释放信号
        # ///////////////////////////////////////////////////////////////
        # 添加菜单
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # 设置信号
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # 标题栏 / 添加额外的按钮
        # ///////////////////////////////////////////////////////////////
        # 添加菜单
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # 设置信号
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # 添加标题
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDarkaaa")

        # 左列设置信号
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # 设置初始页面 / 设置左右列菜单
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "设置左列",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # 示例自定义小部件
        # 这里添加了使用Qt Designer创建的自定义小部件到页面和列中。
        # 这是一个示例，创建应用程序时应删除它。
        #
        # 加载页面、左列和右列的对象
        # 你可以通过下面的对象访问Qt Designer项目中的对象：
        #
        # <OBJECTS>
        # 左列: self.ui.left_column.menus
        # 右列: self.ui.right_column
        # 加载页面: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # 加载设置
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # 加载主题颜色
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # 左列
        # ///////////////////////////////////////////////////////////////

        # 按钮 1
        self.left_btn_1 = PyPushButton(
            text="按钮 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # 按钮 2
        self.left_btn_2 = PyPushButton(
            text="带图标的按钮",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # 按钮 3 - 默认 QPushButton
        self.left_btn_3 = QPushButton("默认 QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # 页面
        # ///////////////////////////////////////////////////////////////




        # 右侧列
        # ///////////////////////////////////////////////////////////////

        # 按钮 1
        self.right_btn_1 = PyPushButton(
            text="显示菜单 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # 按钮 2
        self.right_btn_2 = PyPushButton(
            text="显示菜单 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # 结束 - 自定义控件示例
        # ///////////////////////////////////////////////////////////////

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

