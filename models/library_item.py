import uuid
from datetime import datetime
from abc import abstractmethod

class LibraryItem:
  id: str
  name: str
  date_added: datetime
  
  def __init__(
    self,
    name: str,
    id: str | None,
    date_added: datetime | None
  ):
    self.name = name
    self.id = id if id is not None else uuid.uuid4()
    self.date_added = date_added if date_added is not None else datetime.now()
  
  @abstractmethod
  def show_data(self):
    print("You need to rewrite this method")

  