import sys
from PySide6.QtWidgets import QApplication
from ui_main import PokeView
from logic import PokeLogic


class AppController:
    def __init__(self):
        self.view = PokeView()
        self.model = PokeLogic()

        # modelo → vista
        self.model.dataLoaded.connect(self.load_grid)
        self.model.detailLoaded.connect(self.view.show_detail)

    def load_grid(self, pokemon_list):
        self.view.populate_grid(pokemon_list, self.model.load_detail)

    def run(self):
        self.view.show()
        self.model.load_pokemon()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = AppController()
    controller.run()

    sys.exit(app.exec())