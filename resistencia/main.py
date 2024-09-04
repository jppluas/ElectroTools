import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLineEdit, QLabel, QPushButton, QFileDialog, QStackedWidget)
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor, QAction
from PyQt6.QtCore import Qt

from resistance_calculator import ResistanceCalculator
from voltage_divider_calculator import VoltageDividerCalculator
from resistors_voltage_divider_calculator import ResistorsVoltageDividerCalculator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadoras")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        self.resistance_calculator = ResistanceCalculator()
        self.voltage_divider_calculator = VoltageDividerCalculator()
        self.resistors_voltage_divider_calculator = ResistorsVoltageDividerCalculator()


        self.stacked_widget.addWidget(self.resistance_calculator)
        self.stacked_widget.addWidget(self.voltage_divider_calculator)
        self.stacked_widget.addWidget(self.resistors_voltage_divider_calculator)


        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        calculator_menu = menubar.addMenu('Calculadoras')

        resistance_action = QAction('Calculadora de Resistencias', self)
        resistance_action.triggered.connect(self.show_resistance_calculator)
        calculator_menu.addAction(resistance_action)

        voltage_divider_action = QAction('Calculadora de Divisor de Voltaje', self)
        voltage_divider_action.triggered.connect(self.show_voltage_divider_calculator)
        calculator_menu.addAction(voltage_divider_action)

        resistors_voltage_divider_action = QAction('Calculadora de Divisor de Voltaje con Resistencias Comerciales', self)
        resistors_voltage_divider_action.triggered.connect(self.show_resistors_voltage_divider_calculator)
        calculator_menu.addAction(resistors_voltage_divider_action)

    def show_resistance_calculator(self):
        self.stacked_widget.setCurrentWidget(self.resistance_calculator)

    def show_voltage_divider_calculator(self):
        self.stacked_widget.setCurrentWidget(self.voltage_divider_calculator)

    def show_resistors_voltage_divider_calculator(self):
        self.stacked_widget.setCurrentWidget(self.resistors_voltage_divider_calculator)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


   
