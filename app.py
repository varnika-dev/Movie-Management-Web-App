from flask import Flask, render_template, request, jsonify
import psycopg2
import random
import time
app = Flask(__name__)

# Database configuration
DATABASE = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': '2624',
    'port': '5433'  # Change to the appropriate port if necessary
}

# Function to generate a random genre from a list of real genres
@app.route('/add_genre', methods=['GET']) 
def generate_genre():
    genres = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Western']
    return random.choice(genres)

# Function to generate a random director name
@app.route('/add_director', methods=['GET'])
def generate_director():
    director_names = [
        "Christopher Nolan", "Quentin Tarantino", "Martin Scorsese",
        "Steven Spielberg", "Alfred Hitchcock", "Stanley Kubrick",
        "James Cameron", "Francis Ford Coppola", "Clint Eastwood",
        "David Fincher", "Ridley Scott", "Tim Burton", "Spike Lee",
        "Woody Allen", "Peter Jackson", "Akira Kurosawa", "Wes Anderson",
        "Coen Brothers"
    ]
    return random.choice(director_names)

# Function to generate a random actor name
@app.route('/add_actor', methods=['GET'])
def generate_actor():
    first_names = ["John", "Emma", "Michael", "Sophia", "William",
        "Olivia", "James", "Ava", "Alexander", "Isabella",
        "Robert", "Mia", "Daniel", "Emily", "Matthew",
        "Charlotte", "David", "Amelia", "Joseph", "Harper"
    ]
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones",
        "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson"
    ]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

@app.route('/Add_multiple_movies', methods=['GET'])
def Add_multiple_movies():
    return render_template('Add_multiple_movies.html')

# Function to add multiple movies
@app.route('/add_multiple_movies', methods=['POST'])
def add_multiple_movies():
    try:
        conn = psycopg2.connect(**DATABASE)
        cursor = conn.cursor()
        num_movies = int(request.form['num_movies'])

        for _ in range(num_movies):
            # Generate random movie details
            title = f"Random Movie {random.randint(1, 1000)}"
            release_year = random.randint(1900, 2022)
            genre = generate_genre()
            director = generate_director()
            rating = round(random.uniform(1, 10), 1)
            description = "A randomly generated movie."

            # Insert the movie into the database
            cursor.execute("INSERT INTO movie(title, releaseYear, genre, director, rating, description) VALUES (%s, %s, %s, %s, %s, %s)",
                           (title, release_year, genre, director, rating, description))
        
        conn.commit()
        conn.close()

        return jsonify({'message' : f'{num_movies} added successfully'})
    except Exception as e:
        print(e)
        return jsonify({'error':'error'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_multiple_movies', methods=['GET', 'POST'])
def add_multiple_movies_route():
    if request.method == 'POST':
        try:
            num_movies = int(request.form['num_movies'])
            success = add_multiple_movies(num_movies)
            if success:
                return jsonify({'message': f'Successfully added {num_movies} movies.'})
            else:
                return jsonify({'error': 'Failed to add movies.'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return render_template('add_multiple_movies.html')
    
#Function to execute a query and measure time
def execute_query_with_time(query):
    start_time = time.time()
    conn = psycopg2.connect(**DATABASE)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    end_time = time.time()
    execution_time = round(end_time - start_time, 3)
    return result, execution_time

# Function to add an index to the releaseYear column
@app.route('/add_index', methods=['GET'])
def add_index():
    try:
        conn = psycopg2.connect(**DATABASE)
        cursor = conn.cursor()
        cursor.execute("CREATE INDEX idx_release_year ON movie (releaseYear)")
        cursor.execute("CREATE INDEX idx_year_range ON movie (startYear, endYear)")
        conn.commit()
        conn.close()
        return jsonify({'message': 'Indexes added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to search movies by year
@app.route('/search_movies_by_year', methods=['GET'])
def search_movies_by_year():
    year = request.args.get('year')
    query = f"SELECT COUNT(*) FROM movie WHERE releaseYear = {year}"
    result_before_index, time_before_index = execute_query_with_time(query)

    query_with_index = f"SELECT COUNT(*) FROM movie WHERE releaseYear = {year}"
    result_after_index, time_after_index = execute_query_with_time(query_with_index)

    return jsonify({
        'num_movies_found_before_index': result_before_index[0][0],
        'execution_time_before_index': time_before_index,
        'num_movies_found_after_index': result_after_index[0][0],
        'execution_time_after_index': time_after_index
    })

# Function to search movies by year range
@app.route('/search_movies_by_year_range', methods=['GET'])
def search_movies_by_year_range():
    start_year = request.args.get('startYear')
    end_year = request.args.get('endYear')
    query = f"SELECT COUNT(*) FROM movie WHERE startYear = {start_year} AND endYear = {end_year}"
    result_before_index, time_before_index = execute_query_with_time(query)

    query_with_index = f"SELECT COUNT(*) FROM movie WHERE startYear = {start_year} AND endYear = {end_year}"
    result_after_index, time_after_index = execute_query_with_time(query_with_index)

    return jsonify({
        'num_movies_found_before_index': result_before_index[0][0],
        'execution_time_before_index': time_before_index,
        'num_movies_found_after_index': result_after_index[0][0],
        'execution_time_after_index': time_after_index
    })

if __name__ == '__main__':
    app.run(debug=True)
