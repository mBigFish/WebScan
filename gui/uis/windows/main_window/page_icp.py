from threading import Thread

from PySide6.QtGui import QMovie, Qt

from gui.core.json_themes import Themes
from gui.uis.windows.main_window import UI_MainWindow
from gui.widgets import *
from core.icp.GetIcp import ICP

class UiPageIcp:
    """废物函数，只是为了可以让下面函数给出提示"""
    def __init__(self):
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    def setup_ui(self):
        def __set_border():
            # icp备案结果
            self.ui.load_pages.lable_icp_result_domain.setStyleSheet("""
                             border: 1px solid blue;         /* 设置边框颜色为蓝色，宽度为3px */
                             border-radius: 20px;            /* 设置圆角边框 */
                             padding: 10px;                  /* 设置内边距 */
                             font-size: 16px;                /* 设置字体大小 */
                         """)

            self.ui.load_pages.lable_icp_result_unitName.setStyleSheet("""
                             border: 1px solid red;         /* 设置边框颜色为蓝色，宽度为3px */
                             border-radius: 20px;            /* 设置圆角边框 */
                             padding: 10px;                  /* 设置内边距 */
                             font-size: 16px;                /* 设置字体大小 */
                         """)

            self.ui.load_pages.lable_icp_result_serviceLicence.setStyleSheet("""
                             border: 1px solid yellow;         /* 设置边框颜色为蓝色，宽度为3px */
                             border-radius: 20px;            /* 设置圆角边框 */
                             padding: 10px;                  /* 设置内边距 */
                             font-size: 16px;                /* 设置字体大小 */
                         """)

            self.ui.load_pages.lable_icp_result_contentTypeName.setStyleSheet("""
                             border: 1px solid black;         /* 设置边框颜色为蓝色，宽度为3px */
                             border-radius: 20px;            /* 设置圆角边框 */
                             padding: 10px;                  /* 设置内边距 */
                             font-size: 16px;                /* 设置字体大小 */
                         """)

            self.ui.load_pages.lable_icp_result_mainLicence.setStyleSheet("""
                             border: 1px solid purple;         /* 设置边框颜色为蓝色，宽度为3px */
                             border-radius: 20px;            /* 设置圆角边框 */
                             padding: 10px;                  /* 设置内边距 */
                             font-size: 16px;                /* 设置字体大小 */
                         """)

            self.ui.load_pages.lable_icp_result_updateRecordTime.setStyleSheet("""
                             border: 1px solid green;         /* 设置边框颜色为蓝色，宽度为3px */
                             border-radius: 20px;            /* 设置圆角边框 */
                             padding: 10px;                  /* 设置内边距 */
                             font-size: 16px;                /* 设置字体大小 */
                         """)

            self.ui.load_pages.lable_icp_result_natureName.setStyleSheet("""
                             border: 1px solid white;         /* 设置边框颜色为蓝色，宽度为3px */
                             border-radius: 20px;            /* 设置圆角边框 */
                             padding: 10px;                  /* 设置内边距 */
                             font-size: 16px;                /* 设置字体大小 */
                         """)

        def __thread_button_clicked(btn_name):
            # thread = Thread(target=__test)
            # thread.start()

            thread = Thread(target=__button_clicked, args=(btn_name,))
            thread.start()

        def __button_clicked(btn_name):
            if btn_name == "push_button_icp":
                self.push_button_icp.setEnabled(False)
                self.push_button_icp.setText("正在查询")
                self.ui.load_pages.lable_icp_row3.setText("正在查询....")

                self.ui.load_pages.lable_icp_result_mainLicence.clear()
                self.ui.load_pages.lable_icp_result_updateRecordTime.clear()
                self.ui.load_pages.lable_icp_result_unitName.clear()
                self.ui.load_pages.lable_icp_result_natureName.clear()
                self.ui.load_pages.lable_icp_result_serviceLicence.clear()
                self.ui.load_pages.lable_icp_result_domain.clear()
                self.ui.load_pages.lable_icp_result_contentTypeName.clear()
                domain = self.line_edit_icp_domain.text()
                a = ICP()
                icp_resp = a.main(domain)
                if icp_resp["code"] == 200:
                    if len(icp_resp["params"]["list"]) != 0:
                        self.ui.load_pages.lable_icp_row3.setText("查询成功")
                        self.ui.load_pages.lable_icp_result_mainLicence.setText(
                            str(icp_resp["params"]["list"][0]["mainLicence"]))
                        self.ui.load_pages.lable_icp_result_updateRecordTime.setText(
                            str(icp_resp["params"]["list"][0]["updateRecordTime"]))
                        self.ui.load_pages.lable_icp_result_unitName.setText(
                            str(icp_resp["params"]["list"][0]["unitName"]))
                        self.ui.load_pages.lable_icp_result_natureName.setText(
                            str(icp_resp["params"]["list"][0]["natureName"]))
                        self.ui.load_pages.lable_icp_result_serviceLicence.setText(
                            str(icp_resp["params"]["list"][0]["serviceLicence"]))
                        self.ui.load_pages.lable_icp_result_domain.setText(str(icp_resp["params"]["list"][0]["domain"]))
                        self.ui.load_pages.lable_icp_result_contentTypeName.setText(
                            str(icp_resp["params"]["list"][0]["contentTypeName"]))
                    else:
                        self.ui.load_pages.lable_icp_row3.setText(f"查询成功，当前域名未备案")

                else:
                    self.ui.load_pages.lable_icp_row3.setText(f"查询失败，原因：{icp_resp['msg']}，请再试一次！")
                self.push_button_icp.setEnabled(True)
                self.push_button_icp.setText("查询")

        self.themes = Themes().items
        # icp备案域名输入框
        self.line_edit_icp_domain = PyLineEdit(

            text="",
            radius=8,
            border_size=2,
            color="#FFFFFF",
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            context_color="#00ABE8"
        )
        self.line_edit_icp_domain.setPlaceholderText("请输入域名...")
        self.line_edit_icp_domain.setMaximumWidth(800)
        self.line_edit_icp_domain.setMinimumHeight(40)

        # icp备案确认按钮
        self.push_button_icp = PyPushButton(
            text="查询",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_icp.setMaximumHeight(40)
        self.push_button_icp.setMaximumWidth(200)

        self.ui.load_pages.icp_row1_layout.addWidget(self.line_edit_icp_domain)
        self.ui.load_pages.icp_row1_layout.addWidget(self.push_button_icp)
        self.push_button_icp.clicked.connect(lambda: __thread_button_clicked("push_button_icp"))

        # icp备案结果
        __set_border()


