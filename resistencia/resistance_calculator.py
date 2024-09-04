from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLineEdit, QLabel, QPushButton, QFileDialog, QStackedWidget)
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor, QAction
from PyQt6.QtCore import Qt

# Diccionarios de mapeo de colores a valores de franjas, multiplicadores y tolerancias
color_to_value = {
    'Negro': 0, 'Marrón': 1, 'Rojo': 2, 'Naranja': 3, 'Amarillo': 4,
    'Verde': 5, 'Azul': 6, 'Violeta': 7, 'Gris': 8, 'Blanco': 9
}

color_to_multiplier = {
    'Negro (1)': 1, 'Marrón (10)': 10, 'Rojo (100)': 100, 'Naranja (1k)': 1000, 'Amarillo (10k)': 10000,
    'Verde (100k)': 100000, 'Azul (1M)': 1000000, 'Violeta (10M)': 10000000, 'Gris (100M)': 100000000, 'Blanco (1G)': 1000000000,
    'Dorado (0.1)': 0.1, 'Plateado (0.01)': 0.01
}

color_to_tolerance = {
    'Marrón (±1%)': 1, 'Rojo (±2%)': 2, 'Verde (±0.5%)': 0.5, 'Azul (±0.25%)': 0.25, 'Violeta (±0.1%)': 0.1, 'Gris (±0.05%)': 0.05,
    'Dorado (±5%)': 5, 'Plateado (±10%)': 10
}

value_to_color = {v: k for k, v in color_to_value.items()}
multiplier_to_color = {v: k for k, v in color_to_multiplier.items()}
tolerance_to_color = {v: k for k, v in color_to_tolerance.items()}

color_to_hex = {
    'Negro': '#000000', 'Marrón': '#8B4513', 'Rojo': '#FF0000', 'Naranja': '#FFA500', 'Amarillo': '#FFFF00',
    'Verde': '#008000', 'Azul': '#0000FF', 'Violeta': '#EE82EE', 'Gris': '#808080', 'Blanco': '#FFFFFF',
    'Dorado': '#FFD700', 'Plateado': '#C0C0C0'
}

hex_to_color = {v: k for k, v in color_to_hex.items()}

class ResistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.band1 = QComboBox()
        self.band2 = QComboBox()
        self.band3 = QComboBox()
        self.band4 = QComboBox()

        self.resistance_value = QLineEdit()

        self.resistance_total = QLabel()

        for color, value in color_to_value.items():
            self.band1.addItem(f"{color} ({value})", value)
            self.band2.addItem(f"{color} ({value})", value)
        for color, multiplier in color_to_multiplier.items():
            self.band3.addItem(color, multiplier)
        for color, tolerance in color_to_tolerance.items():
            self.band4.addItem(color, tolerance)

        self.band1.currentIndexChanged.connect(self.update_resistance)
        self.band2.currentIndexChanged.connect(self.update_resistance)
        self.band3.currentIndexChanged.connect(self.update_resistance)
        self.band4.currentIndexChanged.connect(self.update_resistance)

        self.resistance_value.returnPressed.connect(self.update_bands_from_input)

        layout.addWidget(QLabel("Banda 1"))
        layout.addWidget(self.band1)
        layout.addWidget(QLabel("Banda 2"))
        layout.addWidget(self.band2)
        layout.addWidget(QLabel("Multiplicador"))
        layout.addWidget(self.band3)
        layout.addWidget(QLabel("Tolerancia"))
        layout.addWidget(self.band4)
        layout.addWidget(QLabel("Valor de la resistencia (ohmios)"))
        layout.addWidget(self.resistance_value)

        self.resistance_image = QLabel()
        layout.addWidget(self.resistance_image)
        layout.addWidget(self.resistance_total)

        self.setLayout(layout)

        self.update_resistance()

    def update_resistance(self):
        try:
            band1_value = self.band1.currentData()
            band2_value = self.band2.currentData()
            multiplier_value = self.band3.currentData()
            tolerance_value = self.band4.currentData()

            resistance = (band1_value * 10 + band2_value) * multiplier_value
            self.resistance_value.setText(f"{resistance}")
            self.resistance_total.setText(f"{resistance} Ω ±{tolerance_value}%")

            self.update_resistance_image()
        except KeyError:
            self.resistance_value.setText("")
            self.resistance_total.setText("")

    def update_resistance_image(self):
        resistance_img = QPixmap(300, 100)
        resistance_img.fill(Qt.GlobalColor.white)
        painter = QPainter(resistance_img)

        # Dibujar la resistencia
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.white)
        painter.drawRect(50, 30, 200, 40)

        # Dibujar las bandas de colores
        band_colors = [
            self.band1.currentText().split(' ')[0], 
            self.band2.currentText().split(' ')[0], 
            self.band3.currentText().split(' ')[0].split(' ')[0],
            self.band4.currentText().split(' ')[0].split(' ')[0]
        ]
        positions = [60, 90, 150, 210]
        for i, color in enumerate(band_colors):
            painter.setBrush(QColor(color_to_hex[color]))
            painter.drawRect(positions[i], 30, 20, 40)

        painter.end()
        self.resistance_image.setPixmap(resistance_img)
    
    def update_bands_from_input(self):
        try:
            resistance_text = self.resistance_value.text()
            resistance = float(resistance_text)

            # Find the closest multiplier
            multiplier = 1
            while resistance >= 100 and multiplier <= 1000000000:
                resistance /= 10
                multiplier *= 10

            # Encontrar los valores de las bandas
            band1_value = int(resistance // 10)
            band2_value = int(resistance % 10)
            multiplier_value = multiplier

            self.band1.setCurrentIndex(self.band1.findData(band1_value))
            self.band2.setCurrentIndex(self.band2.findData(band2_value))
            self.band3.setCurrentIndex(self.band3.findData(multiplier_value))

            self.update_resistance_image()
        except ValueError:
            pass
