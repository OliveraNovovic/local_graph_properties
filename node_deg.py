import networkx as nx
import pandas as pd
import operator
import pickle

'''
Node degree represent the number of edges adjacent to the node. 
The weighted node degree is the sum of the edge weights for edges incident to that node.
'''

def deg_average(dfObj):
    #print(dfObj.loc[dfObj['node'] == 1])
    #subset of a dataframe where node = 1
    df_degree = pd.DataFrame(columns=['poly', 'avg_degree', 'avg_w_degree'])
    for i in range(1, 314):
        df_subs = dfObj.loc[dfObj['node'] == i]
        #degree_list = df_subs['degree'].tolist()
        degree_mean = df_subs['degree'].mean()
        #w_degree_list = df_subs['weighted_degree'].tolist()
        w_degree_mean = df_subs['weighted_degree'].mean()
        df_degree = df_degree.append({'poly': str(i), 'avg_degree': int(degree_mean), 'avg_w_degree': w_degree_mean},
                                     ignore_index=True)
    return df_degree


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

    # Creating an empty Dataframe with column names only
    dfObj = pd.DataFrame(columns=['date', 'node', 'degree', 'weighted_degree'])

    for d in date:
        graph = path + "/filtered005vornoi_graphs/graph_vornoi_" + d + ".csv"
        #wfile = path + "/betcent_by_date/betcent_" + d + ".pkl"
        D = nx.Graph()
        with open(graph, 'r') as g:
            lines = g.readlines()[1:]
            for line in lines:
                el = line.split(',')
                id1 = el[0].strip()
                id2 = el[1].strip()
                w = float(el[2].strip())
                D.add_weighted_edges_from([(id1, id2, w)])

        #node degree of every node
        for i in range(1, 314):
            node = str(i)
            node_deg = D.degree(node)
            w_node_deg = D.degree(node, weight='weight')
            dfObj = dfObj.append({'date': d, 'node': i, 'degree': node_deg, 'weighted_degree': w_node_deg},
                                 ignore_index=True)

    #print(dfObj)
    deg_average(dfObj).to_csv("avg_node_w_degree.csv", index=False)




if __name__=='__main__':
    main()