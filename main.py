# ///////////////////////////////////////////////////////////////
#
# 作者: WANDERSON M.PIMENTA
# 项目制作工具: Qt Designer 和 PySide6
# 版本: 1.0.0
#
# 该项目可以自由使用，只要在Python脚本中保留相应的版权声明，
# 可修改任何视觉界面（GUI）中的信息，不会产生任何法律责任。
#
# 如果你想将产品用于商业用途，Qt许可协议有一定的限制，
# 我建议你阅读Qt官方许可条款：
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# 导入包和模块
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# 导入Qt核心
# ///////////////////////////////////////////////////////////////
from qt_core import *

# 导入设置
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# 导入Py One Dark窗口
# ///////////////////////////////////////////////////////////////
# 主窗口
from gui.uis.windows.main_window import *

# 导入Py One Dark控件
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# 调整Qt字体DPI以适应高DPI和4K显示器
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"


# 如果是4K显示器，启用 'os.environ["QT_SCALE_FACTOR"] = "2"'

# 主窗口
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗口
        # 从 "gui\uis\main_window\ui_main.py" 加载控件
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # 加载设置
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # 设置主窗口
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # 显示/隐藏调整大小的拖动手柄
        SetupMainWindow.setup_gui(self)
        # UiPageIcp.setupUi(self)
        # testclass.test_setup_gui(self)
        # a = SetupMainWindow()
        # a.setup_gui()

        # 显示主窗口
        # ///////////////////////////////////////////////////////////////
        self.show()

    # 左侧菜单按钮被点击时
    # 根据按钮的对象名称/按钮ID执行功能
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # 获取点击的按钮
        btn = SetupMainWindow.setup_btns(self)

        # 如果点击的是"btn_close_left_column"，则取消选择
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # 获取标题栏按钮并重置活动状态
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        # 左侧菜单
        # ///////////////////////////////////////////////////////////////

        # 主页面按钮
        if btn.objectName() == "btn_home":
            # 选择菜单
            self.ui.left_menu.select_only_one(btn.objectName())

            # 加载页面 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # 控件按钮
        if btn.objectName() == "btn_widgets":
            # 选择菜单
            self.ui.left_menu.select_only_one(btn.objectName())

            # 加载页面 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # 备案查询
        if btn.objectName() == "btn_get_icp":
            # 选择菜单
            self.ui.left_menu.select_only_one(btn.objectName())

            # 加载页面 3
            MainFunctions.set_page(self, self.ui.load_pages.page_icp)

        # 网站扫描
        if btn.objectName() == "btn_web_scan":
            # 选择菜单
            self.ui.left_menu.select_only_one(btn.objectName())

            # 加载页面 3
            MainFunctions.set_page(self, self.ui.load_pages.page_scan)


        # 底部信息
        if btn.objectName() == "btn_info":
            # 检查左侧栏是否可见
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # 显示/隐藏
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # 显示/隐藏
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # 更改左侧栏菜单
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="信息标签",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # 设置菜单左侧
        # if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
        #     # 检查左侧栏是否可见
        #     if not MainFunctions.left_column_is_visible(self):
        #         # 显示/隐藏
        #         MainFunctions.toggle_left_column(self)
        #         self.ui.left_menu.select_only_one_tab(btn.objectName())
        #     else:
        #         if btn.objectName() == "btn_close_left_column":
        #             self.ui.left_menu.deselect_all_tab()
        #             # 显示/隐藏
        #             MainFunctions.toggle_left_column(self)
        #         self.ui.left_menu.select_only_one_tab(btn.objectName())

            # # 更改左侧栏菜单
            # if btn.objectName() != "btn_close_left_column":
            #     MainFunctions.set_left_column_menu(
            #         self,
            #         menu=self.ui.left_column.menus.menu_1,
            #         title="设置左侧栏",
            #         icon_path=Functions.set_svg_icon("icon_settings.svg")
            #     )

        # 标题栏菜单
        # ///////////////////////////////////////////////////////////////

        # 设置标题栏按钮
        # if btn.objectName() == "btn_top_settings":
        #     # 切换激活状态
        #     if not MainFunctions.right_column_is_visible(self):
        #         btn.set_active(True)
        #
        #         # 显示/隐藏
        #         MainFunctions.toggle_right_column(self)
        #     else:
        #         btn.set_active(False)
        #
        #         # 显示/隐藏
        #         MainFunctions.toggle_right_column(self)
        #
        #     # 获取左侧菜单按钮
        #     top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
        #     top_settings.set_active_tab(False)

            # 调试输出
        print(f"按钮 {btn.objectName()} 被点击!")

    # 左侧菜单按钮释放时
    # 根据按钮的对象名称/按钮ID执行功能
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # 获取点击的按钮
        btn = SetupMainWindow.setup_btns(self)

        # 调试输出
        print(f"按钮 {btn.objectName()} 被释放!")

    # 窗口大小调整事件
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # 鼠标点击事件
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # 设置窗口拖动位置
        self.dragPos = event.globalPosition().toPoint()


# 设置启动时的参数
# 设置初始类以及QApplication类的其他参数
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # 应用程序
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # 执行应用
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
