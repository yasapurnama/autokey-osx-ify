import re

keys = "<ctrl>+w"

window = window.get_active_class()
is_terminal = re.search('term', window, re.IGNORECASE)

if is_terminal:
  keys = "<shift>+" + keys

keyboard.send_keys(keys)
