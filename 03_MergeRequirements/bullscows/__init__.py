import textdistance as td
import random

def bullscows(guess: str, secret: str) -> (int, int):
    bulls = td.hamming.similarity(guess, secret)
    cows = td.bag.similarity(guess, secret) - bulls
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)

    count = 0
    secret_len = len(secret)
    while True:
        guess = ask("Введите слово: ", words)

        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)

        count += 1
        if bulls == secret_len:
            return count
