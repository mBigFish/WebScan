# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesvGgVKr.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QScrollArea, QSizePolicy,
    QSpinBox, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(920, 734)
        self.verticalLayout_2 = QVBoxLayout(MainPages)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color:#2c313c")
        self.page_scan = QWidget()
        self.page_scan.setObjectName(u"page_scan")
        self.page_scan_layout = QHBoxLayout(self.page_scan)
        self.page_scan_layout.setObjectName(u"page_scan_layout")
        self.scan_left_farme = QFrame(self.page_scan)
        self.scan_left_farme.setObjectName(u"scan_left_farme")
        self.scan_left_farme.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_left_farme.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.scan_left_farme)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scan_left_up_farme = QFrame(self.scan_left_farme)
        self.scan_left_up_farme.setObjectName(u"scan_left_up_farme")
        self.scan_left_up_farme.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_left_up_farme.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.scan_left_up_farme)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scan_plugins_groupBox = QGroupBox(self.scan_left_up_farme)
        self.scan_plugins_groupBox.setObjectName(u"scan_plugins_groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.scan_plugins_groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scan_plugins_farme_row1 = QFrame(self.scan_plugins_groupBox)
        self.scan_plugins_farme_row1.setObjectName(u"scan_plugins_farme_row1")
        self.scan_plugins_farme_row1.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_plugins_farme_row1.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_plugins_layout_row1 = QHBoxLayout(self.scan_plugins_farme_row1)
        self.scan_plugins_layout_row1.setObjectName(u"scan_plugins_layout_row1")

        self.verticalLayout_8.addWidget(self.scan_plugins_farme_row1)

        self.scan_plugins_farme_row2 = QFrame(self.scan_plugins_groupBox)
        self.scan_plugins_farme_row2.setObjectName(u"scan_plugins_farme_row2")
        self.scan_plugins_farme_row2.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_plugins_farme_row2.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_plugins_layout_row2 = QHBoxLayout(self.scan_plugins_farme_row2)
        self.scan_plugins_layout_row2.setObjectName(u"scan_plugins_layout_row2")

        self.verticalLayout_8.addWidget(self.scan_plugins_farme_row2)

        self.scan_plugins_farme_row3 = QFrame(self.scan_plugins_groupBox)
        self.scan_plugins_farme_row3.setObjectName(u"scan_plugins_farme_row3")
        self.scan_plugins_farme_row3.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_plugins_farme_row3.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_plugins_layout_row3 = QHBoxLayout(self.scan_plugins_farme_row3)
        self.scan_plugins_layout_row3.setObjectName(u"scan_plugins_layout_row3")

        self.verticalLayout_8.addWidget(self.scan_plugins_farme_row3)


        self.horizontalLayout_3.addWidget(self.scan_plugins_groupBox)

        self.scan_params_groupBox = QGroupBox(self.scan_left_up_farme)
        self.scan_params_groupBox.setObjectName(u"scan_params_groupBox")
        self.scan_params_groupBox.setMinimumSize(QSize(0, 300))
        self.verticalLayout_9 = QVBoxLayout(self.scan_params_groupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scan_params_farme_row1 = QFrame(self.scan_params_groupBox)
        self.scan_params_farme_row1.setObjectName(u"scan_params_farme_row1")
        self.scan_params_farme_row1.setMinimumSize(QSize(0, 70))
        self.scan_params_farme_row1.setStyleSheet(u"border: 1px solid \"#568AF2\";         /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u84dd\u8272\uff0c\u5bbd\u5ea6\u4e3a3px */\n"
"border-radius: 20px;            /* \u8bbe\u7f6e\u5706\u89d2\u8fb9\u6846 */\n"
"padding: 1px;                  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */")
        self.scan_params_farme_row1.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_params_farme_row1.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_params_layout_row1 = QHBoxLayout(self.scan_params_farme_row1)
        self.scan_params_layout_row1.setObjectName(u"scan_params_layout_row1")
        self.label_2 = QLabel(self.scan_params_farme_row1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 40))
        self.label_2.setMaximumSize(QSize(90, 40))
        self.label_2.setStyleSheet(u"border: 1px solid \"#408ab4\"; \n"
"border-radius: 20px; \n"
"padding: 5px;")

        self.scan_params_layout_row1.addWidget(self.label_2)

        self.scan_params_farme_row1_1 = QFrame(self.scan_params_farme_row1)
        self.scan_params_farme_row1_1.setObjectName(u"scan_params_farme_row1_1")
        self.scan_params_farme_row1_1.setStyleSheet(u"border: none;         /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u84dd\u8272\uff0c\u5bbd\u5ea6\u4e3a3px */\\nborder-radius: 20px;            /* \u8bbe\u7f6e\u5706\u89d2\u8fb9\u6846 */\\npadding: 1px;                  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */")
        self.scan_params_farme_row1_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_params_farme_row1_1.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_params_layout_row1_1 = QHBoxLayout(self.scan_params_farme_row1_1)
        self.scan_params_layout_row1_1.setObjectName(u"scan_params_layout_row1_1")

        self.scan_params_layout_row1.addWidget(self.scan_params_farme_row1_1)


        self.verticalLayout_9.addWidget(self.scan_params_farme_row1)

        self.scan_params_farme_row2 = QFrame(self.scan_params_groupBox)
        self.scan_params_farme_row2.setObjectName(u"scan_params_farme_row2")
        self.scan_params_farme_row2.setMinimumSize(QSize(0, 70))
        self.scan_params_farme_row2.setStyleSheet(u"border: 1px solid \"#568AF2\";         /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u84dd\u8272\uff0c\u5bbd\u5ea6\u4e3a3px */\n"
"border-radius: 20px;            /* \u8bbe\u7f6e\u5706\u89d2\u8fb9\u6846 */\n"
"padding: 1px;                  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */")
        self.scan_params_farme_row2.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_params_farme_row2.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_params_layout_row2 = QHBoxLayout(self.scan_params_farme_row2)
        self.scan_params_layout_row2.setObjectName(u"scan_params_layout_row2")
        self.label_3 = QLabel(self.scan_params_farme_row2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 40))
        self.label_3.setMaximumSize(QSize(90, 40))
        self.label_3.setStyleSheet(u"border: 1px solid \"#408ab4\"; \n"
"border-radius: 20px; \n"
"padding: 5px;")

        self.scan_params_layout_row2.addWidget(self.label_3)

        self.scan_params_farme_row2_1 = QFrame(self.scan_params_farme_row2)
        self.scan_params_farme_row2_1.setObjectName(u"scan_params_farme_row2_1")
        self.scan_params_farme_row2_1.setStyleSheet(u"border: none;         /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u84dd\u8272\uff0c\u5bbd\u5ea6\u4e3a3px */\\nborder-radius: 20px;            /* \u8bbe\u7f6e\u5706\u89d2\u8fb9\u6846 */\\npadding: 1px;                  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */")
        self.scan_params_farme_row2_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_params_farme_row2_1.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_params_layout_row2_1 = QHBoxLayout(self.scan_params_farme_row2_1)
        self.scan_params_layout_row2_1.setObjectName(u"scan_params_layout_row2_1")

        self.scan_params_layout_row2.addWidget(self.scan_params_farme_row2_1)


        self.verticalLayout_9.addWidget(self.scan_params_farme_row2)

        self.scan_params_farme_row3 = QFrame(self.scan_params_groupBox)
        self.scan_params_farme_row3.setObjectName(u"scan_params_farme_row3")
        self.scan_params_farme_row3.setMinimumSize(QSize(0, 70))
        self.scan_params_farme_row3.setStyleSheet(u"border: 1px solid \"#568AF2\";         /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u84dd\u8272\uff0c\u5bbd\u5ea6\u4e3a3px */\n"
"border-radius: 20px;            /* \u8bbe\u7f6e\u5706\u89d2\u8fb9\u6846 */\n"
"padding: 1px;                  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */")
        self.scan_params_farme_row3.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_params_farme_row3.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_params_layout_row3 = QHBoxLayout(self.scan_params_farme_row3)
        self.scan_params_layout_row3.setObjectName(u"scan_params_layout_row3")
        self.label_4 = QLabel(self.scan_params_farme_row3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 40))
        self.label_4.setMaximumSize(QSize(90, 40))
        self.label_4.setStyleSheet(u"border: 1px solid \"#408ab4\"; \n"
"border-radius: 20px; \n"
"padding: 5px;")

        self.scan_params_layout_row3.addWidget(self.label_4)

        self.scan_params_farme_row3_1 = QFrame(self.scan_params_farme_row3)
        self.scan_params_farme_row3_1.setObjectName(u"scan_params_farme_row3_1")
        self.scan_params_farme_row3_1.setStyleSheet(u"border: none;         /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u84dd\u8272\uff0c\u5bbd\u5ea6\u4e3a3px */\\nborder-radius: 20px;            /* \u8bbe\u7f6e\u5706\u89d2\u8fb9\u6846 */\\npadding: 1px;                  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */")
        self.scan_params_farme_row3_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_params_farme_row3_1.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_params_layout_row3_1 = QHBoxLayout(self.scan_params_farme_row3_1)
        self.scan_params_layout_row3_1.setObjectName(u"scan_params_layout_row3_1")

        self.scan_params_layout_row3.addWidget(self.scan_params_farme_row3_1)


        self.verticalLayout_9.addWidget(self.scan_params_farme_row3)

        self.scan_params_farme_row4 = QFrame(self.scan_params_groupBox)
        self.scan_params_farme_row4.setObjectName(u"scan_params_farme_row4")
        self.scan_params_farme_row4.setMinimumSize(QSize(0, 70))
        self.scan_params_farme_row4.setStyleSheet(u"border: 1px solid \"#568AF2\";         /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u4e3a\u84dd\u8272\uff0c\u5bbd\u5ea6\u4e3a3px */\n"
"border-radius: 20px;            /* \u8bbe\u7f6e\u5706\u89d2\u8fb9\u6846 */\n"
"padding: 5px;                  /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */")
        self.scan_params_farme_row4.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_params_farme_row4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.scan_params_farme_row4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.scan_params_farme_row4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 40))
        self.label_5.setMaximumSize(QSize(90, 40))
        self.label_5.setStyleSheet(u"border: 1px solid \"#408ab4\"; \n"
"border-radius: 20px; \n"
"padding: 5px;")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_hint = QLabel(self.scan_params_farme_row4)
        self.label_hint.setObjectName(u"label_hint")
        self.label_hint.setStyleSheet(u"border: 1px solid \"#b292ea\"; \n"
"border-radius: 20px; \n"
"padding: 5px;")
        self.label_hint.setTextFormat(Qt.TextFormat.AutoText)

        self.horizontalLayout_4.addWidget(self.label_hint)


        self.verticalLayout_9.addWidget(self.scan_params_farme_row4)


        self.horizontalLayout_3.addWidget(self.scan_params_groupBox)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_6.addWidget(self.scan_left_up_farme)

        self.scan_left_down_farme = QFrame(self.scan_left_farme)
        self.scan_left_down_farme.setObjectName(u"scan_left_down_farme")
        self.scan_left_down_farme.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_left_down_farme.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_left_down_layout = QHBoxLayout(self.scan_left_down_farme)
        self.scan_left_down_layout.setObjectName(u"scan_left_down_layout")

        self.verticalLayout_6.addWidget(self.scan_left_down_farme)


        self.page_scan_layout.addWidget(self.scan_left_farme)

        self.scan_right_farme = QFrame(self.page_scan)
        self.scan_right_farme.setObjectName(u"scan_right_farme")
        self.scan_right_farme.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_right_farme.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.scan_right_farme)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scan_right_farme_row1 = QFrame(self.scan_right_farme)
        self.scan_right_farme_row1.setObjectName(u"scan_right_farme_row1")
        self.scan_right_farme_row1.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_right_farme_row1.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_right_layout_row1 = QHBoxLayout(self.scan_right_farme_row1)
        self.scan_right_layout_row1.setObjectName(u"scan_right_layout_row1")

        self.verticalLayout_10.addWidget(self.scan_right_farme_row1)

        self.scan_right_farme_row2 = QFrame(self.scan_right_farme)
        self.scan_right_farme_row2.setObjectName(u"scan_right_farme_row2")
        self.scan_right_farme_row2.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_right_farme_row2.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_right_layout_row2 = QVBoxLayout(self.scan_right_farme_row2)
        self.scan_right_layout_row2.setObjectName(u"scan_right_layout_row2")

        self.verticalLayout_10.addWidget(self.scan_right_farme_row2)

        self.scan_right_farme_row3 = QFrame(self.scan_right_farme)
        self.scan_right_farme_row3.setObjectName(u"scan_right_farme_row3")
        self.scan_right_farme_row3.setFrameShape(QFrame.Shape.StyledPanel)
        self.scan_right_farme_row3.setFrameShadow(QFrame.Shadow.Raised)
        self.scan_right_layout_row3 = QVBoxLayout(self.scan_right_farme_row3)
        self.scan_right_layout_row3.setObjectName(u"scan_right_layout_row3")

        self.verticalLayout_10.addWidget(self.scan_right_farme_row3)


        self.page_scan_layout.addWidget(self.scan_right_farme)

        self.page_scan_layout.setStretch(0, 4)
        self.page_scan_layout.setStretch(1, 1)
        self.pages.addWidget(self.page_scan)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.Shape.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.welcome_base)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.welcome_base)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 233, 265))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.tableView = QTableView(self.page_test)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(150, 280, 611, 121))
        self.spinBox = QSpinBox(self.page_test)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(270, 140, 88, 22))
        self.pages.addWidget(self.page_test)
        self.page_icp = QWidget()
        self.page_icp.setObjectName(u"page_icp")
        self.page_icp.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_icp_layout = QVBoxLayout(self.page_icp)
        self.page_icp_layout.setObjectName(u"page_icp_layout")
        self.icp_row1_farme = QFrame(self.page_icp)
        self.icp_row1_farme.setObjectName(u"icp_row1_farme")
        self.icp_row1_farme.setFrameShape(QFrame.Shape.StyledPanel)
        self.icp_row1_farme.setFrameShadow(QFrame.Shadow.Raised)
        self.icp_row1_layout = QHBoxLayout(self.icp_row1_farme)
        self.icp_row1_layout.setObjectName(u"icp_row1_layout")

        self.page_icp_layout.addWidget(self.icp_row1_farme)

        self.icp_row3_farme = QFrame(self.page_icp)
        self.icp_row3_farme.setObjectName(u"icp_row3_farme")
        self.icp_row3_farme.setFrameShape(QFrame.Shape.StyledPanel)
        self.icp_row3_farme.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.icp_row3_farme)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lable_icp_row3 = QLabel(self.icp_row3_farme)
        self.lable_icp_row3.setObjectName(u"lable_icp_row3")

        self.verticalLayout_7.addWidget(self.lable_icp_row3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page_icp_layout.addWidget(self.icp_row3_farme)

        self.icp_row2_farme = QFrame(self.page_icp)
        self.icp_row2_farme.setObjectName(u"icp_row2_farme")
        self.icp_row2_farme.setFrameShape(QFrame.Shape.StyledPanel)
        self.icp_row2_farme.setFrameShadow(QFrame.Shadow.Raised)
        self.icp_row2_layout = QVBoxLayout(self.icp_row2_farme)
        self.icp_row2_layout.setObjectName(u"icp_row2_layout")
        self.groupBox_2 = QGroupBox(self.icp_row2_farme)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lable_icp_result_mainLicence_2 = QLabel(self.groupBox_2)
        self.lable_icp_result_mainLicence_2.setObjectName(u"lable_icp_result_mainLicence_2")
        self.lable_icp_result_mainLicence_2.setMaximumSize(QSize(200, 40))
        self.lable_icp_result_mainLicence_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_2.addWidget(self.lable_icp_result_mainLicence_2)

        self.lable_icp_result_mainLicence = QLabel(self.groupBox_2)
        self.lable_icp_result_mainLicence.setObjectName(u"lable_icp_result_mainLicence")
        self.lable_icp_result_mainLicence.setMinimumSize(QSize(256, 0))
        self.lable_icp_result_mainLicence.setMaximumSize(QSize(16777215, 40))
        self.lable_icp_result_mainLicence.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_2.addWidget(self.lable_icp_result_mainLicence)

        self.lable_icp_result_updateRecordTime_2 = QLabel(self.groupBox_2)
        self.lable_icp_result_updateRecordTime_2.setObjectName(u"lable_icp_result_updateRecordTime_2")
        self.lable_icp_result_updateRecordTime_2.setMaximumSize(QSize(150, 40))
        self.lable_icp_result_updateRecordTime_2.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_2.addWidget(self.lable_icp_result_updateRecordTime_2)

        self.lable_icp_result_updateRecordTime = QLabel(self.groupBox_2)
        self.lable_icp_result_updateRecordTime.setObjectName(u"lable_icp_result_updateRecordTime")
        self.lable_icp_result_updateRecordTime.setMaximumSize(QSize(16777215, 40))
        self.lable_icp_result_updateRecordTime.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_2.addWidget(self.lable_icp_result_updateRecordTime)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lable_icp_result_unitName_2 = QLabel(self.groupBox_2)
        self.lable_icp_result_unitName_2.setObjectName(u"lable_icp_result_unitName_2")
        self.lable_icp_result_unitName_2.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_5.addWidget(self.lable_icp_result_unitName_2)

        self.lable_icp_result_unitName = QLabel(self.groupBox_2)
        self.lable_icp_result_unitName.setObjectName(u"lable_icp_result_unitName")
        self.lable_icp_result_unitName.setMaximumSize(QSize(16777215, 40))
        self.lable_icp_result_unitName.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_5.addWidget(self.lable_icp_result_unitName)

        self.lable_icp_result_natureName_2 = QLabel(self.groupBox_2)
        self.lable_icp_result_natureName_2.setObjectName(u"lable_icp_result_natureName_2")
        self.lable_icp_result_natureName_2.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_5.addWidget(self.lable_icp_result_natureName_2)

        self.lable_icp_result_natureName = QLabel(self.groupBox_2)
        self.lable_icp_result_natureName.setObjectName(u"lable_icp_result_natureName")
        self.lable_icp_result_natureName.setMaximumSize(QSize(16777215, 40))
        self.lable_icp_result_natureName.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_5.addWidget(self.lable_icp_result_natureName)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.icp_row2_layout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.icp_row2_farme)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lable_icp_result_serviceLicence_2 = QLabel(self.groupBox)
        self.lable_icp_result_serviceLicence_2.setObjectName(u"lable_icp_result_serviceLicence_2")
        self.lable_icp_result_serviceLicence_2.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_6.addWidget(self.lable_icp_result_serviceLicence_2)

        self.lable_icp_result_serviceLicence = QLabel(self.groupBox)
        self.lable_icp_result_serviceLicence.setObjectName(u"lable_icp_result_serviceLicence")
        self.lable_icp_result_serviceLicence.setMaximumSize(QSize(16777215, 40))
        self.lable_icp_result_serviceLicence.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_6.addWidget(self.lable_icp_result_serviceLicence)

        self.lable_icp_result_domain_2 = QLabel(self.groupBox)
        self.lable_icp_result_domain_2.setObjectName(u"lable_icp_result_domain_2")
        self.lable_icp_result_domain_2.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_6.addWidget(self.lable_icp_result_domain_2)

        self.lable_icp_result_domain = QLabel(self.groupBox)
        self.lable_icp_result_domain.setObjectName(u"lable_icp_result_domain")
        self.lable_icp_result_domain.setMaximumSize(QSize(16777215, 40))
        self.lable_icp_result_domain.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_6.addWidget(self.lable_icp_result_domain)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lable_icp_result_contentTypeName_2 = QLabel(self.groupBox)
        self.lable_icp_result_contentTypeName_2.setObjectName(u"lable_icp_result_contentTypeName_2")
        self.lable_icp_result_contentTypeName_2.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_7.addWidget(self.lable_icp_result_contentTypeName_2)

        self.lable_icp_result_contentTypeName = QLabel(self.groupBox)
        self.lable_icp_result_contentTypeName.setObjectName(u"lable_icp_result_contentTypeName")
        self.lable_icp_result_contentTypeName.setMaximumSize(QSize(16777215, 40))
        self.lable_icp_result_contentTypeName.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_7.addWidget(self.lable_icp_result_contentTypeName)

        self.lable_icp_result_none = QLabel(self.groupBox)
        self.lable_icp_result_none.setObjectName(u"lable_icp_result_none")
        self.lable_icp_result_none.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_7.addWidget(self.lable_icp_result_none)

        self.lable_icp_result_none_2 = QLabel(self.groupBox)
        self.lable_icp_result_none_2.setObjectName(u"lable_icp_result_none_2")
        self.lable_icp_result_none_2.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_7.addWidget(self.lable_icp_result_none_2)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)


        self.icp_row2_layout.addWidget(self.groupBox)


        self.page_icp_layout.addWidget(self.icp_row2_farme)

        self.page_icp_layout.setStretch(0, 1)
        self.page_icp_layout.setStretch(2, 5)
        self.pages.addWidget(self.page_icp)

        self.verticalLayout_2.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.scan_plugins_groupBox.setTitle(QCoreApplication.translate("MainPages", u"\u529f\u80fd\u9009\u9879", None))
        self.scan_params_groupBox.setTitle(QCoreApplication.translate("MainPages", u"\u53c2\u6570\u9009\u9879", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"\u7f51\u7edc\u8bf7\u6c42\u53c2\u6570", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u5185\u5bb9\u722c\u53d6\u6a21\u5757", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"\u7ebf\u7a0b\u6570\u91cf\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"\u7a0b\u5e8f\u6e29\u99a8\u63d0\u793a", None))
        self.label_hint.setText("")
        self.label.setText(QCoreApplication.translate("MainPages", u"       The MBigFish", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.lable_icp_row3.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainPages", u"ICP\u5907\u6848\u4e3b\u4f53\u4fe1\u606f ", None))
        self.lable_icp_result_mainLicence_2.setText(QCoreApplication.translate("MainPages", u"ICP\u5907\u6848/\u8bb8\u53ef\u8bc1\u53f7\uff1a	", None))
        self.lable_icp_result_mainLicence.setText("")
        self.lable_icp_result_updateRecordTime_2.setText(QCoreApplication.translate("MainPages", u"\u5ba1\u6838\u901a\u8fc7\u65e5\u671f\uff1a	", None))
        self.lable_icp_result_updateRecordTime.setText("")
        self.lable_icp_result_unitName_2.setText(QCoreApplication.translate("MainPages", u"\u4e3b\u529e\u5355\u4f4d\u540d\u79f0\uff1a	", None))
        self.lable_icp_result_unitName.setText("")
        self.lable_icp_result_natureName_2.setText(QCoreApplication.translate("MainPages", u"\u4e3b\u529e\u5355\u4f4d\u6027\u8d28\uff1a	", None))
        self.lable_icp_result_natureName.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainPages", u"ICP\u5907\u6848\u4e3b\u4f53\u4fe1\u606f ", None))
        self.lable_icp_result_serviceLicence_2.setText(QCoreApplication.translate("MainPages", u"ICP\u5907\u6848/\u8bb8\u53ef\u8bc1\u53f7\uff1a	", None))
        self.lable_icp_result_serviceLicence.setText("")
        self.lable_icp_result_domain_2.setText(QCoreApplication.translate("MainPages", u"\u7f51\u7ad9\u57df\u540d\uff1a	", None))
        self.lable_icp_result_domain.setText("")
        self.lable_icp_result_contentTypeName_2.setText(QCoreApplication.translate("MainPages", u"\u670d\u52a1\u524d\u7f6e\u5ba1\u6279\u9879\uff1a	", None))
        self.lable_icp_result_contentTypeName.setText("")
        self.lable_icp_result_none.setText("")
        self.lable_icp_result_none_2.setText("")
    # retranslateUi

