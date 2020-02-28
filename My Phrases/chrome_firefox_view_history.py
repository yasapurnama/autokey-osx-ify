import re

window = window.get_active_class()
is_chrome = re.search('chrome', window, re.IGNORECASE)
is_firefox = re.search('firefox', window, re.IGNORECASE)

if is_chrome or is_firefox:
  keys = "<ctrl>+h"
  keyboard.send_keys(keys)
