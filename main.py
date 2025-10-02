commands = {
  "create_library": 1,
  "delete_library": 2,
}

commands_descriptions = {
  commands["create_library"]: "Создать новую библиотеку",
  commands["delete_library"]: "Удалить библиотеку новую библиотеку"
}

rendered_commands = "\n".join([f"{commands[command_name]} - {commands_descriptions[commands[command_name]]}" for command_name in commands])

while True:
  command = input('''
      Что вы хотите сделать?
      {rendered_commands}
    '''.format(rendered_commands=rendered_commands))