from models.library_item import LibraryItem

class Video(LibraryItem):
  total_size: int | None = None
  format: str
  duration: int | None = None

  def show_data(self):
    return print("Это видео без перезаписанно метода show_data")
  
  