import sys
import urllib.request as request
from bullscows import gameplay

def ask(prompt: str, valid: list[str] = None) -> str:
    while True:
        guess = input(prompt)

        if (valid is not None) and (guess not in valid):
            continue

        return guess


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

dictionary_path = sys.argv[1]

try:
    f = open(sys.argv[1], "r", encoding='utf8')
    words = f.read().split()
except IOError:
    f = request.urlopen(sys.argv[1])
    words = f.read().decode('utf-8').split()

word_len = 5
if len(sys.argv) > 2:
    word_len = sys.argv[2]

words = [w for w in words if len(w) == word_len]

print(gameplay(ask, inform, words))
