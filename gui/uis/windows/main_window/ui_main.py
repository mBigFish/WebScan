# ///////////////////////////////////////////////////////////////
#
# 作者：WANDERSON M.PIMENTA
# 项目使用工具：Qt Designer 和 PySide6
# 版本：1.0.0
#
# 该项目可以自由使用，但仅在Python脚本中保留相应的版权声明，
# 任何可视化界面（GUI）中的信息都可以修改，不会产生任何法律后果。
#
# 如果您打算将产品用于商业用途，Qt许可证有限制，
# 我建议您在官方网页上阅读相关条款：
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# 导入包和模块
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions

# 导入Qt核心模块
# ///////////////////////////////////////////////////////////////
from qt_core import *

# 导入设置
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# 导入主题颜色
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# 导入PyOneDark小部件
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# 导入主窗口设置
# ///////////////////////////////////////////////////////////////
# from .setup_main_window import *

# 导入主窗口页面和应用的侧边框
# ///////////////////////////////////////////////////////////////
from gui.uis.pages.ui_main_pages import Ui_MainPages

# 右侧列
# ///////////////////////////////////////////////////////////////
from gui.uis.columns.ui_right_column import Ui_RightColumn

# 版权信息
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_credits_bar.py_credits import PyCredits


# Py窗口
# ///////////////////////////////////////////////////////////////
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # 加载设置
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # 加载主题颜色
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # 设置初始参数
        parent.resize(self.settings["startup_size"][0], self.settings["startup_size"][1])
        parent.setMinimumSize(self.settings["minimum_size"][0], self.settings["minimum_size"][1])

        # 设置中央小部件
        # 添加中央小部件到应用程序
        # ///////////////////////////////////////////////////////////////
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(f'''
            font: {self.settings["font"]["text_size"]}pt "{self.settings["font"]["family"]}";
            color: {self.themes["app_color"]["text_foreground"]};
        ''')
        self.central_widget_layout = QVBoxLayout(self.central_widget)
        if self.settings["custom_title_bar"]:
            self.central_widget_layout.setContentsMargins(10, 10, 10, 10)
        else:
            self.central_widget_layout.setContentsMargins(0, 0, 0, 0)

        # 加载Py窗口自定义小部件
        # 将所有小部件添加到PyWindow "layout" 中
        # ///////////////////////////////////////////////////////////////
        self.window = PyWindow(
            parent,
            bg_color=self.themes["app_color"]["bg_one"],
            border_color=self.themes["app_color"]["bg_two"],
            text_color=self.themes["app_color"]["text_foreground"]
        )

        # 如果禁用自定义标题栏
        if not self.settings["custom_title_bar"]:
            self.window.set_stylesheet(border_radius=0, border_size=0)

        # 将PyWindow添加到中央小部件
        self.central_widget_layout.addWidget(self.window)

        # 添加左侧菜单框架
        # 在此添加自定义左侧菜单栏
        # ///////////////////////////////////////////////////////////////
        left_menu_margin = self.settings["left_menu_content_margins"]
        left_menu_minimum = self.settings["lef_menu_size"]["minimum"]
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setMaximumSize(left_menu_minimum + (left_menu_margin * 2), 17280)
        self.left_menu_frame.setMinimumSize(left_menu_minimum + (left_menu_margin * 2), 0)

        # 左侧菜单布局
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(
            left_menu_margin,
            left_menu_margin,
            left_menu_margin,
            left_menu_margin
        )

        # 添加左侧菜单
        # 在此添加自定义左侧菜单
        # ///////////////////////////////////////////////////////////////
        self.left_menu = PyLeftMenu(
            parent=self.left_menu_frame,
            app_parent=self.central_widget,  # 用于提示框父容器
            dark_one=self.themes["app_color"]["dark_one"],
            dark_three=self.themes["app_color"]["dark_three"],
            dark_four=self.themes["app_color"]["dark_four"],
            bg_one=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            text_active=self.themes["app_color"]["text_active"]
        )
        self.left_menu_layout.addWidget(self.left_menu)

        # 添加左列
        # 在此添加具有堆叠小部件的左列
        # ///////////////////////////////////////////////////////////////
        self.left_column_frame = QFrame()
        self.left_column_frame.setMaximumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setStyleSheet(f"background: {self.themes['app_color']['bg_two']}")

        # 为左列添加布局
        self.left_column_layout = QVBoxLayout(self.left_column_frame)
        self.left_column_layout.setContentsMargins(0, 0, 0, 0)

        # 添加自定义左列小部件
        self.left_column = PyLeftColumn(
            parent,
            app_parent=self.central_widget,
            text_title="Settings Left Frame",
            text_title_size=self.settings["font"]["title_size"],
            text_title_color=self.themes['app_color']['text_foreground'],
            icon_path=Functions.set_svg_icon("icon_settings.svg"),
            dark_one=self.themes['app_color']['dark_one'],
            bg_color=self.themes['app_color']['bg_three'],
            btn_color=self.themes['app_color']['bg_three'],
            btn_color_hover=self.themes['app_color']['bg_two'],
            btn_color_pressed=self.themes['app_color']['bg_one'],
            icon_color=self.themes['app_color']['icon_color'],
            icon_color_hover=self.themes['app_color']['icon_hover'],
            context_color=self.themes['app_color']['context_color'],
            icon_color_pressed=self.themes['app_color']['icon_pressed'],
            icon_close_path=Functions.set_svg_icon("icon_close.svg")
        )
        self.left_column_layout.addWidget(self.left_column)

        # 添加右侧小部件
        # 在此添加右侧小部件
        # ///////////////////////////////////////////////////////////////
        self.right_app_frame = QFrame()

        # 为右侧应用程序添加布局
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(3, 3, 3, 3)
        self.right_app_layout.setSpacing(6)

        # 添加标题栏框架
        # ///////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # 将自定义标题栏添加到布局
        self.title_bar = PyTitleBar(
            parent,
            logo_width=100,
            app_parent=self.central_widget,
            logo_image="logo_top_100x22.svg",
            bg_color=self.themes["app_color"]["bg_two"],
            div_color=self.themes["app_color"]["bg_three"],
            btn_bg_color=self.themes["app_color"]["bg_two"],
            btn_bg_color_hover=self.themes["app_color"]["bg_three"],
            btn_bg_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            radius=8,
            font_family=self.settings["font"]["family"],
            title_size=self.settings["font"]["title_size"],
            is_custom_title_bar=self.settings["custom_title_bar"]
        )
        self.title_bar_layout.addWidget(self.title_bar)

        # 添加内容区域
        # ///////////////////////////////////////////////////////////////
        self.content_area_frame = QFrame()

        # 创建布局
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)

        # 左侧内容
        self.content_area_left_frame = QFrame()

        # 导入主页面到内容区域
        self.load_pages = Ui_MainPages()
        self.load_pages.setupUi(self.content_area_left_frame)

        # 右侧栏
        self.right_column_frame = QFrame()
        self.right_column_frame.setMinimumWidth(self.settings["right_column_size"]["minimum"])
        self.right_column_frame.setMaximumWidth(self.settings["right_column_size"]["minimum"])

        # 导入右侧列
        # ///////////////////////////////////////////////////////////////
        self.content_area_right_layout = QVBoxLayout(self.right_column_frame)
        self.content_area_right_layout.setContentsMargins(5, 5, 5, 5)
        self.content_area_right_layout.setSpacing(0)

        # 右侧背景
        self.content_area_right_bg_frame = QFrame()
        self.content_area_right_bg_frame.setObjectName("content_area_right_bg_frame")
        self.content_area_right_bg_frame.setStyleSheet(f'''
        #content_area_right_bg_frame {{
            border-radius: 8px;
            background-color: {self.themes["app_color"]["bg_two"]};
        }}
        ''')

        # 添加背景
        self.content_area_right_layout.addWidget(self.content_area_right_bg_frame)

        # 将右侧页面添加到右侧列
        self.right_column = Ui_RightColumn()
        self.right_column.setupUi(self.content_area_right_bg_frame)

        # 添加到布局
        self.content_area_layout.addWidget(self.content_area_left_frame)
        self.content_area_layout.addWidget(self.right_column_frame)

        # 版权信息 / 底部应用框架
        # ///////////////////////////////////////////////////////////////
        self.credits_frame = QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)

        # 创建布局
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setContentsMargins(0, 0, 0, 0)

        # 添加自定义版权信息小部件
        self.credits = PyCredits(
            bg_two=self.themes["app_color"]["bg_two"],
            copyright=self.settings["copyright"],
            version=self.settings["version"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            text_description_color=self.themes["app_color"]["text_description"]
        )

        # 添加到布局
        self.credits_layout.addWidget(self.credits)

        # 将小部件添加到右侧布局
        # ///////////////////////////////////////////////////////////////
        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        self.right_app_layout.addWidget(self.credits_frame)

        # 将小部件添加到 "PyWindow"
        # 在此添加您的自定义小部件或默认小部件
        # ///////////////////////////////////////////////////////////////
        self.window.layout.addWidget(self.left_menu_frame)
        self.window.layout.addWidget(self.left_column_frame)
        self.window.layout.addWidget(self.right_app_frame)

        # 添加中央小部件并设置内容边距
        # ///////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_widget)
