from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLineEdit, QLabel, QPushButton, QFileDialog, QStackedWidget)
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor, QAction
from PyQt6.QtCore import Qt

class VoltageDividerCalculator(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.voltage_input = QLineEdit()
        self.resistance_input1 = QLineEdit()
        self.resistance_input2 = QLineEdit()

        self.result_label = QLabel()

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate_voltage_divider)

        layout.addWidget(QLabel("Voltaje de entrada (V):"))
        layout.addWidget(self.voltage_input)
        layout.addWidget(QLabel("Resistencia R1 (ohmios):"))
        layout.addWidget(self.resistance_input1)
        layout.addWidget(QLabel("Resistencia R2 (ohmios):"))
        layout.addWidget(self.resistance_input2)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_voltage_divider(self):
        try:
            voltage = float(self.voltage_input.text())
            resistance1 = float(self.resistance_input1.text())
            resistance2 = float(self.resistance_input2.text())

            output_voltage = (resistance2 / (resistance1 + resistance2)) * voltage
            self.result_label.setText(f"Voltaje de salida: {output_voltage} V")
        except ValueError:
            self.result_label.setText("¡Entrada no válida!")
    