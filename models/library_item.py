import uuid
from datetime import datetime
from abc import abstractmethod

from lib.library_item import LibraryItemType

class LibraryItem:
  id: str
  parent_id: str
  name: str
  date_created: datetime
  type: LibraryItemType
  
  def __init__(
    self,
    name: str,
    parent_id: str,
    type: LibraryItemType,
    id: str | None,
    date_created: datetime | None
  ):
    self.name = name
    self.type = type
    self.parent_id = parent_id
    self.id = id if id is not None else str(uuid.uuid4())
    self.date_created = date_created if date_created is not None else datetime.now()
  
  @abstractmethod
  def show_data(self):
    print("You need to rewrite this method")

  