## 2. Class inheritance and composition

## Class inheritance

Inheritance is a feature in object-oriented programming that allows one class (called a child or subclass) to inherit
attributes and methods from another class (called a parent or superclass).

It aims to:

- Reuse code across related classes
- Organize code more logically
- Extend functionality without rewriting everything

Let's say we have a base class Athlete, and we want to create a more specific class Runner that inherits from it:

```python
# Base class
class Athlete:
    def __init__(self, first_name, last_name, team_code, disability_class):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class

    def introduce(self):
        print(f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}.")


# Subclass
class Runner(Athlete):
    def __init__(self, first_name, last_name, team_code, disability_class, distance):
        super().__init__(first_name, last_name, team_code, disability_class)
        self.distance = distance  # e.g., 100m, 400m

    def race_info(self):
        print(f"{self.first_name} is running the {self.distance} race.")


# Example usage
runner1 = Runner("Li", "Na", "CHN", "T12", "100m")
runner1.introduce()  # Inherited method
runner1.race_info()  # Subclass-specific method
```

The Athlete class is inherited by adding as an argument to the Runner class `class Runner(Athlete)`. A class can inherit
from more than one class e.g. `class Runner(Athlete, TeamMember)`.

To access the attributes of the parent class, the constructor uses `super().__init__()` to specify the attributes
inherited.

The Runner class now has access to the args and methods of the Athlete class and can also add its own specific
attribute (`distance`), and methods (`race_info()`).

## Class composition

Composition in Python is a design principle where a class is made up of one or more objects from other classes, rather
than inheriting from them.

Imagine that an Athlete can have a list of Medal objects. Type hints have been added to the constructor to make it clear
that medals is a List of Medal objects.

```python
from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Medal:
    type: str
    design: str
    date_designed: date


class Athlete:
    def __init__(self, first_name: str, last_name: str, team_code: str, disability_class: str, medals: List[Medal]):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class
        self.medals = medals  # Composition: Athlete has Medals
```

To create an athlete with medals:
```python
# Create medals
medal1 = Medal("gold", "Paris 2024 design", date(2023, 7, 1))
medal2 = Medal("silver", "Tokyo 2020 design", date(2019, 8, 25))

# Create an athlete with medals
athlete = Athlete(
    first_name="Wei",
    last_name="Wang",
    team_code="CHN",
    disability_class="T54",
    medals=[medal1, medal2]
)

print(athlete)
```

## Activity
1. Modify your Athlete code to add the list of medals as an attribute.

[Next activity](5-03-pydantic.md)