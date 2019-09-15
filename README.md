# Soldiers exercises

Przećwicz z żołnierzami musztrę.
Wczuj się w rolę dowodzącego.

Dzisiaj jest idealny dzień na trening.

Wojsko może mieć bardzo dużo różnych układów.
Nie ma ograniczonej liczby żołnierzy
ich liczba i umieszczenie może być różne.

```↑ ```- reprezentuje pojedyńczego żołnierza i jego kierunek w jakim patrzy

```" "``` - puste miejsce na które może wejść żółnierz

```[
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "]
]
```
 -Pole po jakim poruszają się żołnierze

Aby uruchomić program najpierw:

```
pipenv install
pipenv run orders
```

------------------------------------------
Komunikujesz się z wojskiem za pomoca poniższych komend:

Bazowe komendy:
- "Turn left!",
- "Turn right!",
- "Turn backward!",
- "Go forward!",
- "Go forward n step!",
- "Turn to me!" - wszyscy odwracają się do Ciebie czyli na górę planszy
- "Go scatter" - rozproszyć się

Jest możliwe także wydawanie rozkazów poszczególnym kolumnom i rzędom:
- "nth row, ",
- "nth column, ",
- "Even rows, ",
- "Even columns, ",
- "Odd rows, ",
- "Odd columns, "
Te komendy są wstawiane na początku rozkazów dla wojska.
Na przykład:

command:"1st row, Turn backward!"
```
[" "," "," "," "," "," "," "] wiersz
[" "," "," "," "," "," "," "]  |
[" "," "," "," "," "," "," "]  v
[" "," ","↑","↑","↑"," "," "]  1
[" "," ","↓","↓","↓"," "," "]  2
[" "," ","↓","↓","↓"," "," "]  3
[" "," "," "," "," "," "," "]
          |   |   |
kolumna-> 1   2   3
```

Żołnierze mogą być rozproszeni

Na przykład:
```
[" "," "," "," "," "," "," "],wiersz
[" ","↑","→"," "," ","→"," "], 1
[" "," "," "," "," ","↓"," "], 2
[" "," "," "," "," "," "," "],
[" ","↑"," "," "," "," "," "], 3
[" ","←"," "," ","←","↓"," "], 4
[" "," "," "," "," "," "," "]
kol   1   2       3   4
```

Wiersze są liczone od góry planszy.
Kolumny od lewej.
Numery kolumn i wierszy nie są jednoznaczne z POLEM
po którym poruszają się żołnierze, a z położenia żołnierzy.

command:"Turn on me!"
```
[" "," "," "," "," "," "," "] wiersz
[" "," "," "," "," "," "," "]  |
[" "," "," "," "," "," "," "]  v
[" "," ","↑","↑","↑"," "," "]  1
[" "," ","↑","↑","↑"," "," "]  2
[" "," ","↑","↑","↑"," "," "]  3
[" "," "," "," "," "," "," "]
          |   |   |
kolumna-> 1   2   3
```


Pamiętaj że kierunek żółnierza się zmienia
Gdy dajesz mu komende `Turn left` to on idzie
w lewo względem aktualnego kieurnku w którym patrzy.

Na przykład:

command:"3rd row, Go left!"
```
[" "," "," "," "," "," "," "] wiersz
[" "," "," "," "," "," "," "]  |
[" "," "," "," "," "," "," "]  v
[" "," ","↑","↑","↑"," "," "]  1
[" "," ","↓","↓","↓"," "," "]  2
[" "," "," ","→","→","→"," "]  3
[" "," "," "," "," "," "," "]
          |   |   |
kolumna-> 1   2   3
```

`Ważne`
- Jeżeli na pole na które powinien wejść
żółnierz jest zajęte to nie wykonuje danego rozkazu.
- Gdy rozkaz wymaga wyjście poza pole wtedy także komenda nie jest wykonywana.