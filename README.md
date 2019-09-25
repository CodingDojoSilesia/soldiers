# Soldiers exercises

To run program enter :

```
pip install pipenv
pipenv run orders
```

You have just launched a military management program

You enter text commands on the keyboard and see in the console how the soldiers have interpreted your order.
At the beginning you practice greenhorns who have no idea what you are talking about.
Your task is to teach them what individual commands mean.

You can practice individual commands with them through tests:
```
pipenv install --dev
pipenv run tests
```

----------------------------------------------------

Practice the exercises with the soldiers.
Check yourself in the role of commanding officer?

The army can have many different systems.
There are no limited number of soldiers
their number and placement may be different.

```↑ ```- represents a single soldier and his direction in which he looks

```" "``` - empty place

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
 - Exercise field along which soldiers move

------------------------------------------


 Depending on their ranks, soldiers can respond to various commands.
The initial location of the soldiers is:

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

The Greenhorns know that they shouldn't enter on a field where someone is already standing.
They stand still when the order requires someone to step on.
However, sometimes they leave the field never to be seen again.

- "Turn West!" - `←` everybody turns left,
- "Turn East!" -  `→` everybody turns right,
- "Turn South!" -  `↓` everybody turns back,
- "Go forward!" - everyone goes one step in the direction they are facing
- "Go forward n step!","Go forward n steps!" - everybody goes `n` steps in the direction they are facing
- "Turn to me!" - `↑` everybody turns to the commanding person that is on the board top
- "Go scatter" - get distracted - everybody changes their position:
  - randomly selected board element,
  - turned in a random direction,
  - it is not forbidden to return to his previous place and direction.

#### Corporals:

Greenhorns after learning all commands become corporals.
They are persistent and never run from the field of exercises.
When the order requires going out of the box, they stand on the last possible space.

In addition, we can recognize rows of configuration columns or rows.

```
[" "," "," "," "," "," "," "] row
[" "," "," "," "," "," "," "]  |
[" "," "," "," "," "," "," "]  v
[" "," ","↑","↑","↑"," "," "]  1
[" "," ","↓","↓","↓"," "," "]  2
[" "," ","↓","↓","↓"," "," "]  3
[" "," "," "," "," "," "," "]
          |   |   |
column -> 1   2   3
```

When they are scattered, they still have a great orientation:

```
[" "," "," "," "," "," "," "],row
[" ","↑","→"," "," ","→"," "], 1
[" "," "," "," "," ","↓"," "], 2
[" "," "," "," "," "," "," "],
[" ","↑"," "," "," "," "," "], 3
[" ","←"," "," ","←","↓"," "], 4
[" "," "," "," "," "," "," "]
column1   2       3   4
```

Thanks to this they are able to recognize more commands:

- "1st row, ", "2nd row, ", "3rd row, ", "nth row",
- "1st column, ", "2nd column, ", "3rd column, ",
- "Even rows, ",
- "Even columns, ",
- "Odd rows, ",
- "Odd columns, "

These commands are inserted at the beginning of the military orders:

command:"3rd row, Turn East!"
```
[" "," "," "," "," "," "," "] row
[" "," "," "," "," "," "," "]  |
[" "," "," "," "," "," "," "]  v
[" "," ","↑","↑","↑"," "," "]  1
[" "," ","↑","↑","↑"," "," "]  2
[" "," "," ","→","→","→"," "]  3
[" "," "," "," "," "," "," "]
          |   |   |
column -> 1   2   3
```

### Sergeants
Sergeants can do anything like greenhorn and corporal.
They have a special skill which is recognizing directions.
They can rotate in directions relative to their current position.

- "Turn left!"
- "Turn right!"
- "Turn backward!"

For example:

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

They also recognize commands:

- "Stand still!" - each command is ignored
- "Move your asses!" - soldiers stop ignoring commands and return to their pre-freeze state

You can of course choose the row or column for these commands.

The task was created on the basis of:
https://www.codewars.com/kata/57e23d378a8b8de758000b41