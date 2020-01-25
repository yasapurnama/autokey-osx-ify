import re

window = window.get_active_class()
is_vscode = re.search('code', window, re.IGNORECASE)

if is_vscode:
  keys = "<ctrl>+<shift>+<alt>+<down>"
  keyboard.send_keys(keys)
