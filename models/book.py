from datetime import datetime

from lib.library_item import LibraryItemType
from models.library_item import LibraryItem

class Book(LibraryItem):
  author: str | None
  genre: str | None
  release_date: datetime | None
  rating: int | None
  pages_amount: int

  def __init__(
    self,
    name: str,
    parent_id: str,
    id: str | None = None,
    date_created: datetime | None = None,
    author: str | None = None,
    genre: str | None = None,
    release_date: datetime | None = None,
    rating: int | None = None,
    pages_amount: int | None = None
    ):
    super().__init__(
      id=id,
      name=name,
      parent_id=parent_id,
      date_created=date_created,
      type=LibraryItemType.BOOK
    )
    self.author = author
    self.genre = genre
    self.release_date = release_date
    self.rating = rating
    self.pages_amount = pages_amount if pages_amount is not None else 0

  def show_data(self):
    return print(f'''
    Идентификатор: \"{self.id}\"
    Название книги: \"{self.name}\"
    Библиотека родитель \"{self.parent_id}\"
    Автор: \"{self.author}\"
    Жанр: \"{self.genre}\"
    Дата выпука: \"{self.release_date}\"
    Кол-во страниц: {self.pages_amount}
  ''')
