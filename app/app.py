from models.library import Library
from models.library_item import LibraryItem
from lib.commands import get_user_command, LibraryItemType

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
        case Command.CREATE_LIBRARY_ITEM:
          self.__create_library_item()
          continue
        # case Command.DELETE_LIBRARY:
        # case Command.READ_LIBRARY_ITEM:
        # case Command.EDIT_LIBRARY_ITEM:
        # case Command.DELETE_LIBRARY_ITEM:|

  def __show_libraries_list(self):
    if len(self.libraries) == 0:
      print("\nНи одно библиотеки не обнаруженно! Попробуйте добавить новую!\n")
      return
    print(
      f"\n{"\n\n".join([f"Идентификатор: {library.id}\nИмя: \"{library.name}\"\nДата создания: {library.date_created.strftime("%Y-%m-%d %H:%M")}" for library in self.libraries])}\n"
    )

  def __create_library_item(self):
    target_library: Library
    
    while True:
      input_library_id = input("\nУкажите id библиотеки в которой вы хотите создать новый элемент: ").strip()
      if input_library_id == "" or not input_library_id.isdigit():
        print("\nВведен не корректный id! Попробуйте еще раз!\n")
        continue
      find_libraries = tuple(filter(lambda library: library.id == input_library_id, self.libraries))
      if len(find_libraries) == 0:
        print("\nБиблиотеки с таким id не существует! Попробуйте другой id!\n")
        continue
      target_library = find_libraries[0]
      break

    library_item_name = ""
    library_item_type: LibraryItemType
  
    while True:
      while True:
        input_item_type = input("\nВыберите тип создаваемого элемента библиотеки: ").strip()
        if input_item_type == "" or not input_item_type.isdigit() or int(input_item_type) not in LibraryItemType:
          print("\nТип создаваемого элемента не верен! Попробуйте еще раз!\n")
          continue
        library_item_type = LibraryItemType(int(input_item_type))
        break

      while True:
        library_item_name = input("\nВведите имя нового элемента библиотеки: ").strip()
        if library_item_name == "" or library_item_name.isdigit():
          print("\nИмя элемента библотеки должно начинаться с латинской буквы!\n")
          continue
        break
        
      find_library_items = filter(
        lambda library_item: library_item.name == library_item_name and library_item.type == library_item_type,
        target_library.items
      )
      
      if len(find_library_items) > 0:
        print(f"\nЭлемент библиотеки \"{target_library.name}\" c именем \"{library_item_name}\" и типом \"{library_item_type}\" уже существует. В библиотеке не может содержаться дублирование имен элементов определенного типа! Попробуйте еще раз!\n")
        continue

        
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