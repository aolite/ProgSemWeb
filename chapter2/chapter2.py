from myTripleStore import SimpleGraph

if __name__=="__main__":

    print "Chapter 2 examples"

    print "Creating a simple Graph..."
    movie_graph = SimpleGraph()

    print "Adding blade runner triples..."
    movie_graph.add(('blade_runner', 'name', 'Blade Runner'))
    movie_graph.add(('blade_runner', 'directed_by', 'ridley_scott'))
    movie_graph.add(('ridley_scott', 'name', 'Ridley Scott'))

    print "Who is the diretor of 'blade_runner' "
    print list(movie_graph.triples(('blade_runner', 'directed_by', None)))

    print "Who are the triples with 'name' property?"
    print list(movie_graph.triples((None,'name',None)))

    print "who is the director of 'blade_runner?'"
    print movie_graph.value('blade_runner', 'directed_by', None)

    print "Load movies CSV..."

    movies = SimpleGraph()

    movies.load("../resources/movies.csv")

    print "Movies loaded"

    print "Who is the blade runner id?"
    bladerunnerId = movies.value(None, "name", "Blade Runner")

    print "Blade runner Id: "+ bladerunnerId

    bladerunnerActorIds = [actorId for _, _, actorId in movies.triples((bladerunnerId, "starring", None))]

    print "Who are the blade runner actors Id?"

    print "Actors ID: "+ str (bladerunnerActorIds)

    print str([movies.value(actorId, "name", None) for actorId in bladerunnerActorIds])


    print "In which movies Harrison Ford has participated?"

    harrisonfordId = movies.value(None, "name", "Harrison Ford")

    print ([movies.value(movieId, "name", None) for movieId, _, _ in movies.triples((None, "starring", harrisonfordId))])


    print "In which films Harrison Ford has acted with Steven Spilbers as director?"

    spielbergId = movies.value(None, "name", "Steven Spielberg")

    spielbergMovieIds = set([movieId for movieId, _, _ in movies.triples((None, "directed_by", spielbergId))])

    harrisonfordId = movies.value(None, "name", "Harrison Ford")

    harrisonfordMovieIds = set([movieId for movieId, _, _ in movies.triples((None, "starring", harrisonfordId))])

    print [movies.value(movieId, "name", None) for movieId in spielbergMovieIds.intersection(harrisonfordMovieIds)]








