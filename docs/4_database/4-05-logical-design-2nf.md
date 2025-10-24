# 5. Logical database design to 2NF

## Second normal form (2NF)

Second normal form (2NF) is when a table that is already in 1NF and in which the values of each non-primary-key
attribute (column) can be worked out from the values in all the attributes (columns) that make up the primary key.

To determine 2NF you need to know the concept of a **functional dependency**.

A **functional dependency** indicates how attributes relate to one another. A functional dependency exists when one
attribute (or a set of attributes) uniquely determines another attribute. In other words, if you know the value of one
attribute, you can determine the value of another attribute. There is a formal notation for this which we will not use
in this course.

For tables with a single-column primary key, 2NF is automatically satisfied if the table is in 1NF. This is because
there can’t be partial dependencies when there’s only one column in the primary key.

The key aspects of 2NF are:

- 1NF is met
- No partial dependencies, where a non-key attribute is dependent on only a part of a composite primary key.
  Every non-key attribute must depend on the entire primary key, not just a part of it.

Consider a table storing information about courses and the instructors who teach them:

| CourseID | InstructorID | InstructorName | CourseName |
|:--------:|:------------:|:--------------:|:----------:|
|   101    |      	1      |     Smith      |    Math    |
|   102    |      	2      |    Johnson     |  Science   |
|   103    |      	1      |     Smith      |  Algebra   |

In this table, CourseID and InstructorID together form the composite primary key.

InstructorName depends only on InstructorID, not on the combination of CourseID and InstructorID.

To convert this table to 2NF, we need to remove the partial dependency by creating two separate tables:

Courses Table:

| CourseID | CourseName |
|:---------|:-----------|
| 101      | Math       |
| 102      | Science    |
| 103      | Algebra    |

Instructors Table:

| InstructorID | InstructorName |
|:-------------|:---------------|
| 1            | Smith          |
| 2            | Johnson        |

Now, each non-key attribute is fully dependent on the primary key of its respective table, satisfying 2NF.

## Is the paralympics ERD in 2NF?

The tables in the paralympics ERD already satisfy 2NF. We already replaced the 'type' and 'year' composite primary key
with a single primary key called 'id'.

You could map the functional dependencies and demonstrate 2NF, though it isn't needed in this case:

Games

- PK: id
- Functional dependencies: id → type, year, host_id, start, end, countries, events, sports, participants_m,
  participants_f, participants, highlights, URL
- Each game is uniquely identified by id, and all other attributes depend on it.

Team

- PK: code
- Functional dependencies: code → name, region, sub_region, member_type, notes, country_id
- Each team has a unique code, which determines its other attributes.

Host

- PK: code
- Functional dependencies: code → host
- Each host is uniquely identified by a code.

Disability

- PK: id
- Functional Dependencies: id → description
- Each disability has a unique ID and a description.

Country

- PK: id
- Functional Dependencies: id → country, team_code
- Each country has a unique ID, which determines its name and associated team code.

GamesTeam

- PK: id
- Functional Dependencies: id → games_id, team_id
- This is a junction table for the many-to-many relationship between Games and Team. The surrogate key id determines the
  foreign keys.
- Additionally: {games_id, team_id} → id (this composite key could also uniquely identify the row)

GamesDisability

- PK: id
- Functional Dependencies:
    - id → games_id, disability_id
    - {games_id, disability_id} → id

GamesHost

- PK: id
- Functional Dependencies:
    - id → games_id, host_id
    - {games_id, host_id} → id

[Next activity](4-06-logical-design-3nf.md)
