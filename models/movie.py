from datetime import datetime

from models.video import Video


class Movie(Video):
  director: str | None
  release_date: datetime | None
  rating: int | None
  genre: str | None
  actors: tuple[str] | None
  country: str | None
  budget: int | None
  
  def __init__(
    self,
    name: str,
    director: str | None = None,
    release_date: datetime | None = None,
    rating: int | None = None,
    genre: str | None = None,
    actors: tuple[str] | None = None,
    country: str | None = None,
    budget: int | None = None,
    id: str | None = None,
    date_added: datetime | None = None,
    ):
    super().__init__(
      id=id,
      name=name,
      date_added=date_added
    )
    self.release_date = release_date
    self.director = director
    self.rating = rating
    self.genre = genre
    self.actors = actors
    self.country = country
    self.budget = budget
  
  def show_data(self):
    return print(f"Это фильм: \"{self.name}\"")