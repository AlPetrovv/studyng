INSERT INTO "teacher"("name") VALUES ('Fedorov'), ('Kotelnikov'), ('Sidor');

-- INSERT INTO - create new row in database
-- syntax:
    -- INSERT INTO <table_name>(<column_name1>, <column_name2>, ...) VALUES (<value1>, <value2>, ...);
    -- !!!table_name and column name must be use double quotes and values use single quotes


INSERT INTO "lesson"("name", "teacher_id")
VALUES ('sport',1),
       ('history',2),
       ('geo',1),
       ('physic',3),
       ('math',4);