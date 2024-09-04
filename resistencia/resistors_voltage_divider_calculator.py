from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLineEdit, QLabel, QPushButton, QFileDialog, QStackedWidget)
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor, QAction
from PyQt6.QtCore import Qt

resistor_values = [
    1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2,
    10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
    100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
    1000, 1200, 1500, 1800, 2200, 2700, 3300, 3900, 4700, 5600, 6800, 8200,
    10000, 12000, 15000, 18000, 22000, 27000, 33000, 39000, 47000, 56000, 68000, 82000,
    100000, 120000, 150000, 180000, 220000, 270000, 330000, 390000, 470000, 560000, 680000, 820000,
    1000000, 1200000, 1500000, 1800000, 2200000, 2700000, 3300000, 3900000, 4700000, 5600000, 6800000, 8200000,
    10000000, 12000000, 15000000, 18000000, 22000000, 27000000, 33000000, 39000000, 47000000, 56000000, 68000000, 82000000
]

class ResistorsVoltageDividerCalculator(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.voltage_input = QLineEdit()
        self.output_voltage_input = QLineEdit()
        self.result_label = QLabel()

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate_voltage_divider)

        layout.addWidget(QLabel("Voltaje de entrada (V):"))
        layout.addWidget(self.voltage_input)
        layout.addWidget(QLabel("Voltaje de salida deseado (V):"))
        layout.addWidget(self.output_voltage_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_voltage_divider(self):
        try:
            voltage_in = float(self.voltage_input.text())
            voltage_out_desired = float(self.output_voltage_input.text())

            best_combination, actual_voltage_out = self.find_best_resistor_combination(voltage_in, voltage_out_desired)
            if best_combination:
                self.result_label.setText(f"Mejor combinación de resistencias:\nR1 = {best_combination[0]} ohmios, R2 = {best_combination[1]} ohmios\nVoltaje real de salida: {actual_voltage_out} V")
            else:
                self.result_label.setText("No se pudo encontrar una combinación de resistencias.")
        except ValueError:
            self.result_label.setText("Entrada no válida!")

    def find_best_resistor_combination(self, voltage_in, voltage_out_desired):
        best_error = float('inf')
        best_combination = None
        actual_voltage_out_best = None

        for r1 in resistor_values:
            for r2 in resistor_values:
                voltage_out = (r2 / (r1 + r2)) * voltage_in
                error = abs(voltage_out - voltage_out_desired)
                if error < best_error:
                    best_error = error
                    best_combination = (r1, r2)
                    actual_voltage_out_best = voltage_out

        return best_combination, actual_voltage_out_best
