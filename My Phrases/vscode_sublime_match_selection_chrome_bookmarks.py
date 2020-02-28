import re

window = window.get_active_class()
is_vscode = re.search('code', window, re.IGNORECASE)
is_sublime = re.search('sublime', window, re.IGNORECASE)
is_chrome = re.search('chrome', window, re.IGNORECASE)

if is_vscode or is_sublime or is_chrome:
  keys = "<ctrl>+d"
  keyboard.send_keys(keys)
