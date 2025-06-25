# Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для
# некоторой организации. БД
# должна содержать таблицу Работник со следующей структурой
# записи:
# фамилия, имя,
# отчество, возраст, пол, профессия, стаж работы.

import sqlite3 as sq

workers = [
    (1, 'Новиков', 'Дмитрий', 'Александрович', 40, 2, 'Дизайнер', 15),
    (2, 'Федорова', 'Ольга', 'Николаевна', 27, 1, 'Маркетолог', 7),
    (3, 'Васильев', 'Сергей', 'Игоревич', 50, 2, 'Программист', 25),
    (4, 'Морозова', 'Анна', 'Сергеевна', 32, 1, 'Инженер', 6),
    (5, 'Волков', 'Павел', 'Анатольевич', 29, 2, 'Менеджер', 4),
    (6, 'Смирнова', 'Наталья', 'Васильевна', 38, 1, 'Дизайнер', 12),
    (7, 'Иванов', 'Иван', 'Иванович', 30, 2, 'Инженер', 5),
    (8, 'Кузнецова', 'Елена', 'Владимировна', 35, 1, 'Аналитик', 10),
    (9, 'Петрова', 'Мария', 'Сергеевна', 28, 1, 'Программист', 3),
    (10, 'Сидоров', 'Алексей', 'Петрович', 45, 2, 'Сварщик', 6),
]

with sq.connect('employment.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS worker")
    cur.execute("""CREATE TABLE IF NOT EXISTS worker (
    worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    otchestvo TEXT NOT NULL,
    old INTEGER NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    profession TEXT NOT NULL,
    work_exp INTEGER DEFAULT 0
    )""")

cur.executemany('INSERT INTO worker VALUES (?, ?, ?, ?, ?, ?, ?, ?)', workers)

cur.execute("SELECT * FROM worker WHERE surname = 'Иванов'")
cur.execute("SELECT * FROM worker WHERE profession = 'Программист'")
cur.execute("SELECT * FROM worker WHERE old > 30")

cur.execute("DELETE FROM worker WHERE surname = 'Кузнецова'")
cur.execute("DELETE FROM worker WHERE profession = 'Инженер'")
cur.execute("DELETE FROM worker WHERE old < 30")

cur.execute("UPDATE worker SET profession = 'Старший инженер' WHERE surname = 'Иванов'")
cur.execute("UPDATE worker SET old = 45 WHERE name = 'Иванов'")
cur.execute("UPDATE worker SET work_exp = 8 WHERE profession = 'Дизайнер'")

cur.execute("SELECT * FROM worker")

rows = cur.fetchall()

for row in rows:
    print('\t'.join(map(str, row)))

