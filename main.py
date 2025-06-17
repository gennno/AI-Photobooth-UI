import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
)
from PySide6.QtCore import Qt, QSize
import qtawesome as qta

class DeepProApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeepPro AI Photo App")
        self.setFixedSize(1280, 720)
        self.setStyleSheet("background-color: #121212;")

        # Main container
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Left panel (ikon user)
        self.left_panel = QLabel()
        self.left_panel.setFixedWidth(640)
        self.left_panel.setStyleSheet("background-color: #1e1e1e;")
        user_icon = qta.icon('fa5s.user-circle', color='gray')
        self.left_panel.setPixmap(user_icon.pixmap(200, 200))
        self.left_panel.setAlignment(Qt.AlignCenter)

        # Right panel
        self.right_panel = QWidget()
        right_layout = QVBoxLayout(self.right_panel)
        right_layout.setContentsMargins(10, 10, 10, 10)
        right_layout.setSpacing(15)

        # Tambahkan ke main layout
        main_layout.addWidget(self.left_panel)
        main_layout.addWidget(self.right_panel)

        self.setup_top_inputs(right_layout)
        self.setup_grid_buttons(right_layout)

    def setup_top_inputs(self, layout):
        input_container = QWidget()
        input_layout = QHBoxLayout()
        input_layout.setSpacing(12)
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
            card.setFixedSize(100, 120)
            card.setStyleSheet("""
                QWidget {
                    background-color: #1c1c1c;
                    border: 1px solid #333;
                    border-radius: 10px;
                }
                QWidget:hover {
                    background-color: #2a2a2a;
                }
            """)

            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(6, 6, 6, 6)
            card_layout.setSpacing(4)

            # Close button
            close_btn = QPushButton("x")
            close_btn.setFixedSize(16, 16)
            close_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: #888;
                    border: none;
                    font-weight: bold;
                }
                QPushButton:hover {
                    color: red;
                }
            """)
            close_btn.setCursor(Qt.PointingHandCursor)
            close_btn.clicked.connect(lambda checked, l=label: print(f"{l} closed"))

            top_row = QHBoxLayout()
            top_row.addStretch()
            top_row.addWidget(close_btn)

            icon_label = QLabel()
            icon = qta.icon(icon_name, color='gray')
            icon_label.setPixmap(icon.pixmap(40, 40))
            icon_label.setAlignment(Qt.AlignCenter)

            text_label = QLabel(label)
            text_label.setAlignment(Qt.AlignCenter)
            text_label.setStyleSheet("color: #bbb; font-size: 11px;")

            card_layout.addLayout(top_row)
            card_layout.addWidget(icon_label)
            card_layout.addWidget(text_label)

            input_layout.addWidget(card)

        input_container.setLayout(input_layout)
        layout.addWidget(input_container)

    def setup_grid_buttons(self, layout):
        grid_buttons = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        btn_names = [
            ("Photobooth", 'fa5s.camera-retro'),
            ("Flux", 'fa5s.bolt'),
            ("Text2Image", 'fa5s.font'),
            ("Matting", 'fa5s.cut'),
            ("Deep", 'fa5s.brain'),
            ("Shaper", 'fa5s.shapes'),
            ("Face swap", 'fa5s.user-friends'),
            ("Change outfit", 'fa5s.tshirt'),
            ("T2i with pose", 'fa5s.user'),
            ("Custom BG", 'fa5s.images'),
            ("Bg & Outfit", 'fa5s.fill-drip'),
            ("Advance matting", 'fa5s.cut'),
            ("Img2img", 'fa5s.sync'),
            ("Cartoon", 'fa5s.smile')
        ]

        positions = [(i, j) for i in range(4) for j in range(4)]
        for pos, (name, icon_name) in zip(positions, btn_names):
            btn = QPushButton(name)
            btn.setIcon(qta.icon(icon_name, color='white'))
            btn.setIconSize(QSize(22, 22))
            btn.setStyleSheet(self.button_style())
            btn.setMinimumSize(QSize(130, 70))
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, n=name: print(f"{n} clicked"))
            grid_layout.addWidget(btn, *pos)

        grid_buttons.setLayout(grid_layout)
        layout.addWidget(grid_buttons)

    def button_style(self):
        return """
            QPushButton {
                background-color: #2c2c2c;
                color: white;
                font-size: 13px;
                padding: 8px;
                border-radius: 6px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DeepProApp()
    win.show()
    sys.exit(app.exec())
