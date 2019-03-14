import os
import sys
from conans.util.env_reader import get_env
import colorama
from colorama import Fore, Style

print("CONAN_COLOR_DISPLAY" in os.environ)
print(get_env("CONAN_COLOR_DISPLAY", 1))
print(get_env("PYCHARM_HOSTED"))

if get_env("PYCHARM_HOSTED"):  # in PyCharm disable convert/strip
    colorama.init(convert=False, strip=False)
else:
    colorama.init()

data = "message"
data = "%s%s%s%s" % (Fore.RED, '', data, Style.RESET_ALL)

sys.stdout.write(data)
sys.stdout.flush()
