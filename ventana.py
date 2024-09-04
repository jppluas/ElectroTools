import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Ventana con botón')
        self.show()

        self.boton = QPushButton('Mostrar mensaje', self)
        self.boton.move(100, 100)
        self.boton.clicked.connect(self.mostrarMensaje)

    def mostrarMensaje(self):
        QMessageBox.about(self, 'Mensaje', '¡Hola, mundo!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()

    sys.exit(app.exec())
