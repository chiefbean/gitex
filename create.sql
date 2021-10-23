CREATE TABLE repo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    path TEXT
);

CREATE TABLE commit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    user TEXT,
    date TEXT
);