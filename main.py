import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout, QComboBox
)
from PySide6.QtCore import Qt, QSize
import qtawesome as qta

class DeepProApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeepPro AI Photo App")
        self.setFixedSize(1280, 720)

        # Main container
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Left panel: Image Preview
        self.left_panel = QLabel()
        self.left_panel.setFixedWidth(640)
        self.left_panel.setStyleSheet("background-color: #1e1e1e;")
        user_icon = qta.icon('fa5s.user-circle', color='gray')
        self.left_panel.setPixmap(user_icon.pixmap(200, 200))
        self.left_panel.setAlignment(Qt.AlignCenter)

        # Right panel
        self.right_panel = QWidget()
        self.right_panel.setStyleSheet("background-color: #121212;")
        right_layout = QVBoxLayout(self.right_panel)
        right_layout.setContentsMargins(10, 10, 10, 10)
        right_layout.setSpacing(15)

        # Assemble panels
        main_layout.addWidget(self.left_panel)
        main_layout.addWidget(self.right_panel)

        self.setup_top_inputs(right_layout)
        self.setup_prompt_area(right_layout)
        self.setup_tools_and_deep_button(right_layout)
        self.setup_grid_buttons(right_layout)
        self.setup_file_buttons(right_layout)

    def setup_top_inputs(self, layout):
        input_container = QWidget()
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)
        input_layout.setContentsMargins(0, 0, 0, 0)

        inputs = [
            ("Live camera", 'fa5s.camera'),
            ("Input", 'fa5s.user'),
            ("Input +", 'fa5s.plus'),
            ("Style", 'fa5s.paint-brush'),
            ("Background", 'fa5s.image'),
            ("Overlay", 'fa5s.layer-group')
        ]

        for label, icon_name in inputs:
            card = QWidget()
            card.setFixedSize(90, 130)
            card.setStyleSheet("""
                background-color: #2b2b2b;
                border: 1px solid #444;
                border-radius: 10px;
            """)
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(5, 5, 5, 5)
            card_layout.setSpacing(5)

            # Close button
            close_btn = QPushButton("x")
            close_btn.setFixedSize(16, 16)
            close_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #999;
                    border: none;
                    font-weight: bold;
                }
                QPushButton:hover {
                    color: red;
                }
            """)
            close_btn.setCursor(Qt.PointingHandCursor)

            top_layout = QHBoxLayout()
            top_layout.addStretch()
            top_layout.addWidget(close_btn)

            icon_label = QLabel()
            icon = qta.icon(icon_name, color='gray')
            icon_label.setPixmap(icon.pixmap(40, 40))
            icon_label.setAlignment(Qt.AlignCenter)

            text_label = QLabel(label)
            text_label.setAlignment(Qt.AlignCenter)
            text_label.setStyleSheet("color: #ccc; font-size: 12px;")

            card_layout.addLayout(top_layout)
            card_layout.addWidget(icon_label)
            card_layout.addWidget(text_label)
            input_layout.addWidget(card)

        input_container.setLayout(input_layout)
        layout.addWidget(input_container)

    def setup_prompt_area(self, layout):
        prompt_input = QLineEdit()
        prompt_input.setPlaceholderText("Enter your prompt here...")
        prompt_input.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: white;
                padding: 8px;
                font-size: 14px;
                border: 1px solid #444;
                border-radius: 5px;
            }
        """)
        layout.addWidget(prompt_input)

    def setup_tools_and_deep_button(self, layout):
        row = QHBoxLayout()
        row.setSpacing(10)

        tool_icons = ['camera', 'copy', 'paste', 'bookmark']
        for icon_name in tool_icons:
            btn = QPushButton()
            btn.setIcon(qta.icon(f'fa5s.{icon_name}', color='white'))
            btn.setFixedSize(32, 32)
            btn.setStyleSheet("background-color: #2a2a2a; border: none; border-radius: 5px;")
            row.addWidget(btn)

        row.addStretch()

        deep_btn = QPushButton("deep")
        deep_btn.setStyleSheet("""
            QPushButton {
                background-color: #d92c2c;
                color: white;
                font-weight: bold;
                font-size: 14px;
                padding: 10px 20px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #b52424;
            }
        """)
        row.addWidget(deep_btn)

        layout.addLayout(row)

    def setup_grid_buttons(self, layout):
        grid_container = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        btn_names = [
            "Photobooth", "Flux", "Text2Image", "Matting", "Deep", "Shaper", "Face swap",
            "Change outfit", "T2i with pose", "Custom BG", "Bg & Outfit", "Advance matting", "Img2img", "Cartoon"
        ]

        for idx, name in enumerate(btn_names):
            btn = QPushButton(name)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d;
                    color: white;
                    padding: 10px;
                    font-size: 13px;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #444444;
                }
            """)
            row = idx // 7
            col = idx % 7
            grid_layout.addWidget(btn, row, col)

        grid_container.setLayout(grid_layout)
        layout.addWidget(grid_container)

    def setup_file_buttons(self, layout):
        file_row = QHBoxLayout()
        file_icons = ["folder-open", "save", "cloud-upload-alt", "cog"]

        for icon in file_icons[:3]:
            btn = QPushButton()
            btn.setIcon(qta.icon(f'fa5s.{icon}', color='white'))
            btn.setFixedSize(32, 32)
            btn.setStyleSheet("background-color: #2a2a2a; border: none; border-radius: 5px;")
            file_row.addWidget(btn)

        format_combo = QComboBox()
        format_combo.addItems(["png", "jpg", "webp"])
        format_combo.setStyleSheet("background-color: #1e1e1e; color: white;")
        file_row.addWidget(format_combo)

        settings_btn = QPushButton()
        settings_btn.setIcon(qta.icon(f'fa5s.{file_icons[-1]}', color='white'))
        settings_btn.setFixedSize(32, 32)
        settings_btn.setStyleSheet("background-color: #2a2a2a; border: none; border-radius: 5px;")
        file_row.addWidget(settings_btn)

        layout.addLayout(file_row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DeepProApp()
    win.show()
    sys.exit(app.exec())
