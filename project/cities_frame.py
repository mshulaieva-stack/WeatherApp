from PyQt6.QtWidgets import QFrame , QVBoxLayout

class CitiesFrame(QFrame):
    def __init__ (self):
        super().__init__()
        self.setObjectName("citiesFrame")
        self.setStyleSheet("background-color: #425060;")
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        self.main_layout.setSpacing(12)



 