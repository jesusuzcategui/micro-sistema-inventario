from utils.db import Db
import json

def initTerminal():
  connection = Db()
  lista = connection.list()
  print(lista)
