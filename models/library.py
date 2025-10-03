import uuid
from datetime import datetime

from models.library_item import LibraryItem

class Library:
  id: str
  name: str
  items: list[LibraryItem]
  date_created: datetime
  
  def __init__(
      self,
      name: str,
      id: str | None,
      date_added: datetime | None,
      items: list[LibraryItem] = list()
    ):
      self.name = name
      self.id = id if id is not None else uuid.uuid4()
      self.date_created = date_added if date_added is not None else datetime.now()
      self.items = items

  def add_item(self, item: LibraryItem):
    self.items.append(item)

  def remove_item(self, id: int):
    self.items = list(filter(lambda item: item.id is not id, self.items))

  def show_item(self, id: int):
    filtered_items = list(filter(lambda item: item.id is id, self.items))
    if len(filtered_items) == 0:
      print("Такого элемента не найдено, попробуйте еще")
      return
    found_item = filtered_items[0]
    found_item.show_data()