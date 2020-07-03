import bs4 as bs
import pandas as pd
import requests
import numpy as np



def save_tickers():
	resp=requests.get('https://en.wikipedia.org/wiki/History_of_Amazon')
	soup=bs.BeautifulSoup(resp.text)
	tables=soup.findAll('table',{'class':'wikitable sortable'})
	years=[]
	mds=[]
	events=[]
	dets=[]
	i=0
	for table in tables:
		#print(table)
		#print("**********************************************************************************************")
		if i==0:
			i=1
			continue
		for row in table.findAll('tr')[1:]:
			year=row.findAll('td')[0].text
			if '\n' in year:
				year=year[:-1]
			print(year)
			years.append(year)
			Md=row.findAll('td')[1].text
			if '\n' in Md:
				Md=Md[:-1]
			mds.append(Md)
			event=row.findAll('td')[2].text
			if '\n' in event:
				event=event[:-1]
			events.append(event)
			det=row.findAll('td')[3].text
			if '\n' in det:
				det=det[:-1]
			dets.append(det)
	#print(years)
	#print(mds)
	#print(events)
	#print(dets)
	
	name='Amazon_details.csv'
	year_a=np.array(years)
	md_a=np.array(mds)
	event_a=np.array(events)
	det_a=np.array(dets)
	#long_sp_a=np.array(long_sp)
#		print(len(lat_a))
#		print(len(long_a))
#		print(len(lat_sp_a))
#		print(len(long_sp_a))						

	d={'year':year_a,'Mon_and_day':md_a,'events':event_a,'details':det_a,}
	df=pd.DataFrame(d)
	#df=pd.DataFrame(list(zip(year,Md,events,dets)),columns=['Year','Mon_and_day','Event','Details'])
	df.to_csv(name,index=False)


save_tickers()


