CREATE TABLE Team (
    code VARCHAR(3) PRIMARY KEY CHECK (code ~ '^[A-Z]{3}$'),
    name VARCHAR(100) NOT NULL,
    region VARCHAR(20) CHECK (region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')),
    sub_region VARCHAR(30) CHECK (
        sub_region IN (
            'South', 'South-East', 'North', 'South, West', 'North, West', 'Central',
            'Caribbean', 'Central', 'South-East', 'Oceania', 'West', 'Central, East'
        ) OR sub_region IS NULL
    ),
    member_type VARCHAR(20) CHECK (member_type IN ('country', 'team', 'dissolved', 'contract')),
    notes TEXT,
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES Country(id)
);