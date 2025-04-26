CREATE TABLE teacher ( -- create table command
  id SERIAL PRIMARY KEY, -- add id column: serial==autoincrement, PRIMARY KEY - unique and not null
  name VARCHAR(255) NOT NULL -- add name column: VARCHAR - usr char symbols for this column, 255 - max length, NOT NULL - not null
);

-- HOW TO ADD COLUMN WHILE CREATING TABLE
    -- <column_name> <column type> <column conditions>

-- PRIMARY KEY - unique and not null (standard conditions)


-- CREATE TABLE WITH FOREIGN KEY
CREATE TABLE lesson(
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
teacher_id INT NOT NULL, -- add teacher_id column: for FOREIGN KEY we need to add column that connect to another table
FOREIGN KEY(teacher_id) REFERENCES teacher(id) -- add FOREIGN KEY: set FOREIGN KEY for teacher_id == teacher.id
);

--- HOW TO ADD FOREIGN KEY WHILE CREATING TABLE
    -- FOREIGN KEY(<column_name>) REFERENCES <another_table>(<column_name>)



