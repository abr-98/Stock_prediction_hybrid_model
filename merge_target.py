import pandas as pd


def merge():
	df1=pd.read_csv('dataset_target_2.csv',index_col='Date')

	df3=pd.read_csv('dataset_target.csv')
	df2=pd.read_csv('Dataset_temp.csv',index_col='Date')

	Dates=[]
	i=0
	while i<len(df3):
		Dates.append(df3.iloc[i]['Date'])
		i+=1
		
	
	df_new=df1.join(df2,how='outer')
	df_new.fillna(0.0)

	df_new['Date']=Dates

	df_new.to_csv('Dataset_main.csv',index=False)

merge()