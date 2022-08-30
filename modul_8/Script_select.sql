/*5 студентов с наибольшим средним баллом по всем предметам.*/
SELECT AVG(mark) as avg_mark, name
FROM  marks
LEFT JOIN students ON students.id = marks.student_id
GROUP BY name
ORDER BY  avg_mark DESC
LIMIT 5;

SELECT name, AVG(mark) as avg_mark
FROM students, marks
where students.id = marks.student_id 
GROUP BY name
ORDER BY  avg_mark DESC
LIMIT 5;

/*1 студент с наивысшим средним баллом по одному предмету.*/
SELECT students.name, AVG(mark) as avg_mark, subjects.name
FROM marks, students,subjects
where marks.subject_id = subjects.id and students.id = marks.student_id and subjects.name = "Python"
GROUP BY students.name
ORDER BY avg_mark DESC
LIMIT 1;

/*средний балл в группе по одному предмету.*/
SELECT groups.name as N_group, ROUND(AVG(mark), 2) as avg_mark, subjects.name as subject
FROM marks, groups, students, subjects
WHERE marks.subject_id = subjects.id and students.group_id = groups.id and subjects.name = "Python" 
and groups.name = 535 and students.id = marks.student_id;

/*Средний балл в потоке.*/
SELECT round(AVG(mark),2)
FROM marks;

/*Какие курсы читает преподаватель*/
SELECT teachers.name, subjects.name 
FROM teachers, subjects
WHERE teachers.id = subjects.teacher_id and teachers.name = 'Matthew Robbins';

/*Список студентов в группе.*/
SELECT students.name
FROM groups, students
WHERE students.group_id = groups.id and groups.name = '312'
ORDER BY students.name;

/*Оценки студентов в группе по предмету.*/
SELECT students.name, marks.mark 
FROM groups, students, subjects, marks
WHERE students.group_id = groups.id and groups.name = '312' and subjects.name = 'Go' and marks.student_id = students.id 
ORDER BY students.name;

/*Оценки студентов в группе по предмету на последнем занятии*/
SELECT students.name, marks.mark 
FROM groups, students, subjects, marks
WHERE students.group_id = groups.id and groups.name = '312' and subjects.name = 'Go' and marks.student_id = students.id 
and created_at = (SELECT max(created_at) FROM marks)
GROUP BY students.name;

/*Список курсов, которые посещает студент.*/
SELECT subjects.name
FROM subjects, students, marks
WHERE students.id = marks.student_id and subjects.id = marks.subject_id  and students.name = 'Andrea Martin'
GROUP BY subjects.name;

/*Список курсов, которые студенту читает преподаватель.*/
SELECT subjects.name
FROM subjects, students, marks, teachers
WHERE students.id = marks.student_id and subjects.id = marks.subject_id  and students.name = 'Andrea Martin' 
and teachers.name = 'Michelle Martin' and subjects.teacher_id = teachers.id 
GROUP BY subjects.name;

/*Средний балл, который преподаватель ставит студенту.*/
SELECT AVG(marks.mark)
FROM groups, students, subjects, marks, teachers 
WHERE students.id = marks.student_id and subjects.id = marks.subject_id  and students.name = 'Andrea Martin' 
and teachers.name = 'Michelle Martin' and subjects.teacher_id = teachers.id;

/*Средний балл, который ставит преподаватель.*/
SELECT teachers.name as Techers_name, ROUND(AVG(marks.mark), 2) as avg_mark
FROM groups, students, subjects, marks, teachers 
WHERE subjects.id = marks.subject_id  and subjects.teacher_id = teachers.id
GROUP BY teachers.name;


