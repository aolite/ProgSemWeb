from myTripleStore import SimpleGraph

if __name__ == "__main__":
    print "----- PLACES -----"

    print "Loading place triples..."

    places_graph = SimpleGraph()

    places_graph.load("../resources/place_triples.txt")

    print "Places graph read..."

    print "Tel me everything about San Francisco"

    for sf_triples in places_graph.triples((None, "name", "San Francisco")):
        print sf_triples





