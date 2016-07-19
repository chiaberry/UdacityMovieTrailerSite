# Udacity Movie Trailer Site
Movie Trailer Website project for Udacity Nanodegree program

The project was to create a website that played the trailers of some of my favorite movies. 

Repository includes


1. `fresh_tomatoes.py`: Module provided by Udacity to generate website, [link here] (https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py). I edited it to also show a film's brief summary upon mouseover of the poster art. 


2. `movies.py`: Python file that creates a class to store my favorite movies, their posters, a brief summary and link to their trailer on youtube. 


3. `trailer_page.py`: Python file that imports movies.py and fresh_tomatoes.py. Creates multiple instances of the Movie class and stores them in a list. Calls `open_movies_page()` from fresh_tomatoes to generate website. 


4. `fresh_tomatoes.html`: website generated by calling trailer_page.py


Running `trailer_page.py` will generate and load the website in a new tab in your default browser. 
