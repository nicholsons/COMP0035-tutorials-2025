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
    FOREIGN KEY (country_id) REFERENCES country(id) ON UPDATE CASCADE ON DELETE SET NULL
);

-- Sample Data Insertion
INSERT INTO country (id, country) VALUES (1, 'France'), (2, 'Japan');

INSERT INTO disability (id, description) VALUES 
    (1, 'Visual Impairment'),
    (2, 'Wheelchair User');

INSERT INTO games (id, type, year, start, end, countries, events, sports, participants_m, participants_f, participants, highlights, URL)
VALUES
    (1, 'summer', 2020, '2020-08-24', '2020-09-05', 100, 540, 22, 2100, 1900, 4000, 'First games postponed due to COVID', 'https://example.com');

INSERT INTO team (code, name, region, sub_region, member_type, notes, country_id) VALUES
    ('FRA', 'France Team', 'Europe', 'Western Europe', 'country', 'Strong athletics', 1),
    ('JPN', 'Japan Team', 'Asia', 'East Asia', 'country', NULL, 2);