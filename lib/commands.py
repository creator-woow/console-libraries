from enum import IntEnum
class Command(IntEnum):
  CREATE_LIBRARY = 1
  READ_LIBRARIES_LIST = 2
  DELETE_LIBRARY = 3
  CREATE_LIBRARY_ITEM = 4
  DELETE_LIBRARY_ITEM = 5
  EDIT_LIBRARY_ITEM = 6
  READ_LIBRARY_ITEM = 7
  READ_LIBRARY_ITEMS = 8


commands_descriptions = {
  Command.CREATE_LIBRARY: "Создать новую библиотеку",
  Command.READ_LIBRARY_ITEMS: "Показать все элементы библиотеки",
  Command.DELETE_LIBRARY: "Удалить библиотеку новую библиотеку",
  Command.READ_LIBRARIES_LIST: "Показать все библиотеки",
  Command.CREATE_LIBRARY_ITEM: "Создать новый элемент в библиотеке",
  Command.DELETE_LIBRARY_ITEM: "Удалить элемент из библиотеки",
  Command.EDIT_LIBRARY_ITEM: "Редактировать элемент библиотеки",
  Command.READ_LIBRARY_ITEM: "Прочитать элемент библиотеки",
}


rendered_commands = "\n".join([f"{command} - {commands_descriptions[command]}" for command in Command])


def get_user_command() -> Command:
  while True:
    command = input("Что вы хотите сделать?\n"  + f"{rendered_commands}\n\n")
  
    if not command.isdigit() or int(command) not in Command:
      print("Такой команды нет! Попробуйте еще раз!\n")
      continue

    return Command(int(command))
   