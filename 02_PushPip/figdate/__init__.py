from time import strftime
from pyfiglet import Figlet

default_format = "%Y %d %b %A"
default_font = "graceful"


def date(format = default_format, font = default_font):
    f = Figlet(font = font)
    return f.renderText(strftime(format))
