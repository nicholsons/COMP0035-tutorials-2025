-- SQLite
-- 1. View all courses
SELECT * FROM course;

-- 2. List all students enrolled in a course
SELECT student.student_name, course.course_name
FROM enrollment
JOIN student ON enrollment.student_id = student.student_id
JOIN course ON enrollment.course_id = course.course_id;

-- 3. List students with their teacher’s name
SELECT student.student_name, course.course_name, teacher.teacher_name
FROM enrollment
JOIN student ON enrollment.student_id = student.student_id
JOIN course ON enrollment.course_id = course.course_id
JOIN teacher ON course.teacher_id = teacher.teacher_id;

-- 4. Count how many students are in each course
SELECT course.course_name, COUNT(*) AS student_count
FROM enrollment
JOIN course ON enrollment.course_id = course.course_id
GROUP BY course.course_name;