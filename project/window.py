from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
from .cities_frame import CitiesFrame

WINDOW_W = 1260
WINDOW_H = 720
LEFT_W = 380
MARGIN = 20

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Weather app")
        self.setFixedSize(WINDOW_W, WINDOW_H)

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.cities_frame = CitiesFrame()
        self.cities_frame.setFixedWidth(LEFT_W)
        root.addWidget(self.cities_frame)

        self.right_frame = QFrame()
        self.right_frame.setStyleSheet("background-color: #DF8B77;")
        root.addWidget(self.right_frame)

        right_layout = QVBoxLayout(self.right_frame)
        right_layout.setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)
        right_layout.setSpacing(MARGIN)

        self.top_bar = self.make_frame(36)
        self.current_block = self.make_frame(272)
        self.forecast_block = self.make_frame(320)
        
        right_layout.addWidget(self.top_bar)
        right_layout.addWidget(self.current_block)
        right_layout.addWidget(self.forecast_block)

    def make_frame(self, height):
        block = QFrame()
        block.setFixedHeight(height)
        block.setStyleSheet("background-color: #22252A")
        return block
