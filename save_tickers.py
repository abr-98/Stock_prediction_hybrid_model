import bs4 as bs
import pickle
import requests


def save_tickers():
	resp=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup=bs.BeautifulSoup(resp.text)
	table=soup.find('table',{'class':'wikitable sortable'})
	tickers=[]
	for row in table.findAll('tr')[1:]:
		ticker=row.findAll('td')[0].text[:-1]
		tickers.append(ticker)

	with open("tickers.pickle",'wb') as f:
		pickle.dump(tickers, f)


	return tickers

save_tickers()




