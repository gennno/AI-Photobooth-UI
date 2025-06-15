import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout
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

        # Left panel (ikon user)
        self.left_panel = QLabel()
        self.left_panel.setFixedWidth(640)
        self.left_panel.setStyleSheet("background-color: #1e1e1e;")
        user_icon = qta.icon('fa5s.user-circle', color='gray')  # fa5 solid style
        self.left_panel.setPixmap(user_icon.pixmap(200, 200))
        self.left_panel.setAlignment(Qt.AlignCenter)

        # Right panel
        self.right_panel = QWidget()
        self.right_panel.setStyleSheet("background-color: #121212;")
        right_layout = QVBoxLayout(self.right_panel)
        right_layout.setContentsMargins(10, 10, 10, 10)
        right_layout.setSpacing(15)

        # Tambahkan ke main layout
        main_layout.addWidget(self.left_panel)
        main_layout.addWidget(self.right_panel)

        self.setup_top_buttons(right_layout)
        self.setup_grid_buttons(right_layout)

    def setup_top_buttons(self, layout):
        top_button_row = QHBoxLayout()
        buttons_top = [
            ("Live camera", 'fa5s.video'),
            ("Input", 'fa5s.upload'),
            ("Input +", 'fa5s.plus'),
            ("Style", 'fa5s.paint-brush'),
            ("Background", 'fa5s.image'),
            ("Overlay", 'fa5s.layer-group')
        ]

        for label, icon_name in buttons_top:
            btn = QPushButton(label)
            btn.setIcon(qta.icon(icon_name, color='white'))
            btn.setIconSize(QSize(18, 18))
            btn.setStyleSheet(self.button_style())
            btn.clicked.connect(lambda checked, l=label: print(f"{l} clicked"))
            top_button_row.addWidget(btn)

        layout.addLayout(top_button_row)

    def setup_grid_buttons(self, layout):
        grid_buttons = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

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
            btn.setIconSize(QSize(20, 20))
            btn.setStyleSheet(self.button_style())
            btn.clicked.connect(lambda checked, n=name: print(f"{n} clicked"))
            grid_layout.addWidget(btn, *pos)

        grid_buttons.setLayout(grid_layout)
        layout.addWidget(grid_buttons)

    def button_style(self):
        return """
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
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DeepProApp()
    win.show()
    sys.exit(app.exec())
