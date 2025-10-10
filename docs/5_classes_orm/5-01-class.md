# 1. Introduction to Python classes

A Python class is way of bundling data (attributes) and behaviour (methods) together. They are often described as
being a "blueprint" for creating objects. Objects specific instances of things with data values for the attributes.

Consider the Paralympics scenario. Each Paralympics such as Paris 2024, has multiple sports such as Boccia. Boccia
has multiple events such as "Men's individual BC1" or "Mixed Pairs BC4".

An event might have attributes such as name, sport, category, competing athletes. It may also have behaviour such as to
describe the event; or to register athletes for the event. This can be written as a Python class.

Men's 100m T54, an Athletics event for classification T54 (wheelchair racing) is an example of a specific instance, or
object, that can be created from the event class.

A Python class to represent an event can be written as follows:

```python
class ParalympicEvent:
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         describe() Prints a description of the event
         register_athlete() Adds an athlete to the list of athletes
     """

    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names

    def describe(self):
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)
```

To break this down:

- `class ParalympicEvent:` is the keyword `class` defines this as a Python class. Unlike functions, Class names start
  with capital letters and do not use underscores.
- docstring: classes include docstrings at the class level and then for each function within it. This example uses
  the [Google style of class docstring](https://google.github.io/styleguide/pyguide.html#384-classes).
- `def __init__(self, name, sport, classification, athletes)`: - `__init__` is a special method used to initialize new
  objects from a class, also referred to as the constructor. When you create a new object for the class this lets you
  set the value of its attributes. The parameter `self` is how the current object refers to itself. It lets you access
  and modify its attributes (variables).
- `self.name` is an example of an attribute for the class
- `def describe()` is a method of the class

This is only an introduction to the core features of a class.

## Creating objects from a class

To create an object to represent a specific event, you pass values using the rules of its constructor. In this case we
can create an instance of an event by providing the name, sport and classification:

```python
event = ParalympicEvent(
    name="Men's individual BC1",
    sport="Boccia",
    classification="BC1",
)
```

To use the methods of the class use the dot notation:

```python
event.describe()  # Should print the event description, "Athletes competing" will be empty
event.register_athlete("Sungjoon Jung")  # should register the athlete
event.describe()  # Should print the event again, "Athletes competing" should include Sungjoon Jung
```

## Activity: Create an instance of a class and use its methods

1. The ParalympicEvent class is in [starter_class.py](../../src/activities/starter/starter_class.py).
2. Use the class to create an instance for a given event and register an athlete.

## Activity: Create an Athlete class

1. An athlete is likely to have more detail than their name.
2. Add a class to create an Athlete. Include relevant attributes such as name, the team they represent and their
   disability class.
3. Add a method that prints the details of the class. Rather than the `describe()` method shown in the example above
   create a string representation of the class. To do this you can overwrite the default method by defining a method
   called `__str__(self)`. See [example here](https://www.codecademy.com/resources/docs/python/dunder-methods/str).
4. Create an instance of the class and print it.

[Next activity](5-02-inheritance-composition.md)