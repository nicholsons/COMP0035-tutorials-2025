PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS country (
    id INTEGER PRIMARY KEY,
    country TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS disability (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    type TEXT CHECK (type IN ('winter', 'summer')),
    year INTEGER CHECK (year BETWEEN 1960 AND 9999),
    start TEXT,
    end TEXT,
    countries INTEGER,
    events INTEGER,
    sports INTEGER,
    participants_m INTEGER,
    participants_f INTEGER,
    participants INTEGER,
    highlights TEXT,
    URL TEXT
);

CREATE TABLE IF NOT EXISTS team (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT CHECK (region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')),
    sub_region TEXT,
    member_type TEXT CHECK (member_type IN ('country', 'team', 'dissolved', 'construct')),
    notes TEXT,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES country(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS host (
    id INTEGER PRIMARY KEY,
    place_name TEXT NOT NULL,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES country(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS gamesteam (
    id INTEGER PRIMARY KEY,
    games_id INTEGER,
    team_code TEXT,
    FOREIGN KEY (games_id) REFERENCES games(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (team_code) REFERENCES team(code)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS gamesdisability (
    id INTEGER PRIMARY KEY,
    games_id INTEGER,
    disability_id INTEGER,
    FOREIGN KEY (games_id) REFERENCES games(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (disability_id) REFERENCES disability(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS gameshost (
    id INTEGER PRIMARY KEY,
    games_id INTEGER,
    host_id INTEGER,
    FOREIGN KEY (games_id) REFERENCES games(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (host_id) REFERENCES host(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);