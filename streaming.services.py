def test_where_watch_movie():
    movie_1 = Movie('The Sevent Seal', 'comedy', 'Ingmar Bergman', 1957)
    movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
    movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)


    service_1 = StreamingService('Netflix')
    service_2 = StreamingService('HBO')

    service_1.add_movie(movie_1)
    service_2.add_movie(movie_2)
    service_2.add_movie(movie_3)

    guide = StreamingGuide()
    guide.add_streaming_service(service_1)
    guide.add_streaming_service(service_2)

    result_1 = guide.where_to_watch("The Sevent Seal")
    assert result_1 == ["The Sevent Seal (1957)", "Netflix"], f"Error: {result_1}"

    result_2 = guide.where_to_watch("Home Alone")
    assert result_2 == ["Home Alone (1990)", "HBO"], f"Error: {result_2}"

    result_3 = guide.where_to_watch("Little Women")
    assert result_3 == ["Little Women (2019)", "HBO"], f"Error: {result_3}"

    print("All tests passed for where_to_watch")


test_where_watch_movie()