from enum import IntEnum

class LibraryItemType(IntEnum):
  BOOK = 1
  MAGAZINE = 2
  MOVIE = 3
  MUSIC_CLIP = 4

library_item_type_description = {
  LibraryItemType.BOOK: "Книга",
  LibraryItemType.MAGAZINE: "Журнал",
  LibraryItemType.MOVIE: "Фильм",
  LibraryItemType.MUSIC_CLIP: "Музыкальный клип",
}

rendered_library_item_type_variants = "\n".join([f"{type} - {library_item_type_description[type]}" for type in LibraryItemType])