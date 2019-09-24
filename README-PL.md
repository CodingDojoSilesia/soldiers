# Soldiers exercises

Aby uruchomić program najpierw:

```
pipenv install --dev
pipenv run orders
```

Pojawi się program do zarządzania wojskiem

------------------------------------------

Przećwicz z żołnierzami musztrę.
Wczuj się w rolę dowodzącego.

Wojsko może mieć bardzo dużo różnych układów.
Nie ma ograniczonej liczby żołnierzy
ich liczba i umieszczenie może być różne.

```↑ ```- reprezentuje pojedyńczego żołnierza i jego kierunek w jakim patrzy

```" "``` - puste miejsce

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
 -Pole do ćwiczeń po jakim poruszają się żołnierze

------------------------------------------


Komunikujesz się z wojskiem za pomoca poniższych komend:

W zależności od zaawansowania żołnierze potrafią reagować na różne komendy:

Początkowe położenie żołnierzy to:
```
[
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," ","↑","↑","↑"," "," "],
[" "," ","↑","↑","↑"," "," "],
[" "," ","↑","↑","↑"," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "]
]
```

#### Żółtodzioby:

Żółtodzioby są słabo wytrenowanie i mogą wchodzić na siebie.
Zdarza im się także wychodzić poza pole do ćwiczeń i nie wracać.

- "Turn left!" - `←` wszyscy odwracają się w lewo
- "Turn right!" -  `→` wszyscy odwracają się w prawo,
- "Turn backward!" -  `↓` wszyscy odwracają się do tyłu,
- "Go forward!" - wszyscy idą o jeden krok w kierunku jakim są zwróceni
- "Go forward n step!", - wszyscy idą o `n` kroków w kierunku jakim są zwróceni
- "Turn to me!" - `↑` wszyscy odwracają się do dowodzącego czyli na górę planszy
- "Go scatter" - rozproszyć się - wszyscy zmieniają położenie:
  - losowo wybrany element planszy,
  - odwróceni w losowym kierunku

#### Szeregowi:

Żółtodzioby po poznaniu wszystkich komend stają się szeregowymi.
Szeregowi wiedzą, że na pole gdzie ktoś już stoi nie powinno sie się wchodzić.
Stoją w miejscu, gdy rozkaz wymaga wejścia na kogoś.

Są wytrwali i nigdy nie uciekają z pola ćwiczeń.
Gdy rozkaz wymaga wyjścia poza pole do ćwiczeń to stawają na ostatnim możliwym polu.

Poza tym potrafią rozpoznawać do którego rzędu lub kolumny należą.

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

Gdy są rozproszeni to wciąż mają świetną orientację:

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

Dzięki temu są w stanie rozpoznawać więcej komend:

- "1th row, ", "2nd row, ", "3rd row, ", "nth row",
- "1th column, ", "2nd column, ", "3rd column, ",
- "Even rows, ",
- "Even columns, ",
- "Odd rows, ",
- "Odd columns, "

Te komendy są wstawiane na początku rozkazów dla wojska:

command:"3rd row, Go right!"
```
[" "," "," "," "," "," "," "] wiersz
[" "," "," "," "," "," "," "]  |
[" "," "," "," "," "," "," "]  v
[" "," ","↑","↑","↑"," "," "]  1
[" "," ","↑","↑","↑"," "," "]  2
[" "," "," ","→","→","→"," "]  3
[" "," "," "," "," "," "," "]
          |   |   |
kolumna-> 1   2   3
```

### Wyjadacze
Wyjadacze mają lepsze zoreintowanie w kierunkach. Potrafią wszystko co źółtodzioby i szeregowi.
Różnią się od nich tym, że obracają się w kierunkach względem aktualnego położenia.

Gdy dajesz im komendę `Turn left` to idą
w lewo względem aktualnego kierunku w którym patrzy.

Zadanie zostało stworzone na podstawie:
https://www.codewars.com/kata/57e23d378a8b8de758000b41