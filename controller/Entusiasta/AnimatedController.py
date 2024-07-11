from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, pyqtSignal, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor
import math
import random

class AnimatedController(QLabel):
    pressed = pyqtSignal()
    released = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateSignal)
        self.phase = 0
        self.duration = 0

    def mousePressEvent(self, event):
        self.pressed.emit()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.released.emit()
        super().mouseReleaseEvent(event)

    def startAnimation(self, duration):
        self.phase = 0
        self.duration = duration * 60  # Convertir segundos a intervalos de 50 ms
        self.timer.start(20)  # Actualizar cada 20 ms para mayor velocidad

    def stopAnimation(self):
        self.timer.stop()
        self.update()

    def updateSignal(self):
        if self.phase < self.duration:
            self.phase += 2  # Incrementar fase rápidamente
            self.update()
        else:
            self.stopAnimation()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.timer.isActive():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            pen = QPen(QColor(0, 0, 0), 2)
            painter.setPen(pen)

            width = self.width()
            height = self.height()
            num_points = 100
            step = width / num_points
            amplitude = height / 6

            points = []
            for i in range(num_points):
                x = i * step
                # Variar la amplitud y frecuencia para simular una onda de voz
                y = height / 2 + amplitude * math.sin((i + self.phase) * 0.5) * random.uniform(0.5, 1.5)
                points.append(QPointF(x, y))

            painter.drawPolyline(*points)
            painter.end()
