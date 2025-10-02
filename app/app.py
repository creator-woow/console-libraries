from models.library import Library
from lib.commands import get_user_command, start_create_library, Command

class App():
  libraries: list[Library] = list()
  
  def __init__(self):
    pass
  
  def start_app(self):
    while True:
      print(self.libraries)
      command = get_user_command()
      match command:
        case Command.CREATE_LIBRARY:
          self.libraries.append(start_create_library())
          continue
        # case Command.DELETE_LIBRARY:
        # case Command.ADD_LIBRARY_ITEM:
        # case Command.READ_LIBRARY_ITEM:
        # case Command.EDIT_LIBRARY_ITEM:
        # case Command.DELETE_LIBRARY_ITEM: