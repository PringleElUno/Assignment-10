# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 12/1/2024
# Define a class named Movie that has four data members: _title, _genre, _director, and _year
# Define a Streaming Service that has two data members: _name and _catalog.
# Define a class named StreamingGuide that has one data member, _streamingservices

class Movie:
    """
    Attributes:
        
    A class representing a Movie
    
    Attributes:
        _title(str): The title of the movie.
        _genre(str): The genre of the movie.
        _director(str): The director of the movie.
        _year (int): The year of the movie.
    """
   
    def __init__(self, _title, _genre, _director, _year):
        """
        Initializing a class named Movie with four data members that are its attributes.
    
         Parameters:
            _title(str): Title of the movie.
            _genre(str): Genre of the movie.
            _director(str): The director of the movie.
            _year(int): The year the movie was released.
           """

        self._title = _title
        self._genre = _genre
        self._director = _director
        self._year = _year

    def get_title(self):
        """
        Return the title of the movie.
        """
        return self._title

    def get_genre(self):
        """
        Return the genre of the movie.
        """
        return self._genre

    def get_director(self):
        """
        Return the director of the movie.
        """
        return self._director

    def get_year(self):
        """
        Return the year of the movie.
        """
        return self._year

class StreamingService:
    """
    A class representing the Streaming Service that has two data members.

    Attributes:
        _name(str): The name of the Movie.
        _catalog(dict): A dictionary of movies with titles as keys and Movie objects as corresponding values.
    """

    def __init__(self, _name):
        """
        Initializes the StreamingService with a empty dictionary and the name.

        Parameters:
            _name(str): The name of the Movie.
        """

        self._name = _name
        self._catalog = {}

    def get_name(self):
        """
        Return the name of the Movie.
        """
        return self._name

    def get_catalog(self):
        """
        Return the dictionary of movies with titles as keys and movie objects with corresponding values.
        """
        return self._catalog

    def add_movie(self, _movie):
        """
        Add the movie object as a parameter and add it to the catalog.

        Parameter:
            movie (str): Add the movie to the catalog.
        """
        self._catalog[_movie.get_title()] = _movie

    def delete_movie(self, _title):
        """
        Define the movie with a specified title from the catalog if it exists.

        Parameter:
            _title (str): The title of the movie that is deleted.
        """
        if _title in self._catalog:
            del self._catalog[_title]

class StreamingGuide:
    """
    Defining a StreamingGuide that has one attribute, _streaming_services which will be a list of Streaming objects

    Attributes:
        _streaming_services (): An empty list of streaming services
    """

    def __init__(self):
        """
        Initiliazing _streaming_services with an empty list
        """
        self._streaming_services = []

    def add_streaming_service(self, service):
        """
        Adds a StreamingService object to the streaming services list.

        Parameters:
            service(StreamingService): Streaming service object added to the list.
        """
        self._streaming_services.append(service)

    def delete_streaming_service(self, name):
        """
        Deletes a StreamingService object if it is on the list.

        Parameters:
            name(str): Name of the Streaming Service that needs to be deleted.
        """

        for service in self._streaming_services:
            if service.get_name() == name:
                self._streaming_services.remove(service)
                break

    def where_to_watch(self, title):
        """
        Defines a movie title and its parameters and returns a list.

        Parameters:
            title(str): The title of the movie to search for.

        Returns:
            list: A list returned with the name and year of the movie as well as the streaming service
            None: If the movie is not available on any StreamingService it will return to none
        """

        result = []
        services_found = False

        # Repeat with the for loop for each streaming service in the guide
        for service in self._streaming_services:
            catalog = service.get_catalog()
            # Check if the movie exists in the service catalog using an if statement
            if title in catalog:
                movie = catalog[title]
                # If it does not have the details add it to the movie
                if not result:
                    result = [f"{title} ({movie.get_year()})"]
                result.append(service.get_name())
                # Append the name of the streaming service to the result
                services_found = True
        # Return the result if the services are found if not return to None
        return result if services_found else None
