# ///////////////////////////////////////////////////////////////
#
# 作者：WANDERSON M.PIMENTA
# 项目使用：Qt Designer 和 PySide6 制作
# 版本：1.0.0
#
# 本项目可以自由使用，但仅限在 Python 脚本中保留相应的版权声明，
# 视觉界面（GUI）中的任何信息可以根据需要修改，不受任何限制。
#
# 如果您想将产品用于商业用途，请注意 Qt 许可的相关限制，
# 我建议您阅读官方文档：https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# 导入包和模块
# ///////////////////////////////////////////////////////////////
import sys

# 导入 QT 核心
# ///////////////////////////////////////////////////////////////
from qt_core import *

# 加载主 UI
# ///////////////////////////////////////////////////////////////
from .ui_main import *


# 功能函数
class MainFunctions:
    def __init__(self):
        super().__init__()
        # 设置主窗口
        # 从 "gui\uis\main_window\ui_main.py" 加载小部件
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # 设置主窗口页面
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.ui.load_pages.pages.setCurrentWidget(page)

    # 设置左侧栏页面
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(
            self,
            menu,
            title,
            icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    # 返回左侧栏是否可见
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # 返回右侧栏是否可见
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # 设置右侧栏页面
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)

    # 通过对象名称获取标题按钮
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    # 通过对象名称获取左侧菜单按钮
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)

    # 左右栏的显示/隐藏
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        # 获取当前列的宽度
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        # 获取当前列的宽度
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_left = self.ui.settings["left_column_size"]["minimum"]
        maximum_left = self.ui.settings["left_column_size"]["maximum"]
        minimum_right = self.ui.settings["right_column_size"]["minimum"]
        maximum_right = self.ui.settings["right_column_size"]["maximum"]

        # 检查左侧列的值
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # 检查右侧列的值
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right

            # 左侧框动画
        self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # 右侧框动画
        self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # 动画分组
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

