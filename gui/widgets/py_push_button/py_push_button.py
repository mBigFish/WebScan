# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
    border: {_border_width}px {_border_style} {_border_color};
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
    border-radius: {_radius};
    background-color: {_bg_color};
}}
QPushButton:hover {{
    border-color: {_border_color_hover};
    background-color: {_bg_color_hover};
}}
QPushButton:pressed {{
    border-color: {_border_color_pressed};
    background-color: {_bg_color_pressed};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
            self,
            text: str,
            radius: int,
            color: str,
            bg_color: str,
            bg_color_hover: str,
            bg_color_pressed: str,
            border_width: int = 1,
            border_style: str = "solid",
            border_color: str = "transparent",
            border_color_hover: str | None = None,
            border_color_pressed: str | None = None,
            parent: QWidget | None = None,
    ):
        super().__init__(parent)

        # 初始化参数存储
        self._text = text
        self._radius = radius
        self._color = color
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed

        # 边框参数处理
        self._border_width = border_width
        self._border_style = border_style
        self._border_color = border_color
        self._border_color_hover = border_color_hover or border_color
        self._border_color_pressed = border_color_pressed or border_color

        # 基础控件设置
        self.setText(text)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__apply_style()

    def __apply_style(self) -> None:
        """应用所有样式参数到样式表"""
        custom_style = style.format(
            # 基础样式参数
            _color=self._color,
            _radius=f"{self._radius}px",  # 明确单位
            _bg_color=self._bg_color,
            _bg_color_hover=self._bg_color_hover,
            _bg_color_pressed=self._bg_color_pressed,

            # 边框样式参数
            _border_width=self._border_width,
            _border_style=self._border_style,
            _border_color=self._border_color,
            _border_color_hover=self._border_color_hover,
            _border_color_pressed=self._border_color_pressed
        )
        self.setStyleSheet(custom_style)

    # region 公共方法 ----------------------------------------------------------
    def set_border(
            self,
            width: int | None = None,
            style: str | None = None,
            color: str | None = None
    ) -> None:
        """设置边框属性"""
        if width is not None:
            self._border_width = width
        if style is not None:
            self._border_style = style
        if color is not None:
            self._border_color = color
        self.__apply_style()

    def set_border_hover(self, color: str) -> None:
        """设置悬停边框颜色"""
        self._border_color_hover = color
        self.__apply_style()

    def set_border_pressed(self, color: str) -> None:
        """设置按下边框颜色"""
        self._border_color_pressed = color
        self.__apply_style()

    def set_bg_color(self, color: str) -> None:
        """设置背景颜色"""
        self._bg_color = color
        self.__apply_style()

    def set_bg_color_hover(self, color: str) -> None:
        """设置悬停背景颜色"""
        self._bg_color_hover = color
        self.__apply_style()

    def set_bg_color_pressed(self, color: str) -> None:
        """设置按下背景颜色"""
        self._bg_color_pressed = color
        self.__apply_style()

    def set_text_color(self, color: str) -> None:
        """设置文字颜色"""
        self._color = color
        self.__apply_style()

    # def animate_bg_color(self, start_color, end_color, duration=500):
    #     """背景色渐变动画"""
    #     self.anim = QPropertyAnimation(self, b"bg_color")
    #     self.anim.setDuration(duration)
    #     self.anim.setEasingCurve(QEasingCurve.OutCubic)
    #     self.anim.setStartValue(start_color)
    #     self.anim.setEndValue(end_color)
    #     self.anim.start()
