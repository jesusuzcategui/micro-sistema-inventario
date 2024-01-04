from textual.app import App
from .createForm import CreateFormScreen
from .listPage import ListPageScreen
from .settingsPage import SettingsPageScreen

class InventarioApp(App):

  CSS_PATH = "inventario.tcss"

  MODES = {
    "home": ListPageScreen,
    "register": CreateFormScreen,
    "settings": SettingsPageScreen
  }

  BINDINGS = [
    ("h", "switch_mode('home')", "Lista de Productos"),
    ("r", "switch_mode('register')", "Registrar producto"),
    ("s", "switch_mode('settings')", "Ajustes")
  ]

  def on_mount(self) -> None:
    self.switch_mode('register')