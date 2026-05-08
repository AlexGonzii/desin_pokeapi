from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QScrollArea, QDialog
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests


class DetailDialog(QDialog):
    def __init__(self, detail):
        super().__init__()
        self.setWindowTitle(detail["name"])

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Nombre: {detail['name']}"))
        layout.addWidget(QLabel(f"Altura: {detail['height']}"))
        layout.addWidget(QLabel(f"Peso: {detail['weight']}"))
        layout.addWidget(QLabel(f"Tipos: {', '.join(detail['types'])}"))

        self.setLayout(layout)


class PokeView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pokédex")
        self.resize(600, 800)

        self.layout = QVBoxLayout()

        self.scroll = QScrollArea()
        self.container = QWidget()
        self.grid = QGridLayout()

        self.container.setLayout(self.grid)
        self.scroll.setWidget(self.container)
        self.scroll.setWidgetResizable(True)

        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)

        self.buttons = []

    def populate_grid(self, pokemon_list, on_click):
        cols = 2

        for i, p in enumerate(pokemon_list):
            row = i // cols
            col = i % cols

            btn = QPushButton(p["name"])
            btn.setFixedHeight(120)

            # cargar imagen
            image_data = requests.get(p["image"]).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            label = QLabel()
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)

            container = QVBoxLayout()
            container.addWidget(label)
            container.addWidget(btn)

            wrapper = QWidget()
            wrapper.setLayout(container)

            btn.clicked.connect(lambda _, pid=p["id"]: on_click(pid))

            self.grid.addWidget(wrapper, row, col)
            self.buttons.append(btn)

    def show_detail(self, detail):
        dialog = DetailDialog(detail)
        dialog.exec()