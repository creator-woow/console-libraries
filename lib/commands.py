from enum import IntEnum

from models.library import Library

class Command(IntEnum):
  CREATE_LIBRARY = 1
  DELETE_LIBRARY = 2
  ADD_LIBRARY_ITEM = 3
  DELETE_LIBRARY_ITEM = 4
  EDIT_LIBRARY_ITEM = 5
  READ_LIBRARY_ITEM = 6


commands_descriptions = {
  Command.CREATE_LIBRARY: "Создать новую библиотеку",
  Command.DELETE_LIBRARY: "Удалить библиотеку новую библиотеку",
  Command.ADD_LIBRARY_ITEM: "Добавить новый элемент в библиотеку",
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
   

def start_create_library():
  library_name = ""
  
  while True:
    library_name = input("\nВведите имя библиотеки: ")
    if library_name == "" or library_name.isdigit():
      print("\nИмя библотеки должно начинаться с латинской буквы!\n")
      continue
    break
  
  new_library = Library(name=library_name)

  print(f"Библиотека \"{new_library.name}\" была успешно создана!\n")

  return new_library