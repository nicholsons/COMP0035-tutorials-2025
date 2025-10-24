# 6. Logical database design to 3NF

## Third normal form (3NF)

Third normal form (3NF) is a table that is already in 1NF and 2NF, and in which the values in all non-primary-key
columns can be worked out from only the primary key column(s) and no other columns.

The key aspects of 3NF are:

- It is in Second Normal Form (2NF)
- No Transitive Dependencies: All non-prime attributes (attributes that are not part of any candidate key) must be
  directly dependent on the primary key. There should be no transitive dependency, where a non-prime attribute depends
  on another non-prime attribute.

Consider this table:

| StudentID (PK)	 | CourseID (PK)	 | InstructorID	 | InstructorName |
|:----------------|:---------------|:--------------|:---------------|
| 1	              | 101	           | 1	            | Smith          |
| 2	              | 102	           | 2	            | Johnson        |
| 3	              | 103	           | 1	            | Smith          |

StudentID and CourseID together form the composite primary key.

InstructorName is dependent on InstructorID, not directly on the composite key.

To convert this table to 3NF, we need to remove the transitive dependency by creating separate tables:

StudentsCourses Table:

| StudentID (PK)	 | CourseID (PK)	 | InstructorID	 |
|:----------------|:---------------|:--------------|
| 1	              | 101	           | 1	            | 
| 2	              | 102	           | 2	            | 
| 3	              | 103	           | 1	            |

Instructors Table:

| InstructorID	(PK) | InstructorName |
|:------------------|:---------------|
| 1	                | Smith          |
| 2	                | Johnson        |
| 1	                | Smith          |

Each non-primary attribute is directly dependent on the primary key of its respective table and so satisfies 3NF.

## Is the paralympics ERD in 3NF?

- Games: All attributes (e.g., type, year, host_id, etc.) depend directly on id. No transitive dependencies (e.g.,
  host_id
  is a foreign key, but host details are stored in the Host table).
- Team: Attributes like name, region, sub_region, etc. depend directly on code. country_id is a foreign key, not a
  derived attribute.
- Host: host depends directly on code.
- Disability: description depends directly on id.
- Country: country, team_code depend directly on id. team_code is a foreign key, not a derived attribute.
- GamesTeam, GamesDisability, GamesHost: These are association tables with surrogate keys (id) and foreign keys. No
  non-key attributes, so no transitive dependencies.

The design meets 3NF. All non-key attributes depend only on the primary key, and there are no transitive dependencies.

You could add further tables to the design if you wished; for example create tables for the region, sub_region and 
member_type values that are used in the Team table.

[Next activity](4-07-logical-design-constraints-data.md)
