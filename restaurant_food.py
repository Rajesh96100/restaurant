import pandas as pd
import sys


def analyze_log_file(path):
    df=pd.read_csv(path, names=['eater_id', 'foodmenu_id'])
    grouped_data=df.groupby(['eater_id', 'foodmenu_id']).size().reset_index(name='counts')
    sorted_data=grouped_data.sort_values('counts', ascending=False)
    count=sorted_data['counts'].max()
    if count>1 :
       raise Exception
    df2=df.groupby(['foodmenu_id']).size().reset_index(name='counts').sort_values('counts', ascending=False)
    df3=df2.iloc[[0,1,2]]
    df4=df3['foodmenu_id']
    print(df4)


if _name_ == "_main_":
    path = sys.argv[1]
    analyze_log_file(path)
