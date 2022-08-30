CREATE TABLE groups(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name VARCHAR(30));

CREATE TABLE teachers(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name VARCHAR(30));

CREATE TABLE subjects(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name VARCHAR(30),
teacher_id INT,
FOREIGN KEY (teacher_id) REFERENCES teachers (id)
ON DELETE SET NULL
ON UPDATE CASCADE);

CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name VARCHAR(35),
group_id INT,
FOREIGN KEY (group_id) REFERENCES groups (id)
ON DELETE SET NULL
ON UPDATE CASCADE);

CREATE TABLE marks(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
student_id INT,
subject_id INT,
mark INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
FOREIGN KEY (student_id) REFERENCES students (id),
FOREIGN KEY (subject_id) REFERENCES subjects (id)
ON DELETE SET NULL
);