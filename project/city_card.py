from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QFrame, QGridLayout

class CityCard(QFrame):
    def __init__(self, city, time, condition, temp, t_max, t_min):
        super().__init__()
        
        self.setObjectName("Card")
        self.setFixedHeight(84)
        
        #створюємо та налаштовуємо позначку (назву) міста 
        self.name_label = QLabel(city)
        self.name_label.setStyleSheet("font-size: 21px; font-weight: 600; color: white;")

        #створюємо позначку часу на картці
        self.time_label = QLabel(time)
        self.time_label.setStyleSheet("font-size: 11px; color: rgba(255, 255, 255, 0.8);")
        
        # позначка стану погоди (хмарно, сонячно...)
        self.condition_label = QLabel(condition)
        self.condition_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.condition_label.setStyleSheet("font-size: 11px; color: rgba(255, 255, 255, 0.8);")
        
        #позначка температури у місці
        self.temp_label = QLabel(f"{temp}°")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.temp_label.setStyleSheet("font-size: 40px; font-weight: 600, color: white;")
        
        #позначка діапазону від максимальнох до мінімальної погоди
        self.range_label = QLabel(f"Макс.: {t_max}°, мін.: {t_min}°")
        self.range_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.range_label.setStyleSheet("font-size: 11px; color: rgba(255, 255, 255, 0.8);")
        
        #створюємо сітку для того щоб помістити у такому порядку характеристики картки (назва міста, температура...)
        layout = QGridLayout(self)
        layout.setContentsMargins(10, 6, 10, 6)
        
        #додаємо картки на layout по індексам сітки
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.time_label, 1, 0 )
        layout.addWidget(self.condition_label, 2, 0)
        layout.addWidget(self.temp_label, 0, 1, 2, 1)
        layout.addWidget(self.range_label, 2, 1)  