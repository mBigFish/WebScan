from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget

from gui.core.functions import Functions


class UiPageHome:
    # 页面 1 - 向主页面添加logo
    def setup_ui(self):
        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)