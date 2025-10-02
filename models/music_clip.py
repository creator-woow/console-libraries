from datetime import datetime

from models.video import Video


class MusicClip(Video):
  director: str | None
  singer: str | tuple[str] | None
  release_date: datetime | None
  
  def __init__(
    self,
    name: str,
    director: str | tuple[str] | None,
    singer: str | None,
    release_date: datetime | None,
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
    self.singer = singer
  
  def show_data(self):
    return print("Это музыкальный клип: \"{self.name}\"")