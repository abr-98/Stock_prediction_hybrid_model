import pandas as pd
import numpy as np

def create_data():
	months=['January','February','March','April','May','June','July','August','September','October','November','December']
	years=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

	dates=[]
	events=[]

	#2010-01-07

	i=0
	df=pd.read_csv('Amazon_details.csv')

	while i<len(df):

		year= df.iloc[i]['year']
		print(year)
		if str(year) in years:
			#i+=1
			#continue
		#else:
			print("A")
			m=df.iloc[i]['Mon_and_day']
			if " " in m:
				mon=m.split(" ")[0]
				days=m.split(" ")[1]
			else:
				mon=m
				days=1

			
			month=months.index(mon)+1

			ext=0
			while ext<15:
				days=int(days)
				day=days+ext
				if day>29:
					days=1
					month=month+1

				if day<10:
					day_f='0'+str(day)
				else:
					day_f=str(day)
				if month<10:
					mon_f='0'+str(month)
				else:
					mon_f=str(month)

				
				date=str(year)+'-'+mon_f+'-'+day_f
				print(date)
				dates.append(date)

				events.append(df.iloc[i]['events'])
				ext+=1
		i+=1
	name='Amazon_details_final.csv'
	
	event_a=np.array(events)
	date_a=np.array(dates)
	#long_sp_a=np.array(long_sp)
#		print(len(lat_a))
#		print(len(long_a))
#		print(len(lat_sp_a))
#		print(len(long_sp_a))						

	d={'dates':date_a,'events':event_a}
	df=pd.DataFrame(d)
	#df=pd.DataFrame(list(zip(year,Md,events,dets)),columns=['Year','Mon_and_day','Event','Details'])
	df.to_csv(name,index=False)


create_data()

