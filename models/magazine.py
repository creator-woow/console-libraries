from datetime import datetime

from lib.library_item import LibraryItemType
from models.library_item import LibraryItem

class Magazine(LibraryItem):
  issue_number: int | None
  release_date: datetime | None
  distributor: str | None
  editor: str | None
  number_of_page: int
  
  def __init__(
    self,
    name: str,
    parent_id: str,
    issue_number: int | None  = None,
    release_date: datetime | None  = None,
    distributor: str | None  = None,
    editor: str | None  = None,
    number_of_page: int | None  = None,
    date_added: datetime | None = None,
    id: str | None = None,
    ):
    super().__init__(
      id=id,
      name=name,
      parent_id=parent_id,
      date_created=date_added,
      type=LibraryItemType.MAGAZINE
    )
    self.release_date = release_date
    self.issue_number = issue_number
    self.distributor = distributor
    self.editor = editor
    self.number_of_page = number_of_page if number_of_page is not None else 0
  
  def show_data(self):
    return print(f"Это журнал: \"{self.name}\"")