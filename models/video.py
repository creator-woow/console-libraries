from models.library_item import LibraryItem

class Video(LibraryItem):
  total_size: int # Размер в мб
  format: str
  duration: int # В минутах

  def show_data(self):
    return print("Это видео без перезаписанно метода show_data")
  
  