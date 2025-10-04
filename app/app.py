from models.library import Library
from models.library_item import LibraryItem
from models.book import Book
from models.magazine import Magazine
from models.movie import Movie
from models.music_clip import MusicClip
from lib.commands import get_user_command, Command
from lib.library_item import LibraryItemType, library_item_type_description, rendered_library_item_type_variants

class App():
  libraries: list[Library] = list()

  def handle_menu_select(self):
    while True:
      command = get_user_command()
      match command:
        case Command.CREATE_LIBRARY:
          self.__create_library()
          continue
        case Command.READ_LIBRARIES_LIST:
          self.__show_libraries_list()
          continue
        case Command.READ_LIBRARY_ITEMS:
          self.__show_library_items()
          continue
        case Command.CREATE_LIBRARY_ITEM:
          self.__create_library_item()
          continue
        case Command.READ_LIBRARY_ITEM:
          self.__show_library_item()
        # case Command.DELETE_LIBRARY:
        # case Command.EDIT_LIBRARY_ITEM:
        # case Command.DELETE_LIBRARY_ITEM:

  def __find_library(self):
    if len(self.libraries) == 0:
      print("\nНи одной библиотеки еще не существует! Создайте новую!\n")
      return None

    find_library: Library

    while True:
      input_library_id = input("\nУкажите id библиотеки: ").strip()
      if input_library_id == "":
        print("\nВведен не корректный id! Попробуйте еще раз!\n")
        continue
      find_libraries = tuple(filter(lambda library: library.id == input_library_id, self.libraries))
      if len(find_libraries) == 0:
        print("\nБиблиотеки с таким id не существует! Попробуйте другой id!\n")
        continue
      find_library = find_libraries[0]
      break

    return find_library     
  
  def __find_library_item(self, library: Library):
    if len(library.items) == 0:
      print("\nНи одного элемента в библиотеке не содержиться! Добавьте элементы!\n")
      return None

    input_library_item_id: str
    
    while True:
      input_library_item_id = input("\nID элемента библиотеки: ")
      if input_library_item_id == "":
        print("\nВведен не корректный id! Попробуйте еще раз!\n")
        continue
      break
    
    find_items = tuple(filter(lambda item: item.id == input_library_item_id, library.items))
    if len(find_items) == 0:
      print("\nВведен не корректный id! Попробуйте еще раз!\n")
      return None
    return find_items[0]

  def __show_libraries_list(self):
    if len(self.libraries) == 0:
      print("\nНи одно библиотеки не обнаруженно! Попробуйте добавить новую!\n")
      return
    print(
      f"\n{"\n\n".join([f"Идентификатор: \"{library.id}\"\nИмя: \"{library.name}\"\nДата создания: {library.date_created.strftime("%Y-%m-%d %H:%M")}" for library in self.libraries])}\n"
    )
  
  def __show_library_items(self):
    target_library = self.__find_library()
    if len(target_library.items) == 0:
      print("\nНи одного элемента библиотеки не обнаруженно! Попробуйте добавить новый элемент!\n")
      return
    print(
      f"\n{"\n\n".join([f"Библиотека родитель: \"{target_library.name}\" - \"{target_library.id}\"\nТип элемента: \"{library_item_type_description[item.type]}\"\nИдентификатор: \"{item.id}\"\nИмя: \"{item.name}\"\nДата создания: {item.date_created.strftime("%Y-%m-%d %H:%M")}" for item in target_library.items])}\n"
    )
    
  def __show_library_item(self):
    target_library = self.__find_library()
    if target_library == None:
      return
    library_item = self.__find_library_item(target_library)
    if library_item == None:
      return
    library_item.show_data()

  def __create_library_item(self):
    find_library = self.__find_library()

    if find_library == None:
      return

    library_item_name = ""
    library_item_type: LibraryItemType
  
    while True:
      while True:
        print("\n" + rendered_library_item_type_variants)
        input_item_type = input("\nВыберите тип создаваемого элемента библиотеки: ").strip()
        if input_item_type == "" or not input_item_type.isdigit() or int(input_item_type) not in LibraryItemType:
          print("\nТип создаваемого элемента не верен! Попробуйте еще раз!\n")
          continue
        library_item_type = LibraryItemType(int(input_item_type))
        break

      while True:
        library_item_name = input("\nВведите имя нового элемента библиотеки: ").strip()
        if library_item_name == "" or library_item_name.isdigit():
          print("\nИмя элемента библотеки должно начинаться с латинской буквы и не может быть пустым!\n")
          continue
        break
        
      find_library_items = tuple(filter(
        lambda library_item: library_item.name == library_item_name and library_item.type == library_item_type,
        find_library.items
      ))
      
      if len(find_library_items) > 0:
        print(f"\nЭлемент библиотеки \"{find_library.name}\" c именем \"{library_item_name}\" и типом \"{library_item_type_description[library_item_type]}\" уже существует. В библиотеке не может содержаться дублирование имен элементов одного типа! Попробуйте еще раз!\n")
        continue
      break
    
    created_library_item: LibraryItem
    
    match library_item_type:
      case LibraryItemType.BOOK:
        created_library_item = self.__create_book(parent_id=find_library.id, name=library_item_name)
      case LibraryItemType.MAGAZINE:
        pass
      case LibraryItemType.MOVIE:
        pass
      case LibraryItemType.MUSIC_CLIP:
        created_library_item = self.__create_music_clip(parent_id=find_library.id, name=library_item_name)
      
    target_library: Library
    
    for library in self.libraries:
      if library.id == find_library.id:
        target_library = library
      
    target_library.items.append(created_library_item)
    print(f"\nВ библиотеку \"{target_library.name}\" был успешно добавлен новый элемент с типом \"{library_item_type_description[created_library_item.type]}\" и именем \"{created_library_item.name}\"\n")

        
  def __create_book(self, parent_id: str, name: str):
    user_input = {
      "author": None,
      "genre": None,
      "release_date": None,
      "rating": None,
      "pages_amount": None,
    }
    
    user_input["author"] = input("Автор книги: ")
    user_input["genre"] = input("Жанр книги: ")
    user_input["release_date"] = input("Дата выпуска книги: ")
    pages_amount_input = input("Кол-во страниц в книге: ")
    rating_input = input("Рейтинг книги: ")

    user_input["rating"] = int(rating_input) if rating_input != "" and rating_input.isdigit() else None
    user_input["pages_amount"] = int(pages_amount_input) if pages_amount_input != "" and pages_amount_input.isditig() else None

    for key in user_input:
      if user_input[key] == "":
        user_input[key] = None

    return Book(
      name=name,
      parent_id=parent_id,
      **user_input
    )
    
  def __create_music_clip(self, parent_id: str, name: str):
    user_input = {
      "director": None,
      "singer": None,
      "release_date": None,
    }
    
    user_input["director"] = input("Режисер: ")
    user_input["singer"] = input("Певец: ")
    user_input["release_date"] = input("Дата выпуска книги: ")

    for key in user_input:
      if user_input[key] == "":
        user_input[key] = None

    return MusicClip(
      name=name,
      parent_id=parent_id,
      **user_input
    )
        
  def __create_library(self):
    library_name = ""

    while True:
        library_name = input("\nВведите имя библиотеки: ").strip()
        if library_name == "" or library_name.isdigit():
          print("\nИмя библотеки должно начинаться с латинской буквы!\n")
          continue
        saved_libraries_names = tuple(map(lambda library: library.name,  self.libraries))
        if library_name in saved_libraries_names:
          print(f"\n\nБиблиотека с именем \"{library_name}\" уже существует! Имена библиотек должны быть уникальными!\n")
          continue
        break

    new_library = Library(
      id=None,
      date_added=None,
      name=library_name,
      
    )
    print(f"Библиотека \"{new_library.name}\" была успешно создана!\n")

    self.libraries.append(new_library)