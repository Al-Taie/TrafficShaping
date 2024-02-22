#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
from threading import Thread
from ui import AppUI
from firewall import FirewallManager


class TrafficShapingApp(AppUI):
    def __init__(self):
        super().__init__()
        self.firewall = FirewallManager()
        self.setWindowTitle("Traffic Shaping GUI")
        self.handle_connection()

    def handle_connection(self):
        self.block_btn.clicked.connect(self.block_url)
        self.unblock_btn.clicked.connect(self.unblock_url)

    def block_url(self):
        url = self.url_field.text()
        start_time = self.start_time_field.time().toPyTime()
        end_time = self.end_time_field.time().toPyTime()

        process = lambda: self.firewall.block(url=url, start_time=start_time, end_time=end_time)
        Thread(target=process, daemon=True).start()

    def unblock_url(self):
        url = self.url_field.text()

        process = lambda: self.firewall.unblock(url=url)
        Thread(target=process, daemon=True).start()


def main():
    app = QApplication(sys.argv)
    window = TrafficShapingApp()
    window.show()
    apply_stylesheet(app, theme='theme.xml', invert_secondary=False)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
