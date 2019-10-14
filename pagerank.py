import networkx as nx
import operator
import pickle

'''PageRank works on a directed weighted graph. If page A has a link to page B, 
then the score for B goes up, i.e. the more input the page B (node) have, 
the higher is its score.'''


def main():
    #input data: /home/olivera/Documents/data/filtered005vornoi_graphs/november/graph_vornoi_nov01.csv
    path = "/home/olivera/Documents/data"

    date = ["nov01", "nov02", "nov03", "nov04", "nov05", "nov06", "nov07", "nov08",
            "nov09", "nov10", "nov11", "nov12", "nov13", "nov14", "nov15",
            "nov16", "nov17", "nov18", "nov19", "nov20", "nov21", "nov22",
            "nov23", "nov24", "nov25", "nov26", "nov27", "nov28", "nov29",
            "nov30", "dec01", "dec02", "dec03", "dec04", "dec05", "dec06",
            "dec07", "dec08", "dec09", "dec10", "dec11", "dec12", "dec13",
            "dec14", "dec15", "dec16", "dec17", "dec18", "dec19", "dec20",
            "dec21", "dec22", "dec23", "dec24", "dec25", "dec26", "dec27",
            "dec28", "dec29", "dec30", "dec31", "jan01"]

    for d in date:
        graph = path + "/filtered005vornoi_graphs/graph_vornoi_" + d + ".csv"
        wfile = path + "/pagerank_by_date/pagerank_" + d + ".pkl"
        D = nx.Graph()
        with open(graph, 'r') as g:
            lines = g.readlines()[1:]
            for line in lines:
                el = line.split(',')
                id1 = el[0].strip()
                id2 = el[1].strip()
                w = float(el[2].strip())
                D.add_weighted_edges_from([(id1, id2, w)])

        pagerank_dict = nx.pagerank(D)
        with open(wfile, "wb") as wf:
            pickle.dump(pagerank_dict, wf)



    #D = nx.DiGraph()
    #D = nx.Graph()
    #D.add_weighted_edges_from([('A','B',2.5),('A','C',5.5)])


    #print(pagerank_dict)
    #max_pg = max(pagerank_dict.items(), key=operator.itemgetter(1))[0]
    #print("Node with max page rank ", max_pg)
    #sorted_dict = sorted(pagerank_dict, key=pagerank_dict.get, reverse=True)
    #print(sorted_dict)
    #print(pagerank_dict['104'])







if __name__=='__main__':
    main()