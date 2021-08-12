DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS research;

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE research(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    researcher_id  INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    info_gathered TEXT NOT NULL,
    FOREIGN KEY (researcher_id) REFERENCES user (id)
);