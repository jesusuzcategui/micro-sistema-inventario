from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Static, Input, Button, Log, Select
from rich.table import Table
from utils.db import Db
import json


connection = Db()


class CreateFormScreen(Screen):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        event.stop()
        if self._button:
            data = {
                "name": self._name.value,
                "price": self._price.value,
                "price_sale": self._price_sale.value,
                "stock": self._stock.value,
                "owner": self._onwer.value
            }

            log = self.query_one(Log)

            connection.inizialite()
            result = connection.create(
                data["name"],
                int(data["stock"]),
                int(data["price"]),
                int(data["price_sale"]),
                int(data["owner"])
            )

            log.write_line(json.dumps(result))

    def compose(self) -> ComposeResult:

        CSS_PATH = "inventario.tcss"

        self._name = Input(
            placeholder="Nombre de producto",
            id="product_name",
            classes="inputPage"
        )

        self._button = Button(
            "▶︎ Guardar",
            id="guardar_product",
            variant="primary",
            classes="buttonPage"
        )

        self._stock = Input(
            placeholder="Cantidad de existencias",
            id="product_stock",
            classes="inputPage"
        )

        self._onwer = Select(
            classes="inputPage",
            options=[
                ("Tia chavela", 1),
                ("Mia", 2)
            ],
            id="product_owner"
        )

        self._price = Input(
            classes="inputPage",
            id="product_price",
            placeholder="Precio"
        )

        self._price_sale = Input(
            classes="inputPage",
            id="product_price_sale",
            placeholder="Precio venta"
        )

        yield Static("Crear Producto", classes="titlePage")
        yield self._name
        yield self._stock
        yield self._onwer
        yield self._price
        yield self._price_sale
        yield self._button
        yield Log()
        yield Footer()
