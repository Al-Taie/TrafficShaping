from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import res_rc


class AppUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.window_hieght = 430
        self.window_width = 540
        self.setFixedSize(QSize(self.window_width, self.window_hieght))
        self.welcome_tab()
        self.main_tab()
        self.tabWidget.setCurrentIndex(0)

    def welcome_tab(self):
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QRect(0, 0, 534, 430))

        self.welcome_tab = QWidget()
        self.ministry_lbl = QLabel(self.welcome_tab)
        self.ministry_lbl.setGeometry(QRect(0, 12, 200, 75))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.ministry_lbl.setFont(font)
        self.ministry_lbl.setText(u"Ministry of Higher\n"
                                  " Education & Scientific \n"
                                  " Research Ninevah University")
        self.ministry_lbl.setTextFormat(Qt.PlainText)
        self.ministry_lbl.setAlignment(Qt.AlignCenter)
        self.college_lbl = QLabel(self.welcome_tab)

        self.college_lbl.setGeometry(QRect(330, 10, 200, 75))
        self.college_lbl.setFont(font)
        self.college_lbl.setText(u"College of Electronics Engineering  \n"
                                 "  Department of Computer and Information Engineering")
        self.college_lbl.setTextFormat(Qt.PlainText)
        self.college_lbl.setAlignment(Qt.AlignCenter)
        self.college_lbl.setWordWrap(True)
        self.project_decription_lbl = QLabel(self.welcome_tab)
        self.project_decription_lbl.setGeometry(QRect(80, 300, 341, 91))

        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.project_decription_lbl.setFont(font1)
        self.project_decription_lbl.setText(
            u"A project submitted as partial fulfillment for the requirements of the degree of B.Sc. in Computer and Information Engineering")
        self.project_decription_lbl.setTextFormat(Qt.PlainText)
        self.project_decription_lbl.setAlignment(Qt.AlignCenter)
        self.project_decription_lbl.setWordWrap(True)
        self.project_name_lbl = QLabel(self.welcome_tab)
        self.project_name_lbl.setGeometry(QRect(140, 110, 251, 191))

        font2 = QFont()
        font2.setBold(True)
        self.project_name_lbl.setFont(font2)
        self.project_name_lbl.setText(
            u"\u201cRaspberry Pi-Based Network Traffic Shaper and Quality of Service (QoS) Controller\u201d\n"
            "\n"
            " Submitted by \n"
            " Amina Khalid Hashim \n"
            " Areeg Mohmmed Hmed \n"
            " \n"
            " Supervised by \n"
            " Omar Mowaffak Alsaydia")
        self.project_name_lbl.setTextFormat(Qt.PlainText)
        self.project_name_lbl.setAlignment(Qt.AlignCenter)
        self.project_name_lbl.setWordWrap(True)

        self.logo = QLabel(self.welcome_tab)
        self.logo.setGeometry(QRect(213, 0, 81, 91))
        self.logo.setPixmap(QPixmap(u":/logo.png"))
        self.logo.setScaledContents(True)
        self.tabWidget.addTab(self.welcome_tab, "Welcome")

    def main_tab(self):
        self.main_tab = QWidget()
        self.layoutWidget = QWidget(self.main_tab)
        self.layoutWidget.setGeometry(QRect(90, 100, 341, 181))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.url_field = QLineEdit(self.layoutWidget)
        self.url_field.setPlaceholderText(u"Url")
        self.verticalLayout.addWidget(self.url_field)

        self.horizontalLayout = QHBoxLayout()
        self.label = QLabel(self.layoutWidget)
        self.label.setText(u"Start Time:")
        self.horizontalLayout.addWidget(self.label)
        self.start_time_field = QTimeEdit(QTime().currentTime(), self.layoutWidget)
        self.horizontalLayout.addWidget(self.start_time_field)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.end_time_lbl = QLabel(self.layoutWidget)
        self.end_time_lbl.setText(u"End Time:")
        self.horizontalLayout_2.addWidget(self.end_time_lbl)
        self.end_time_field = QTimeEdit(QTime().currentTime(), self.layoutWidget)
        self.horizontalLayout_2.addWidget(self.end_time_field)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.block_btn = QPushButton(self.layoutWidget)
        self.block_btn.setText(u"Block")
        self.horizontalLayout_3.addWidget(self.block_btn)
        self.unblock_btn = QPushButton(self.layoutWidget)
        self.unblock_btn.setFocusPolicy(Qt.NoFocus)
        self.unblock_btn.setText(u"Unblock")
        self.horizontalLayout_3.addWidget(self.unblock_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.main_tab, "Main")
