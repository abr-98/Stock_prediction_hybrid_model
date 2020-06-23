import os
import pandas as pd
import pickle


def compile():
	with open("tickers.pickle",'rb') as f:
			tickers=pickle.load(f)


	main_df=pd.DataFrame()

	for count,ticker in enumerate(tickers):
		if 'AMZN' in ticker:
			continue
		if not os.path.exists('stock_details/{}.csv'.format(ticker)):
			continue
		df=pd.read_csv('stock_details/{}.csv'.format(ticker))
		df.set_index('Date',inplace=True)

		df.rename(columns={'Adj Close': ticker}, inplace=True)
		df.drop(['Open','High','Low',"Close",'Volume'],axis=1,inplace=True)

		
		if main_df.empty:
			main_df=df
		else:
			main_df=main_df.join(df,how='outer')

	print(main_df.head())
	main_df.to_csv('Dataset_temp.csv')

compile()
