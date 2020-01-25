import re

window = window.get_active_class()
is_chrome = re.search('chrome', window, re.IGNORECASE)

if is_chrome:
  keys = "<ctrl>+u"
  keyboard.send_keys(keys)
