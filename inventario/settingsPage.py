from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder, Button
from utils.db import Db

connection = Db()

class SettingsPageScreen(Screen):
  def on_button_pressed(self, event: Button.Pressed) -> None:
    event.stop()
    if self._button:
      result = connection.inizialite()
      if(result == True):
        self.notify("Tabla de productos creada")
        self.app.switch_mode("register")
      else:
        self.notify("Ha ocurrido un error")



  def compose(self) -> ComposeResult:
    self._button = Button("Crear tabla de productos", variant="primary")
    yield self._button
    yield Footer();