-- create table courses(
-- course_id int primary key,
-- course_name varchar(10),
-- student_id int
-- )
-- insert into courses(course_id,course_name,student_id)values
-- (100,'cs',1010),(101,'ec',1011),(102,'ce',1013),(103,'ai',1012)
-- select * from courses

SELECT students.name, courses.course_name  
FROM students  
INNER JOIN courses ON students.id = courses.student_id;
-- insert into courses(course_id,course_name,student_id)values(104,'me',1015)

