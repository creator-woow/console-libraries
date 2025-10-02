from datetime import datetime

from models.library_item import LibraryItem

class Book(LibraryItem):
  author: str | None
  genre: str | None
  release_date: datetime | None
  rating: int | None
  number_of_pages: int

  def __init__(
    self,
    name: str,
    id: str | None = None,
    date_added: datetime | None = None,
    author: str | None = None,
    genre: str | None = None,
    release_date: datetime | None = None,
    rating: int | None = None,
    number_of_pages: int = 0
    ):
    super().__init__(
      id=id,
      name=name,
      date_added=date_added
    )
    self.author = author
    self.genre = genre
    self.release_date = release_date
    self.rating = rating
    self.number_of_pages = number_of_pages

  def show_data(self):
    return print(f"Это книга: \"{self.name}\"")
