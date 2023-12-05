# dużym błędem jest testowanie kodu za pomocą funkcji input

# testy jednostkowe stosujemy dla sytuacji brzegowych

# asercja - warunek (predykat), którego spełnienie
# jest zakładane w danym miejscu kodu

# test regresyjny - sprawdza, czy zmiana nie popsuła
# działającego kodu

def division(a, b):
    if b == 0:
        # raise - rzuca wyjątek (wartość) podany jako argument
        raise ZeroDivisionError
    else:
        return a / b

# TDD - test driven development
