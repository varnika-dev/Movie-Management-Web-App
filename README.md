# Movie-Management-Web-App

SQL and Indexes (25 Points)  
  
Given the following database tables:  
  
•	Movies: MovieID, Title, ReleaseYear, GenreID, DirectorID, RaAng, DescripAon  
•	Genres: GenreID, GenreName  
•	Directors: DirectorID, DirectorName, BirthDate  
•	Actors: ActorID, ActorName, BirthDate  
  
1.	Design the ER model and show the relaAonships clearly between tables (e.g. one-many relaAonships and many-many relaAonships). You may need to add more tables (e.g. to cover the many-many rela<onships), so feel free to add tables and keys as needed.  
 
Answer:   
<img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/fdc3db24-e3d9-4a47-93d5-c10e4b75ce68">


 	 
 
  
 
 
 
2.	Create the database and then create the above tables using SQL.  
 
Answer:   <img width="505" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/b2333a1d-603a-4816-8dce-2ca8ad0f15f0">

 
create table movies(MovieID int,Title varchar(50),ReleaseYear int,GenreID int,DirectorID int, 
RaAng real,DescripAon varchar(50)); select * from movies; 
create table genres(GenresID int,GenreName varchar(50)); select * from genres; 
create table directors(DirectorID int,DirectorName varchar(50),BirthDate int); select * from directors; 
create table actors(ActorID int,ActorName varchar(50),BirthDate int); select * from actors; 
 
 
  
  
 
 
 
 
3.	Populate the tables with real movies data (e.g. your favorite movies) with at least 5 movies. You may do it manually using SQL or using any programming language to import the data (e.g. Python). 
 
Answer:

 
a.insert into movies(MovieID,Title,ReleaseYear,GenreID,DirectorID,RaAng,DescripAon) values(456,'Parasite',2019,1224,34589,8.5,'The script is based on a play Bong wrote in 2013.'), 
(457,'Burning',2018,1225,34590,7.5,'famous chef who disappeared a[er having drugs'), 
(458,'The Chaser',2008,1226,34591,7.8,'a police involved in a breathless race'), 
(459,'Old Boy',2023,1227,34592,8.3,'a man is abducted from the street'), 
(460,'The wailing',2016,1228,34593,7.4,'Villagers invesAgate a stranger'); 

  <img width="483" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/f90ac6fc-56ce-46e9-a937-890c5b58f5c4">
  
 
b.insert into genres(GenresID,GenreName) 
values(850,' psychological, horror ,thriller'), 
(851,'thriller'),(852,'acAon,thriller'), 
(853,'acAon,thriller'), 
(854,'horror'); 
 
 <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/6395ffe7-b1dc-424c-8b05-f995c24b52c8">

 
 
 
c.insert into directors(DirectorID,DirectorName,BirthDate) values(34589,'Bong Joon-ho', 1969), 
(34590,'Lee Chang-dong',1954), 
(34591,'Na Hong-jin',1974), 
(34592,'Park Chan-wook',1963), 
(34593,'Na Hong-jin',1974); 
 
  <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/781089ed-3850-45c1-9f6b-f6493be5b460">

 

 
d.insert into actors(ActorID,ActorName,BirthDate) 
values(123,'Lee Sun-kyun',1975), 
(124,'Uhm Hong-sik',1986), 
(125,'Kim Yoon-seok',1968), 
(126,'Choi Min-sik',1962), 
(127,'Kwak Byung-kyu',1973); 
 
 <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/1c98ad40-7c76-4376-bba8-315cb4a0671c">

 
  
 
 
 
 
 
 
 
 
  
4. Write SQL queries to answer the following:  
 
a. Retrieve all movie Atles and their release years.  
 
 
Answer: 
 
SELECT Atle, releaseyear 
FROM movies; 
 <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/5f161ced-e452-4fa0-a44e-d2215c89ee3a">

 
  
 
 
 
 
List the movies released a[er 2010, sorted by release year.  
 
 
Answer:  SELECT Atle, releaseyear FROM movies 
WHERE releaseyear > 2010 
ORDER BY releaseyear; 
 
 
 <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/fed27db2-e09d-4be8-9265-5ecf322e4062">

 
  
 
 
 
 
 
Retrieve the top-rated movies along with their director.  
 
 
Answer:  SELECT d.directorName, m.Atle 
          FROM movies m 
          JOIN directors d ON m.directorid = d.directorid           ORDER BY m.raAng DESC; 
 
 	 
  
 
 
 
 
 
 <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/09e7c083-22fd-4d8f-8693-c171c9be7c18">

 
 
 
 
 
 
Retrieve the directors who have directed at least three movies.  
 
Answer:   SELECT d.directorName 
FROM directors d 
JOIN movies m ON d.DirectorID = m.DirectorID 
GROUP BY d.directorName 
HAVING COUNT(m.Title) >= 3; 
 
 
  <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/396b73c4-0b8a-4502-834b-952cd18958f5">

 
 
 
 
 
 
 
 
 
 
 
 
 
Get the average raAng for each genre.  
  
 
Answer:   SELECT GenreName, AVG(RaAng) AS AvgRaAng 
          FROM genres,movies 
          GROUP BY GenreName; 
 
  
 
 
 
 <img width="468" alt="image" src="https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/67ca849f-40f9-4059-8533-7a973d302ba6">

 
 
 
 
 
 
 
 
 
 
 
5. Suggest two indexes to be added to the database to enhance performance. One index to enhance an equality query and one index to enhance a range query. Explain clearly why you chose those indexes and show the SQL statements to create them.  
  
Answer:  
 
a.	CREATE INDEX idx_Atle ON movies (Title); 
 
 
Reason: There are several situaAons where you might need to look for a movie straight by its Atle, including when people look up films. The database can find the record that matches the requested movie Atle rapidly. 
 
 
b.	CREATE INDEX idx_movie_raAng ON movies (RaAng); 
 
Reason: For example, to retrieve all movies with a raAng higher than a given number, range queries on the RaAng column can be helpful in locaAng movies inside a given raAng range. Improving the database engine's ability to rapidly discover rows with raAngs falling inside a given range helps speed up such queries by adding an index on RaAng. 
 
 
 
 
 
 
You are free to choose the DBMS that you are comfortable with (e.g. SQLite, PostgreSQL, any other relaAonal database).  
  
Submit a PDF report with clear screenshots and SQL scripts for every quesAon above.  
![image](https://github.com/varnika-dev/Movie-Management-Web-App/assets/146048180/8ac4092c-9f67-44e6-a4b3-af50c235f86e)
