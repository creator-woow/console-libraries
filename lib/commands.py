from enum import IntEnum

from models.library import Library

class Command(IntEnum):
  CREATE_LIBRARY = 1
  DELETE_LIBRARY = 2
  READ_LIBRARIES_LIST = 3
  CREATE_LIBRARY_ITEM = 4
  DELETE_LIBRARY_ITEM = 5
  EDIT_LIBRARY_ITEM = 6
  READ_LIBRARY_ITEM = 7
  

class LibraryItemType(IntEnum):
  BOOK = 1
  MAGAZINE = 2
  MOVIE = 3
  MUSIC = 4
  MUSIC_CLIP = 5


commands_descriptions = {
  Command.CREATE_LIBRARY: "Создать новую библиотеку",
  Command.DELETE_LIBRARY: "Удалить библиотеку новую библиотеку",
  Command.READ_LIBRARIES_LIST: "Показать все библиотеки",
  Command.CREATE_LIBRARY_ITEM: "Добавить новый элемент в библиотеку",
  Command.DELETE_LIBRARY_ITEM: "Удалить элемент из библиотеки",
  Command.EDIT_LIBRARY_ITEM: "Редактировать элемент библиотеки",
  Command.READ_LIBRARY_ITEM: "Прочитать элемент библиотеки элемент библиотеки",
}


rendered_commands = "\n".join([f"{command} - {commands_descriptions[command]}" for command in Command])


def get_user_command() -> Command:
  while True:
    command = input("Что вы хотите сделать?\n"  + f"{rendered_commands}\n\n")
  
    if not command.isdigit() or int(command) not in Command:
      print("Такой команды нет! Попробуйте еще раз!\n")
      continue

    return Command(int(command))
   