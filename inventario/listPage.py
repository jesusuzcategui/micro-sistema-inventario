from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Label, DataTable
from utils.db import Db

connection = Db()

class ListPageScreen(Screen):
  def on_mount(self) -> None:
    table = self.query_one(DataTable)
    cols = ("Indice", "Nombre", "Cantidad", "Precio", "Precio venta", "Dueno", "Estatus")
    for col in cols:
      table.add_column(col, key=col)
    
    data = connection.list()
    table.add_rows(data)
    

  def compose(self) -> ComposeResult:
    yield Label("Lista de productos", classes="titlePage")
    yield DataTable(id="productsTable")
    yield Footer();