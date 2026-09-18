import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QGuiApplication
from ExcelManager import ExcelManager

DARK_STYLESHEET = """
QWidget {
    background-color: #121212;
    color: #FFFFFF;
    font-family: Helvetica, Arial, sans-serif;
}
QLabel {
    color: #FFFFFF;
}
QLineEdit {
    background-color: #2D2D2D;
    color: #FFFFFF;
    border: 1px solid #444444;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 18px;
}
QLineEdit:focus {
    border: 1px solid #4A90E2;
}
QPushButton {
    background-color: #2D2D2D;
    color: #FFFFFF;
    border: 1px solid #555555;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 16px;
}
QPushButton:hover {
    background-color: #3D3D3D;
    border-color: #777777;
}
QPushButton:pressed {
    background-color: #1E1E1E;
}
"""


def center_window(window, width_ratio=0.5, height_ratio=0.5):
    screen = QGuiApplication.primaryScreen()
    if screen:
        screen_geometry = screen.geometry()
        w = int(screen_geometry.width() * width_ratio)
        h = int(screen_geometry.height() * height_ratio)
        x = int((screen_geometry.width() - w) / 2)
        y = int((screen_geometry.height() - h) / 2)
        window.setGeometry(x, y, w, h)
    else:
        window.resize(600, 400)


class FileNameRequest(QWidget):
    def __init__(self):
        super().__init__()
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication(sys.argv)
            self.app.setStyleSheet(DARK_STYLESHEET)
        else:
            self.setStyleSheet(DARK_STYLESHEET)

        self.gui_window = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Oboeta")
        center_window(self, 0.5, 0.5)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        # Title label
        self.text_label = QLabel("please enter file name", self)
        self.text_label.setFont(QFont("Helvetica", 24))
        self.text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text_label)

        # Input field and browse button
        input_container = QHBoxLayout()
        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Helvetica", 18))
        self.input_field.setPlaceholderText("e.g. B1 or B1.xlsx")
        self.input_field.returnPressed.connect(self.submit_text)
        input_container.addWidget(self.input_field)

        self.browse_button = QPushButton("Browse...", self)
        self.browse_button.clicked.connect(self.browse_file)
        input_container.addWidget(self.browse_button)

        layout.addLayout(input_container)

        # Output / error display label
        self.output_field = QLabel("", self)
        self.output_field.setFont(QFont("Helvetica", 16))
        self.output_field.setAlignment(Qt.AlignCenter)
        self.output_field.setStyleSheet("color: #FF6B6B;")
        layout.addWidget(self.output_field)

        # Action buttons
        btn_layout = QHBoxLayout()
        self.submit_button = QPushButton("Start", self)
        self.submit_button.clicked.connect(self.submit_text)
        btn_layout.addWidget(self.submit_button)

        self.close_button = QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)
        btn_layout.addWidget(self.close_button)

        layout.addLayout(btn_layout)

        # Additional buttons
        extra_btn_layout = QHBoxLayout()
        self.button1 = QPushButton("button1", self)
        self.button1.clicked.connect(self.function1)
        extra_btn_layout.addWidget(self.button1)

        self.button2 = QPushButton("button2", self)
        self.button2.clicked.connect(self.function2)
        extra_btn_layout.addWidget(self.button2)

        self.button3 = QPushButton("button3", self)
        self.button3.clicked.connect(self.function3)
        extra_btn_layout.addWidget(self.button3)

        layout.addLayout(extra_btn_layout)

    def function1(self):
        pass

    def function2(self):
        pass

    def function3(self):
        pass

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.input_field.setText(file_path)

    def submit_text(self, event=None):
        file_name = self.input_field.text().strip()
        if not file_name:
            self.output_field.setText("Please enter a file name.")
            return

        if not file_name.endswith(".xlsx") and not file_name.endswith(".xls"):
            file_name += ".xlsx"

        if not os.path.exists(file_name):
            self.output_field.setText(f"File '{file_name}' not found.")
            return

        print(file_name)
        self.hide()
        self.gui_window = GUI(file_name)
        self.gui_window.show()

    def run(self):
        self.show()
        if self.app:
            self.app.exec()


class GUI(QWidget):
    def __init__(self, file_name):
        super().__init__()
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication(sys.argv)
            self.app.setStyleSheet(DARK_STYLESHEET)
        else:
            self.setStyleSheet(DARK_STYLESHEET)

        self.file_name = file_name
        self.manager = ExcelManager(file_name)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Oboeta")
        center_window(self, 0.5, 0.5)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        # Question / prompt label
        initial_text = self.manager.currentCard.get_to_test() if self.manager.currentCard else "No cards available"
        self.text_label = QLabel(initial_text, self)
        self.text_label.setFont(QFont("Helvetica", 24))
        self.text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text_label)

        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Helvetica", 18))
        self.input_field.setPlaceholderText("Enter answer")
        self.input_field.returnPressed.connect(self.submit_text)
        layout.addWidget(self.input_field)

        # Feedback / output label
        self.output_field = QLabel("", self)
        self.output_field.setFont(QFont("Helvetica", 18))
        self.output_field.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.output_field)

        # Close button
        btn_layout = QHBoxLayout()
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.submit_text)
        btn_layout.addWidget(self.submit_button)

        self.close_button = QPushButton("Close", self)
        self.close_button.clicked.connect(self.close)
        btn_layout.addWidget(self.close_button)

        layout.addLayout(btn_layout)

        if not self.manager.currentCard:
            self.input_field.setEnabled(False)

    def submit_text(self, event=None):
        if not self.manager.currentCard:
            return

        text = self.input_field.text()
        self.input_field.clear()

        if self.manager.check_input(text):
            self.output_field.setStyleSheet("color: #4CAF50;")
            self.output_field.setText("Correct!")
            if self.manager.currentCard:
                self.text_label.setText(self.manager.currentCard.get_to_test())
            else:
                self.text_label.setText("All cards completed!")
                self.input_field.setEnabled(False)
        else:
            print(self.manager.currentCard.B)
            self.output_field.setStyleSheet("color: #FF6B6B;")
            self.output_field.setText(self.manager.currentCard.B)

    def closeEvent(self, event):
        self.manager.save_bus()
        event.accept()

    def run(self):
        self.show()
        if self.app:
            self.app.exec()


if __name__ == "__main__":
    fileGetter = FileNameRequest()
    fileGetter.run()
