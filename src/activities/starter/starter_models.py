# Model classes defined using SQLModel. Starter code for activity 5.5.
from __future__ import annotations

from typing import List, Optional

from sqlalchemy import CheckConstraint
from sqlmodel import Field, Relationship, SQLModel


class Games(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    year: int
    start: str | None
    end: str | None
    countries: int | None
    events: int | None
    sports: int | None
    participants_m: int | None
    participants_f: int | None
    participants: int | None
    highlights: str | None
    URL: str | None

    games_teams: List["GamesTeam"] = Relationship(back_populates="games", cascade_delete=True)
    games_disabilities: List["GamesDisability"] = Relationship(back_populates="games", cascade_delete=True)
    games_hosts: List["GamesHost"] = Relationship(back_populates="games", cascade_delete=True)

    __table_args__ = (
        CheckConstraint("type IN ('winter', 'summer')"),
        CheckConstraint("year BETWEEN 1960 AND 9999")
    )


class Country(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    country: str

    teams: List["Team"] = Relationship(back_populates="country")
    hosts: List["Host"] = Relationship(back_populates="country")


class Disability(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str

    games_disabilities: List["GamesDisability"] = Relationship(back_populates="disability")


class Team(SQLModel, table=True):
    code: str = Field(primary_key=True)
    name: str
    region: Optional[str]
    sub_region: Optional[str]
    member_type: Optional[str]
    notes: Optional[str]
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")

    country: Optional[Country] = Relationship(back_populates="teams")
    games_teams: List["GamesTeam"] = Relationship(back_populates="team")

    __table_args__ = (
        CheckConstraint("member_type IN ('country', 'team', 'dissolved', 'construct')"),
        CheckConstraint("region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')")
    )


class Host(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    place_name: str
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")

    country: Optional[Country] = Relationship(back_populates="hosts")
    games_hosts: List["GamesHost"] = Relationship(back_populates="host")


class GamesTeam(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    games_id: int = Field(foreign_key="games.id")
    team_id: str = Field(foreign_key="team.code")

    games: Optional[Games] = Relationship(back_populates="games_teams")
    team: Optional[Team] = Relationship(back_populates="games_teams")


class GamesDisability(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    games_id: int = Field(foreign_key="games.id")
    disability_id: int = Field(foreign_key="disability.id")

    games: Optional[Games] = Relationship(back_populates="games_disabilities")
    disability: Optional[Disability] = Relationship(back_populates="games_disabilities")


class GamesHost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    games_id: int = Field(foreign_key="games.id")
    host_id: int = Field(foreign_key="host.id")

    games: Optional[Games] = Relationship(back_populates="games_hosts")
    host: Optional[Host] = Relationship(back_populates="games_hosts")
