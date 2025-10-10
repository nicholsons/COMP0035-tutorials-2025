# 3. Pydantic classes

[Pydantic](https://docs.pydantic.dev/latest/) is a Python library used for data validation and settings management using
Python type annotations. It's widely used in modern Python projects, particularly with frameworks like FastAPI.

You will be using pydantic and FastAPI in COMP0034.

Pydantic:

- Validates data: Ensures that the data you receive from users, APIs, files, etc. matches the types and constraints
  you specify.
- Parses data: Converts input data into Python objects with the correct types.
- Automatic error messages: If the data is invalid, Pydantic gives clear error messages.

To use Pydantic you inherit it's BaseModel class in your class definitions. This inheritance gives your class all the
attributes and [methods](https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties) of the pydantic
BaseModel class.

Pydantic documentation, and other tutorials, refer to classes defined using pydantic as 'models'. A pydantic model is a
Python class which inherits from BaseModel and defines fields as annotated attributes.

Note that pydantic syntax varies for different versions of pydantic and different versions of Python. Use
the latest [pydantic documentation](https://docs.pydantic.dev/latest/) rather than other sources of information.

Here this the Athlete model again, this time inheriting the pydantic BaseModel and with annotated attributes:

```python
from pydantic import BaseModel


class Athlete(BaseModel):
    first_name: str
    last_name: str
    team_code: str
    disability_class: str
    medals: list[Medal]
```

Pydantic classes can contain methods:

```python
from pydantic import BaseModel


class Athlete(BaseModel):
    first_name: str
    last_name: str
    team_code: str
    disability_class: str
    medals: list[Medal]

    def introduce(self) -> str:
        return f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}."
```

The function signature `def introduce(self) -> str:` uses Python's type hinting to specify that the function
returns a string. This style is not mandatory, but it is more expressive as it clearly indicates the expected return
type.

You can see a version of the classes re-defined with pydantic
in [starter_pydantic.py](../../src/activities/starter/starter_pydantic.py)

## Pydantic validation

The fields for the Athlete class should be validated as per the following comments

```
class Athlete(BaseModel):
    first_name: str  # Must be provided
    last_name: str  # Must be provided
    team_code: str  # Can be None
    disability_class: str  # Can be None
    medals: list[Medal]  # Set to empty as default
```

These can be added as follows:

```python
class Athlete(BaseModel):
    first_name: str
    last_name: str
    team_code: str | None
    disability_class: str | None
    medals: list[Medal] = []
```

## Activity: Add validation to the Athlete

1. Make a copy of [starter_pydantic.py](../../src/activities/starter/starter_pydantic.py)
2. Add validation to the Athlete and optionally to Medal
3. Create an instance with valid data e.g. create an `athlete` with no medals, create a new medal, add the new medal to
   the athlete's medals list e.g. athlete.medals = new_medal

   Examples of real para athletes from Paris 2024:
    - Yuyan Jiang from team CHN People's Republic of China won 7 gold medals
    - Catherine Debrunner from ITA Italy won 5 gold and 1 bronze
    - Bianka Pap from HUN Hungary won 1 gold, 1 silver and 1 bronze
4. Create an instance with invalid data. If you want to catch the errors gracefully use try/except with ValidationError:

    ```python
   from pydantic import ValidationError
   
     try:
        bp = Athlete(first_name="Bianka", medals=1)
    except ValidationError as e:
        print(e.errors())
    ```
   
[Next activity](5-04-orm-sqlmodel.md)