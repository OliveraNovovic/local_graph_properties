import pandas as pd


def main():
    path = "/home/olivera/Documents/data"
    df = pd.read_pickle(path + "/betcent_by_date/betcent_nov01.pkl")
    print(df)

if __name__ == '__main__':
    main()