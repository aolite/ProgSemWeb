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



