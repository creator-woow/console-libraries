from datetime import datetime

from lib.library_item import LibraryItemType
from models.video import Video


class MusicClip(Video):
  director: str | None
  singer: str | tuple[str] | None
  release_date: datetime | None
  
  def __init__(
    self,
    name: str,
    parent_id: str,
    director: str | tuple[str] | None,
    singer: str | None,
    release_date: datetime | None,
    id: str | None = None,
    date_added: datetime | None = None,
    ):
    super().__init__(
      id=id,
      parent_id=parent_id,
      name=name,
      date_created=date_added,
      type=LibraryItemType.MUSIC_CLIP
    )
    self.release_date = release_date
    self.director = director
    self.singer = singer
  
  def show_data(self):
    return print("Это музыкальный клип: \"{self.name}\"")