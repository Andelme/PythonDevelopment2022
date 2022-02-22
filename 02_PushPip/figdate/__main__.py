import sys
import locale
from figdate import date

prev_locale = locale.getlocale()


locale.setlocale(locale.LC_ALL, "ru_RU")

print(date(*sys.argv[1:]))

locale.setlocale(locale.LC_ALL, prev_locale)
