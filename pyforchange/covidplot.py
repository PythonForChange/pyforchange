import pandas as pd
from datetime import datetime

def dateNow():
  now = datetime.now()
  month=now.month
  if (month<10):
    month='0'+str(month)
  else:
    month=str(month)
  d=str(now.year)+"-"+month+"-"+str(now.day)
  return d

class CovidData:
  def __init__(self, country='Chile',adress='https://covid.ourworldindata.org/data/owid-covid-data.csv'):
    self.adress=adress
    self.country=country
    self.reset()
  def reset(self):
    data = pd.read_csv(self.adress)
    data_country = data[data['location']==self.country]
    self.data_country_indexed = data_country.set_index('date')
  def plot(self,param):
    print(param+" in "+self.country+" since 2020-01-01 until "+dateNow())
    if(param=="vacunas"):
      param='new_vaccinations_smoothed'
    if(param=="casos"):
      param='new_cases_smoothed'
    subdata=self.data_country_indexed.loc["2020-01-01":dateNow(), param]
    subdata.plot()