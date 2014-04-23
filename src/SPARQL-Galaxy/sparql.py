
import sys
import rdflib

def main(argv):
    
    logging.basicConfig()
    g = rdflib.Graph()
    g.parse(argv[1])
    results = g.query(argv[2])
    print "<table>"
    print "<tr>"
    for key in results.bindings[1].keys():
        print "<td><b>" + key +"</b></td>"
    print "</tr>"
    for binding in results.bindings:
        print "<tr>"
        for value in binding.values():  
            if isinstance(value, rdflib.term.URIRef):
                print "<td><a href=\"" + value +"\">"+ value +"</a></td>"
            else:
                print "<td>"+ value +"</td>"
        print "</tr>"
    print "</table>"
    
if __name__ == "__main__":
    main(sys.argv)