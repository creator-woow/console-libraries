import uuid
from datetime import datetime
from abc import abstractmethod

from lib.commands import LibraryItemType

class LibraryItem:
  id: str
  name: str
  date_added: datetime
  type: LibraryItemType
  
  def __init__(
    self,
    name: str,
    type: LibraryItemType,
    id: str | None,
    date_added: datetime | None
  ):
    self.name = name
    self.type = type
    self.id = id if id is not None else uuid.uuid4()
    self.date_added = date_added if date_added is not None else datetime.now()
  
  @abstractmethod
  def show_data(self):
    print("You need to rewrite this method")

  