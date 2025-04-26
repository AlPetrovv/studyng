ALTER TABLE "teacher" ADD COLUMN age DATE;

-- ALTER TABLE - change table structure (DROP, ADD, etc.)
-- ADD COLUMN - add column to table
-- syntax:
    -- ALTER TABLE <table_name> ADD COLUMN <column_name> <column_type>;

UPDATE "teacher" SET age = '10-08-1994' WHERE "teacher"."id" = 5;

