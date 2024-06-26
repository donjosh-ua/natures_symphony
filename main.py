from PyQt6 import QtWidgets
from view.defaultView import Ui_NuevoRegistro
import sys


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    NuevoRegistro = QtWidgets.QMainWindow()

    ui = Ui_NuevoRegistro()
    ui.setupUi(NuevoRegistro)

    NuevoRegistro.show()
    
    sys.exit(app.exec())