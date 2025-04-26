SELECT id FROM teacher;
-- SELECT - GET some data from table or tables
-- syntax:
    -- SELECT <can be some logic> <fields> FROM <table_name> <some logic>

SELECT * FROM teacher WHERE id=2;
-- * - get all data from table or tables
-- WHERE - filter by condition

SELECT id AS "Identificator", name AS "First name" FROM "teacher";

-- SELECT <column> AS - use when we need to change name of column until getting the data

SELECT * FROM teacher ORDER BY id DESC;

-- ORDER BY - ordering by column or func (count, aggregate, etc.)
-- DESC - descending 1,2,3 -> 3,2,1


SELECT * FROM "teacher" WHERE "teacher"."name" LIKE '%';
-- SELECT all data from teacher WHERE teacher.name has any symbol
-- LIKE - search by pattern(like re in python)
-- symbol "%" - any symbols ("%en" - trust for "eiten", "en", etc.)

SELECT * FROM "teacher" WHERE id > 3 AND age IS NULL;

SELECT * FROM "teacher" WHERE id BETWEEN 2 AND 5;
-- BETWEEN - filter by range


SELECT "teacher"."name", "lesson"."name" FROM teacher INNER JOIN lesson ON teacher.id = lesson.teacher_id;
-- JOIN - add data from another table to result
-- INNER JOIN - data only from joined objects in tables, that has connection
-- syntax:
    -- SELECT <fields> FROM <table1> INNER JOIN <table2> ON <table1>.<column_name> = <table2>.<column_name>

SELECT "teacher"."name", "lesson"."name" FROM teacher LEFT JOIN lesson ON teacher.id = lesson.teacher_id;

SELECT "teacher"."name", "teacher"."id" FROM teacher UNION SELECT "lesson"."name", "lesson"."id" FROM "lesson";
-- UNION - concat data from tables to one table with columns from tables
-- UNION JUST concat data from tables to specific columns
-- ALL data in one table
-- syntax:
    -- SELECT <fields> FROM <table1> UNION SELECT <fields> FROM <table2>  SELECT etc...


SELECT AVG("teacher"."id") AS "average_id" FROM "teacher";
-- AGGREGATE function (AVG, SUM, MIN, MAX)
-- need to calculate something by column
SELECT MAX("teacher"."id") AS "max_id" FROM "teacher";


SElECT "teacher"."name", COUNT("teacher"."name")  AS "teacher_name_count" FROM "teacher" GROUP BY "teacher"."name";
-- COUNT use with GROUP BY required,
-- syntax:
 -- SELECT <fields>? COUNT <fields> FROM <table> GROUP BY <fields>