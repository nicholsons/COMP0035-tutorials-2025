-- paralympics schema
/*
erDiagram
    Games {
        int id PK "NOT NULL, UNIQUE"
        int type "CHECK (type IN ('winter', 'summer'))"
        int year "CHECK (year BETWEEN 1960 AND 9999)"
        date start
        date end
        int countries
        int events
        int sports
        int participants_m
        int participants_f
        int participants
        string highlights
        string URL
    }
    Country {
        int id PK
        string country
    }
    Disability {
        int id PK
        string description
    }
    Team {
        string code PK
        string name
        string region "CHECK (region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania'))"
        string sub_region
        string member_type "CHECK (member_type IN ('country', 'team', 'dissolved', 'construct'))"
        string notes
        int country_id FK "ON UPDATE CASCADE ON DELETE SET NULL"
    }
    Host {
        int id PK
        string place_name
        int country_id FK "ON UPDATE CASCADE ON DELETE SET NULL"
    }
    GamesTeam {
        int id PK
        int games_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
        str team_code FK "ON UPDATE CASCADE ON DELETE CASCADE"
    }
    GamesDisability {
        int id PK
        int games_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
        int disability_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
    }
    GamesHost {
        int id PK
        int games_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
        int host_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
    }
*/
PRAGMA foreign_keys = ON;
CREATE TABLE games
(
    id INTEGER PRIMARY KEY,
    type TEXT, CHECK (type IN ('winter', 'summer')),
    year INTEGER, CHECK (year BETWEEN 1960 AND 9999),
    start TEXT,
    end TEXT, CHECK (end > start),
    countries INTEGER,
    events INTEGER,
    sports INTEGER,
    participants_m INTEGER,
    participants_f INTEGER,
    participants INTEGER,
    highlights TEXT,
    URL TEXT
);
CREATE TABLE country
(
    id INTEGER PRIMARY KEY,
    country TEXT NOT NULL
);
/*
 Disability {
        int id PK
        string description
    }
 */
CREATE TABLE disability (
        id INTEGER PRIMARY KEY,
        description TEXT

);
-- Team completed to show the FK syntax
CREATE TABLE team
(
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT, CHECK (region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')),
    sub_region TEXT,
    member_type TEXT, CHECK (member_type IN ('country', 'team', 'dissolved', 'construct')),
    notes TEXT,
    country_id INTEGER, FOREIGN KEY (country_id) REFERENCES Country (id) ON UPDATE CASCADE ON DELETE SET NULL
);

/*  Host {
        int id PK
        string place_name
        int country_id FK "ON UPDATE CASCADE ON DELETE SET NULL"
    }

 */

CREATE TABLE host (
    id INTEGER PRIMARY KEY,
    place_name TEXT,
    country_id INTEGER, FOREIGN KEY (country_id) REFERENCES Country (id) ON UPDATE CASCADE ON DELETE SET NULL
);

/*
    GamesTeam {
        int id PK
        int games_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
        str team_code FK "ON UPDATE CASCADE ON DELETE CASCADE"
    }
*/
CREATE TABLE gamesteam (
    id INTEGER PRIMARY KEY,
    games_id INTEGER, FOREIGN KEY games_id REFERENCES games (id) ON UPDATE CASCADE ON DELETE CASCADE,
    team_code TEXT, FOREIGN KEY team_code REFERENCES team (code) ON UPDATE CASCADE ON DELETE CASCADE

);
/*
    GamesDisability {
        int id PK
        int games_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
        int disability_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
    }
*/
CREATE TABLE gamesdisability (
    id INTEGER PRIMARY KEY,
    games_id INTEGER, FOREIGN KEY games_id REFERENCES games (id) ON UPDATE CASCADE ON DELETE CASCADE,
    disability_id INTEGER, FOREIGN KEY disability_id REFERENCES host (id) ON UPDATE CASCADE ON DELETE CASCADE

);
/*
    GamesHost {
        int id PK
        int games_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
        int host_id FK "ON UPDATE CASCADE ON DELETE CASCADE"
    }
*/
CREATE TABLE gameshost (
    id INTEGER PRIMARY KEY,
    games_id INTEGER, FOREIGN KEY games_id REFERENCES games (id) ON UPDATE CASCADE ON DELETE CASCADE,
    host_id INTEGER, FOREIGN KEY host_id REFERENCES disability (id) ON UPDATE CASCADE ON DELETE CASCADE

);