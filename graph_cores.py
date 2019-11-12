import pandas as pd

def cores_average(dfObj):
    #print(dfObj.loc[dfObj['node'] == 1])
    #subset of a dataframe where node = 1
    df_cores = pd.DataFrame(columns=['poly', 'avg_core_num'])
    for i in range(1, 314):
        df_subs = dfObj.loc[dfObj['node'] == i]
        cores_list = df_subs['core_num'].tolist()
        cores_mean = df_subs['core_num'].mean()
        print("Core number mean for node ", i, cores_mean)
        #plot_values(betcent_list, betcent_mean, i)
        df_cores = df_cores.append({'poly': str(i), 'avg_core_num': cores_mean}, ignore_index=True)
    return df_cores

#/home/olivera/Documents/data/cores/november_wcores/wcores_nov_1.txt
#/home/olivera/Documents/data/cores/december_wcores/wcores_dec_1.txt

def main():
    path = "/home/olivera/Documents/data/cores"

    date = ["nov_1", "nov_2", "nov_3", "nov_4", "nov_5", "nov_6", "nov_7", "nov_8",
            "nov_9", "nov_10", "nov_11", "nov_12", "nov_13", "nov_14", "nov_15",
            "nov_16", "nov_17", "nov_18", "nov_19", "nov_20", "nov_21", "nov_22",
            "nov_23", "nov_24", "nov_25", "nov_26", "nov_27", "nov_28", "nov_29",
            "nov_30", "dec_1", "dec_2", "dec_3", "dec_4", "dec_5", "dec_6",
            "dec_7", "dec_8", "dec_9", "dec_10", "dec_11", "dec_12", "dec_13",
            "dec_14", "dec_15", "dec_16", "dec_17", "dec_18", "dec_19", "dec_20",
            "dec_21", "dec_22", "dec_23", "dec_24", "dec_25", "dec_26", "dec_27",
            "dec_28", "dec_29", "dec_30", "dec_31", "jan_1"]


    # Creating an empty Dataframe with column names only
    dfObj = pd.DataFrame(columns=['date', 'node', 'core_num'])

    for d in date:
        core_file = path + "/wcores_" + d + ".txt"
        with open(core_file, 'r') as cf:
            cores_df = pd.read_csv(cf, names=['node', 'core_num'])
            #print(cores_df.node)
            cores_list = []
            for i in range(1, 314):
                node = str(i)
                core_num_node = cores_df.loc[cores_df.node == i]['core_num'].item()
                #print(d, node, core_num_node)
                # Append rows in Empty Dataframe by adding dictionaries
                dfObj = dfObj.append({'date': d, 'node': i, 'core_num': core_num_node}, ignore_index=True)

    #print(dfObj)
    cores_average(dfObj).to_csv("avg_core_num_per_poly.csv", index=False)





if __name__=='__main__':
    main()
