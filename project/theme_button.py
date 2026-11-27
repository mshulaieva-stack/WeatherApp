from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton

#функція для перемикача теми
def create_theme_toggle():
    
    #біла капсула перемикача
    toggle = QFrame()
    toggle.setFixedSize(65, 28)
    toggle.setStyleSheet("background-color: white; border-radius: 14px;")
    
    #горизонтальний layout всередині капсули
    layout = QHBoxLayout(toggle)
    layout.setContentsMargins(3, 3, 3, 3)
    layout.addStretch()
    
    #темний кружечок з символом місяця
    moon_button = QPushButton("🌙")
    moon_button.setFixedSize(22, 22)
    moon_button.setStyleSheet("background-color: #36414E; color: white; border-radius: 11px; font_size: 13px;")
    
    #додаємо на капсулу темну кнопку з місяцем
    layout.addWidget(moon_button)
    
    return toggle