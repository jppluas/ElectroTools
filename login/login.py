import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout, QCheckBox

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Login')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        lbl_usuario = QLabel('Usuario:')
        form_layout.addRow(lbl_usuario, QLineEdit())

        lbl_contrasena = QLabel('Contraseña:')
        form_layout.addRow(lbl_contrasena, QLineEdit())

        chk_recordar = QCheckBox('Recordar usuario')
        form_layout.addRow(chk_recordar)

        layout.addLayout(form_layout)

        btn_ingresar = QPushButton('Ingresar')
        btn_ingresar.clicked.connect(self.ingresar)
        layout.addWidget(btn_ingresar)

        self.setLayout(layout)

    def ingresar(self):
        QMessageBox.about(self, 'Ingresar', '¡Bienvenido!')
    
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()

    sys.exit(app.exec())
