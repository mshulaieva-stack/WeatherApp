from PyQt6.QtWidgets import QFrame , QVBoxLayout, QHBoxLayout

from .city_card import CityCard
from .theme_button import create_theme_toggle

#список міст та інформація із них, яка буде на картках
CITIES = [("Дніпро", "15:24", "Переважно хмарно", 11, 11, 0),
          ("Київ", "15:24", "Сонячно", 14, 15, 0),
          ("Братіслава", "14:24", "Подекуди хмарно, місцям...", 9, 10, 1),
          ("Варшава", "14:24", "Хмарно", 15, 18, 7),
          ("Рим", "14:24", "Сонячно", 24, 25, 16)]

#клас для створення усієї лівої панелі
class CitiesFrame(QFrame):
    def __init__ (self):
        super().__init__()
        self.setObjectName("citiesFrame")
        self.setStyleSheet("background-color: #425060;")
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        self.main_layout.setSpacing(12)
        
        #верхня панель для кнопки перемикача
        top_switch = QHBoxLayout()
        top_switch.addStretch()
        
        #отримуємо капсулу та додаємо її на верхню панель
        toggle = create_theme_toggle()
        top_switch.addWidget(toggle)
        
        #додаємо на головний layout верхню панель
        self.main_layout.addLayout(top_switch)
        
        #перебираємо список з містами та створюємо картки на лівій панелі
        for city_data in CITIES:
            card = CityCard(*city_data)
            self.main_layout.addWidget(card)
            
        self.main_layout.addStretch() #притискаємо картки догори


