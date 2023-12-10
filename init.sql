create table post (
    id integer primary key AUTOINCREMENT,
    title text,
    body text,
    created_at datatime DEFAULT CURRENT_TIMESTAMP
    );