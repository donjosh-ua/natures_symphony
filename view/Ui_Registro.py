# Form implementation generated from reading ui file 'defaultView.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from controller.AnimatedController import AnimatedController

class Ui_Registro(object):
    def setupUi(self, NuevoRegistro):
        NuevoRegistro.setObjectName("NuevoRegistro")
        NuevoRegistro.resize(455, 622)
        NuevoRegistro.setStyleSheet("Background: white")
        
        self.centralwidget = QtWidgets.QWidget(NuevoRegistro)
        self.centralwidget.setObjectName("centralwidget")
        
        # Crear layout principal
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        # Crear y configurar el frame principal
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("Background: white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        # Crear layout para el frame principal
        self.frameLayout = QtWidgets.QVBoxLayout(self.frame)
        
        # Agregar título
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frameLayout.addWidget(self.label)
        
        # Agregar subtítulo
        self.labelAcercar = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelAcercar.setFont(font)
        self.labelAcercar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAcercar.setStyleSheet("color: rgb(170, 255, 127)")
        self.labelAcercar.setObjectName("labelAcercar")
        self.frameLayout.addWidget(self.labelAcercar)
        
        # Agregar señal
        self.labelSenal = AnimatedController(self.frame)
        self.labelSenal.setFixedSize(200, 200)
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px; border: 2px")
        self.labelSenal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSenal.setObjectName("labelSenal")
        self.frameLayout.addWidget(self.labelSenal, alignment=QtCore.Qt.AlignCenter)
        
        # Agregar botón de play
        self.btnPlay = QtWidgets.QPushButton(self.frame)
        self.btnPlay.setFixedSize(81, 41)
        self.btnPlay.setStyleSheet("background: rgb(170, 255, 127); border-radius: 90px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/images/boton-de-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon)
        self.btnPlay.setObjectName("btnPlay")
        self.frameLayout.addWidget(self.btnPlay, alignment=QtCore.Qt.AlignCenter)
        
        # Agregar botón de almacenamiento
        self.btnAlmacenamiento = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.btnAlmacenamiento.setFont(font)
        self.btnAlmacenamiento.setStyleSheet("color: rgb(170, 255, 127);")
        self.btnAlmacenamiento.setFlat(True)
        self.btnAlmacenamiento.setObjectName("btnAlmacenamiento")
        self.frameLayout.addWidget(self.btnAlmacenamiento, alignment=QtCore.Qt.AlignCenter)
        
        # Agregar botón de aceptar captura
        self.btnAceptarCaptura = QtWidgets.QPushButton(self.frame)
        self.btnAceptarCaptura.setStyleSheet("background: rgb(0, 0, 0); color: rgb(255, 255, 255)")
        self.btnAceptarCaptura.setObjectName("btnAceptarCaptura")
        self.frameLayout.addWidget(self.btnAceptarCaptura, alignment=QtCore.Qt.AlignCenter)
        
        # Agregar frame de navegación
        self.frameNavegacion = QtWidgets.QFrame(self.frame)
        self.frameNavegacion.setStyleSheet("Background: white; border-top: 1px solid #E5E7E9;")
        self.frameNavegacion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameNavegacion.setFrameShadow(QtWidgets.QFrame.Raised)
        
        # Crear layout para la navegación
        self.navLayout = QtWidgets.QHBoxLayout(self.frameNavegacion)
        
        # Agregar botones de navegación
        self.btnChat = QtWidgets.QPushButton(self.frameNavegacion)
        self.btnChat.setFixedSize(50, 50)
        self.btnChat.setStyleSheet("border: none;")
        iconChat = QtGui.QIcon()
        iconChat.addPixmap(QtGui.QPixmap("./assets/images/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnChat.setIcon(iconChat)
        self.btnChat.setIconSize(QtCore.QSize(50, 50))
        self.btnChat.setText("")
        self.btnChat.setObjectName("btnChat")
        self.navLayout.addWidget(self.btnChat)
        
        self.b = QtWidgets.QPushButton(self.frameNavegacion)
        self.b.setFixedSize(50, 50)
        self.b.setStyleSheet("border: none;")
        iconTrivia = QtGui.QIcon()
        iconTrivia.addPixmap(QtGui.QPixmap("./assets/images/trivia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b.setIcon(iconTrivia)
        self.b.setIconSize(QtCore.QSize(50, 50))
        self.b.setText("")
        self.b.setObjectName("b")
        self.navLayout.addWidget(self.b)
        
        self.btnCapturar = QtWidgets.QPushButton(self.frameNavegacion)
        self.btnCapturar.setFixedSize(50, 50)
        self.btnCapturar.setStyleSheet("border: none;")
        iconCapturar = QtGui.QIcon()
        iconCapturar.addPixmap(QtGui.QPixmap("./assets/images/capturar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCapturar.setIcon(iconCapturar)
        self.btnCapturar.setIconSize(QtCore.QSize(50, 50))
        self.btnCapturar.setText("")
        self.btnCapturar.setObjectName("btnCapturar")
        self.navLayout.addWidget(self.btnCapturar)
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frameNavegacion)
        self.pushButton_7.setFixedSize(50, 50)
        self.pushButton_7.setStyleSheet("border: none;")
        iconWiki = QtGui.QIcon()
        iconWiki.addPixmap(QtGui.QPixmap("./assets/images/wiki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(iconWiki)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.navLayout.addWidget(self.pushButton_7)
        
        self.pushButton_8 = QtWidgets.QPushButton(self.frameNavegacion)
        self.pushButton_8.setFixedSize(50, 50)
        self.pushButton_8.setStyleSheet("border: none;")
        iconHistorial = QtGui.QIcon()
        iconHistorial.addPixmap(QtGui.QPixmap("./assets/images/historial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(iconHistorial)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.navLayout.addWidget(self.pushButton_8)
        
        # Agregar frame de navegación al layout principal
        self.frameLayout.addWidget(self.frameNavegacion)
        
        # Agregar frame principal al layout principal
        self.mainLayout.addWidget(self.frame)
        
        # Configurar central widget
        NuevoRegistro.setCentralWidget(self.centralwidget)
        
        # Crear y configurar menubar y statusbar
        self.menubar = QtWidgets.QMenuBar(NuevoRegistro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 21))
        self.menubar.setObjectName("menubar")
        NuevoRegistro.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(NuevoRegistro)
        self.statusbar.setObjectName("statusbar")
        NuevoRegistro.setStatusBar(self.statusbar)

        self.retranslateUi(NuevoRegistro)
        QtCore.QMetaObject.connectSlotsByName(NuevoRegistro)

    def retranslateUi(self, NuevoRegistro):
        _translate = QtCore.QCoreApplication.translate
        NuevoRegistro.setWindowTitle(_translate("NuevoRegistro", "Nuevo Registro"))
        self.label.setText(_translate("NuevoRegistro", "CAPTURA"))
        self.labelAcercar.setText(_translate("NuevoRegistro", "Acerca el dispositivo \nlo suficiente a la fuente de audio"))
        self.btnAlmacenamiento.setText(_translate("NuevoRegistro", "Ingresar desde almacenamiento"))
        self.btnAceptarCaptura.setText(_translate("NuevoRegistro", "Aceptar"))