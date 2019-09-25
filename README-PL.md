# Soldiers exercises

Aby uruchomić program najpierw:

```
pip install pipenv

pipenv run orders
```

Pojawi się program do zarządzania wojskiem.
Wprowadzasz klawiaturą komendy tekstowe i widzisz w konsoli jak żółnierze zinterpretowali Twój rozkaz.
Na początku ćwiczysz żóltodziobów, którzy nie mają pojęcia co do nich mówisz.
Twoim zadaniem jest nauczenie ich co znaczą poszczególne komendy.

Możesz z nimi ćwiczyć pojedyńcze komendy przez testy:
```
pipenv install --dev
pipenv run tests
```

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


W zależności od zaawansowania żołnierze potrafią reagować na różne komendy.

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

#### Greenhorns:

Greenhorn wiedzą, że na pole gdzie ktoś już stoi nie powinno sie się wchodzić.
Stoją w miejscu, gdy rozkaz wymaga wejścia na kogoś.
Zdarza im się jednak wychodzić poza pole do ćwiczeń i nie wracać.

- "Turn West!" - `←` wszyscy odwracają się w lewo
- "Turn East!" -  `→` wszyscy odwracają się w prawo,
- "Turn South!" -  `↓` wszyscy odwracają się do tyłu,
- "Go forward!" - wszyscy idą o jeden krok w kierunku jakim są zwróceni
- "Go forward n step!", - wszyscy idą o `n` kroków w kierunku jakim są zwróceni
- "Turn to me!" - `↑` wszyscy odwracają się do dowodzącego czyli na górę planszy
- "Go scatter" - rozproszyć się - wszyscy zmieniają położenie:
  - losowo wybrany element planszy,
  - odwróceni w losowym kierunku,
  - nie jest zabrionione by powrócił na swoje poprzednie miejsce i kierunek patrzenia.

#### Corporals:

Greenhorn po poznaniu wszystkich komend stają się corporal.

Są wytrwali i nigdy nie uciekają z pola ćwiczeń.
Gdy rozkaz wymaga wyjścia poza pole to stawają na ostatnim możliwym polu.

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

- "1st row, ", "2nd row, ", "3rd row, ", "nth row",
- "1st column, ", "2nd column, ", "3rd column, ", "nth column"
- "Even rows, ",
- "Even columns, ",
- "Odd rows, ",
- "Odd columns, "

Te komendy są wstawiane na początku rozkazów dla wojska:

command:"3rd row, Turn East!"
```
[" "," "," "," "," "," "," "] wiersz
[" "," "," "," "," "," "," "]  |
[" "," "," "," "," "," "," "]  v
[" "," ","↑","↑","↑"," "," "]  1
[" "," ","↑","↑","↑"," "," "]  2
[" "," ","→","→","→"," "," "]  3
[" "," "," "," "," "," "," "]
          |   |   |
kolumna-> 1   2   3
```

### Sergeants
Sergeant potrafi wszystko co greenhorn i corporal.
Mają szczególną umiejętność jaką jest rozpoznawanie kierunków.
Potrafią obracać się w kierunkach względem aktualnego położenia.

- "Turn left!"
- "Turn right!"
- "Turn backward!"

Na przykład

```
[" "," "," "," "," "," "," "]
[" "," "," "," "," "," "," "]
[" "," "," "," "," "," "," "]
[" "," ","↑","↑","↑"," "," "]
[" "," ","↓","↓","↓"," "," "]
[" "," ","↓","↓","↓"," "," "]
[" "," "," "," "," "," "," "]
```
"Turn left!"
```
[" "," "," "," "," "," "," "]
[" "," "," "," "," "," "," "]
[" "," "," "," "," "," "," "]
[" "," ","←","←","←"," "," "]
[" "," ","→","→","→"," "," "]
[" "," ","→","→","→"," "," "]
[" "," "," "," "," "," "," "]
```

Rozpoznają także komendy:

- "Stand still!" - każda następna komenda jest ignorowana
- "Move your asses!" - żołnierze przestają ignorować komendy

Możesz oczywiście wybrać wiersz lub kolumnę dla tych komend.

Zadanie zostało stworzone na podstawie:
https://www.codewars.com/kata/57e23d378a8b8de758000b41