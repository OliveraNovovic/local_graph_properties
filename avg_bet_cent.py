import networkx as nx
import operator
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def Average(lst):
    return sum(lst) / len(lst)

def plot_values(dist_array, avg, i):
    #import matplotlib as plt
    #plt.rcParams.update({'figure.max_open_warning': 0})
    fig, ax1 = plt.subplots()
                    #start,stop,step
    t = np.arange(1.00, 63.0, 1.00)
    #s1 = np.exp(t)
    s1 = np.array(dist_array)
    s2 = np.array([avg for i in range(1,63)])
    ax1.plot(t, s1, 'b-', label='betweenness_centrality_per_day')
    ax1.plot(t, s2, 'r--', label='avg_betweenness_centrality')
    ax1.set_xlabel('days', fontsize='x-large')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_ylabel('betweenness centrality', color='b', fontsize='x-large')
    ax1.tick_params('y', colors='b')
    legend = ax1.legend(loc='upper right', shadow=True, fontsize='x-large')
    ax1.set_title('Polygon ' + str(i), fontsize='x-large')

    fig.tight_layout()
    #plt.show()
    fig_name = "betcent_poly_" + str(i) + ".png"
    plt.savefig(fig_name)

def betcent_average(dfObj):
    #print(dfObj.loc[dfObj['node'] == 1])
    #subset of a dataframe where node = 1
    df_betcent = pd.DataFrame(columns=['poly', 'avg_betcent'])
    for i in range(1, 314):
        df_subs = dfObj.loc[dfObj['node'] == i]
        betcent_list = df_subs['local_graph_properties'].tolist()
        betcent_mean = df_subs['local_graph_properties'].mean()
        print("Betweenness centrality mean for node ", i, betcent_mean)
        plot_values(betcent_list, betcent_mean, i)
        df_betcent = df_betcent.append({'poly': str(i), 'avg_betcent': betcent_mean}, ignore_index=True)
    return df_betcent


def main():
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
    dfObj = pd.DataFrame(columns=['date', 'node', 'local_graph_properties'])

    for d in date:
        betcent_file = path + "/betcent_by_date/betcent_" + d + ".pkl"
        with open(betcent_file, 'rb') as betcdf:
            betcent_dict = pickle.load(betcdf)
            betcent_list = []
            for i in range(1, 314):
                node = str(i)
                betcent_node_value = betcent_dict[node]
                #print(d, node, pgrank_node_value)
                #pg_value_list.append(pgrank_node_value)
                # Append rows in Empty Dataframe by adding dictionaries
                dfObj = dfObj.append({'date': d, 'node': i, 'local_graph_properties': betcent_node_value}, ignore_index=True)

    #print(pgr_average(dfObj))
    betcent_average(dfObj).to_csv("avg_betcent_per_poly.csv", index=False)





if __name__=='__main__':
    main()