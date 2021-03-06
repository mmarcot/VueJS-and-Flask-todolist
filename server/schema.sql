DROP TABLE IF EXISTS todoitems;

CREATE TABLE todoitems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL,
    vote INTEGER DEFAULT 0
);