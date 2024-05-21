# Movie-Management-Web-App

This project involves designing, creating, and managing a comprehensive movie database using SQL and Python. The primary objectives are to establish a relational database, populate it with sample data, and optimize query performance through indexing.

 Project Outline

 1. ER Model Design
   -Tables and Relationships**:
   -Movies: Details about movies (e.g., Title, ReleaseYear, GenreID, DirectorID, Rating, Description).
   - Genres: Genres of movies (e.g., GenreID, GenreName).
   -Directors: Information about directors (e.g., DirectorID, DirectorName, BirthDate).
   -Actors: Information about actors (e.g., ActorID, ActorName, BirthDate).
   -MovieActors: Associative table for the many-to-many relationship between movies and actors.

 2. Database Creation
    SQL Scripts: Create tables with appropriate primary and foreign keys.

 3. Data Population
   Sample Data: Insert at least 5 movies along with their genres, directors, and actors.

 4. SQL Queries
   Retrieve Movie Titles and Release Years.
   List Movies Released After 2010.
   Top-Rated Movies with Directors.
   Directors with At Least Three Movies.
   Average Rating for Each Genre.

5. Indexing for Performance
   Equality Query Index**: `CREATE INDEX idx_Title ON movies (Title)`.
   Range Query Index**: `CREATE INDEX idx_Rating ON movies (Rating)`.

6. Data Generation and Performance Testing
   Random Data Generation: Python functions to generate random genres, directors, actors, and millions of movies.
   Performance Measurement: Search queries by year and year range, both before and after indexing, to demonstrate the performance improvements.

 Deliverables
   PDF Report: Detailed documentation with screenshots and SQL scripts.
   Source Code: All SQL scripts and Python code in a ZIP file.
   Video Demonstration: A 5-minute video showcasing database size, search functionality, and execution times before and after indexing.

This project showcases the full cycle of database design, data manipulation, and performance optimization in a relational database system.
