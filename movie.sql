CREATE TABLE IF NOT EXISTS movie (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    releaseYear INT,
    genre VARCHAR(60),
    director VARCHAR(70),
    rating REAL,
    description VARCHAR(100)
);

select * from movie;

select count(*) from movie;

CREATE INDEX idx_release_year ON movie (releaseYear);

