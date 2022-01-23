#!/usr/bin/env python
# coding: utf-8

# In[55]:


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objs as go
import time


# In[3]:


url = 'https://www.capital.gr/finance/el/allstocks/1'
result =requests.get(url)


# In[4]:


soup = BeautifulSoup(result.text,'html.parser')
page = soup.find('div',{'class':'cp__table'})


# In[43]:


quotes=[]
for i in page.find_all('td'):
    try:
        z=(i.a.text)
        try:
            if int(z[0])>=0:
                pass
        except:
            z=z.replace(' ','')
            quotes.append(z)
    except:
        pass


# In[240]:


stock = []
price = []
change = []
change_percentage = []
open = []
high = []
low = []
volume =[] 
turnover =[]
acts = []
buyers = []
sellers =[]
capitalization = [] 
ticker=[]
market=[]

c=0
for i in quotes:
    try:
        url1='https://www.capital.gr/finance/quote/'+i
        result2 = requests.get(url1)
        soup2 = BeautifulSoup(result2.text,'lxml')
        
        ticker.append(i)
        market.append('Athens Stock Market')
        try:
            stock.append(soup2.find('h1',{'class':'bold serif h1ash2'}).text)
        except: 
            stock.append(np.nan)
        
        try:
            price.append(soup2.find('h3',{'class':'price bold'}).span.text.replace(',','.'))
        except:
            price.append(np.nan)

        try:
            try:
                changes = soup2.find('h4',{'class':'winner change'}).find_all('span')
            except:
                changes = soup2.find('h4',{'class':'change'}).find_all('span')
        except:
            pass
        try:
            change.append(changes[0].text.replace(',','.'))
        except:
            change.append(np.nan)
            tickerperc.append(np.nan)
        try:
            z=changes[1].text.replace('(','').replace(')','').replace(',','.').replace('%','')
            change_percentage.append(float((z)))
            tickerperc.append(str(str(i)+' \n'+str(float((z))))+'%')
        except: 
            change_percentage.append(np.nan)
        try:
            financial_data = soup2.find('div',{'class':'finance__details__right'}).find_all('span')
        except:
            pass
        
        try:
            open.append(financial_data[0].text)
        except:
            open.append(np.nan)
        try:
            high.append(financial_data[1].text)
        except:
            high.append(np.nan)
        try:
            low.append(financial_data[2].text)
        except: 
            low.append(np.nan)
        try:
            volume.append(financial_data[3].text)
        except:
            volume.append(np.nan)
        try:    
            turnover.append(financial_data[4].text)
        except:
            turnover.append(np.nan)
        try:
            acts.append(financial_data[5].text)
        except:
            acts.append(np.nan)
        try:    
            buyers.append(financial_data[6].text)
        except:
            buyers.append(np.nan)
        try:    
            sellers.append(financial_data[7].text)
        except:
            sellers.append(np.nan)
        try:   
            capitalization.append(int(financial_data[8].text.replace('.','').replace(' €','')))
        except:
            capitalization.append(np.nan)
        
        c=c+1
        print(c)
    except:
        pass
   


# In[241]:


building_materials=['AKRIT','ΒΙΟΚΑ','ΙΚΤΙΝ','ΑΛΜΥ','ΜΑΘΙΟ','TITC']


# In[242]:


food_and_beverages_wine=['ΕΕΕ','ΜΠΟΠΑ','ΜΠΟΚΑ','ΚΤΗΛΑ','ΚΜΟΛ','ΕΒΡΟΦ','ΚΡΙ','ΣΑΡΑΝ','ΚΕΠΕΝ','ΛΟΥΛΗ','ΝΙΚΑΣ']


# In[243]:


insurance=['ΕΥΠΙΚ','ΜΠΡΙΚ']


# In[244]:


agriculture=['ΣΠΥΡ','ΚΡΕΚΑ']


# In[245]:


industry = ['ΜΥΤΙΛ','ΛΕΒΚ','ΛΕΒΠ','ΠΕΤΡΟ','ΣΑΤΟΚ','ΒΑΡΓ','ΔΡΟΜΕ',
            'CENER','ΜΕΝΤΙ','ΚΑΡΕΛ','ΦΛΕΞΟ','ΒΙΣ','ΠΑΙΡ']


# In[246]:


industrial_manifacturers=['ΦΡΙΓΚΟ','ΒΙΟΣΚ','ΔΙΟΝ','ΒΟΣΥΣ','ΓΕΒΚΑ',
                          'ΕΛΤΟΝ','ΞΥΛΚ','ΞΥΛΠ','ΙΝΤΕΤ']


# In[247]:


construction = ['ΙΝΚΑΤ','ΑΒΑΞ','ΒΙΟΤ','ΓΕΚΤΕΡΝΑ','ΔΟΜΙΚ','ΕΚΤΕΡ','ΕΛΛΑΚΤΩΡ',
               'ΚΛΜ','ΠΡΔ']


# In[248]:


real_estate = ['ΙΝΤΕΡΚΟ','ΤΡΑΣΤΟΡ','ΠΡΟΝΤΕΑ','ΛΑΜΨΑ','ΛΑΜΔΑ','ΠΡΕΜΑ',
               'ΚΑΜΠ','ΕΛΒΙΟ','ΚΕΚΡ','ΑΣΤΑΚ','ΜΙΓΡΕ']


# In[249]:


financial = ['CNLCAP','ΜΙΓ','ΑΝΔΡΟ','ΕΧΑΕ','ΣΕΝΤΡ','ΑΛΦΑ','ΑΤΤ','ΕΥΡΩΒ',
            'ΕΤΕ','ΕΛΛ','ΠΕΙΡ']


# In[250]:


consumer_and_retail = ['ΠΛΑΙΣ','ΦΡΛΚ','ΣΑΡ','ΠΑΠ','ΑΤΕΚ','ΛΙΒΑΝ',
                       'ΛΑΝΑΚ','ΜΟΝΤΑ','ΑΣΚΟ','ΓΓΓΚΡΠ','ΜΟΤΟ','ΝΑΚΑΣ',
                       'ΕΛΓΕΚ','ΥΑΛΚΟ','ΓΕΔ','ΜΙΝ','ΕΛΒΕ','ΔΟΥΡΟ','ΜΠΕΛΑ','ΦΦΓΚΡΠ']


# In[251]:


energy_and_oil = ['ΕΛΙΝ','ΜΟΗ','ΡΕΒΟΙΛ','ΤΕΝΕΡΓ','ΕΛΠΕ','ΔΕΗ','ΑΔΜΗΕ']


# In[252]:


telematics = ['ΣΠΕΙΣ','ΟΤΕ']


# In[253]:


textiles = ['ΒΑΡΝΗ','ΜΟΥΖΚ','ΕΠΙΛΚ','ΝΑΥΠ','ΑΑΑΚ','ΑΑΑΠ','ΦΙΕΡ']


# In[254]:


technology = ['ΕΠΣΙΛ','ΛΟΓΟΣ','ΜΛΣ','ΕΝΤΕΡ','ΙΛΥΔΑ','ΣΠΙ','ΙΝΤΕΚ'
             'ΒΥΤΕ','ΠΡΟΦ','ΚΟΥΑΛ','ΚΟΥΕΣ','ΙΝΤΚΑ']


# In[255]:


metalurgy_and_plastic = ['ΜΕΒΑ','ΒΙΟ','ΕΛΧΑ','ΔΑΙΟΣ','ΠΛΑΘ','ΠΛΑΚΡ',
                         'ΚΟΡΔΕ','ΕΛΣΤΡ','ΜΠΤΚ','ΣΙΔΜΑ','ΤΖΚΑ','ΜΕΡΚΟ',]


# In[256]:


travel_and_tourism = ['ΑΤΤΙΚΑ','ΑΝΕΠΟ','ΑΝΕΚ','ΑΝΕΠ','ΚΥΡΙΟ','ΑΡΑΙΓ','ΟΤΟΕΛ','ΜΙΝΟΑ']


# In[257]:


gambling = ['ΙΝΛΟΤ','ΟΠΑΠ']


# In[258]:


water = ['ΕΥΔΑΠ','ΕΥΑΠΣ']


# In[259]:


health = ['ΙΑΣΩ','ΙΑΤΡ','ΟΛΥΜΠ']


# In[260]:


not_active = ['TITK','ΑΤΕ','ΚΥΠΡ','ΜΕΤΚ','ΣΙΔΕ']


# In[261]:



k=0
group=[]
for i in ticker:
    if i in building_materials:
        group.append('Building Materials')
    elif i in food_and_beverages_wine:
        group.append('Food and Drinks')
    elif i in insurance:
        group.append('Insurance')
    elif i in agriculture:
        group.append('Agriculture')
    elif i in industry:
        group.append('Industry')
    elif i in industrial_manifacturers:
        group.append('Industrial Manifacturers')
    elif i in construction:
        group.append('Construction')
    elif i in real_estate:
        group.append('real_estate')
    elif i in financial:
        group.append('Financial')
    elif i in consumer_and_retail:
        group.append('Consumer and Retail')
    elif i in energy_and_oil:
        group.append('Energy and Oil')
    elif i in telematics:
        group.append('Telematics')
    elif i in textiles:
        group.append('Textiles')
    elif i in technology:
        group.append('Technology')
    elif i in metalurgy_and_plastic:
        group.append('Metalurgy and plastic')
    elif i in travel_and_tourism:
        group.append('Travel and Tourism')
    elif i in gambling:
        group.append('Gambling')
    elif i in water:
        group.append('Water')
    elif i in health:
        group.append('Health')
    else:
        group.append('Other')
    k=k+1

    
        


# In[262]:


data=pd.DataFrame({
'stock': stock,
'ticker' : ticker,
'price':price,
'change': change,
'change_percentage' : change_percentage,
'group': group,
#'open' : open,
#'high' : high,
#'low' : low,
#'volume' : volume,
#'turnover' : turnover,
#'acts' : acts,
#'buyers' : buyers,
#'sellers' : sellers,
'capitalization' : capitalization
                  })
data = data[data['stock'].notna()]


# In[263]:


data = data[data.change != '0.0000']


# In[421]:


data.to_csv('finviz.csv')


# In[358]:


price_=data.price.tolist()
change_percentage_=data.change_percentage.tolist()
ticker_=data.ticker.tolist()


# In[404]:


fig=px.treemap(data, path=[px.Constant('Athens Stock Exchange'),'group','ticker'],values = 'capitalization', color = 'change_percentage',color_continuous_scale=['Red','Red','Red','Red','Red','Red','Red','crimson','firebrick','gray','Green','limegreen','limegreen','lime','lime','lime','lime','lime','lime'],color_continuous_midpoint=0)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.update_traces(marker_line=dict(color="black"))
fig.update_traces(marker_line_width = 0.5)
#fig.data[0].customdata = np.column_stack([price_, change_percentage_,ticker_])
#fig.data[0].texttemplate = "Ticker:%{customdata[2]}<br>Price:$%{customdata[0]}<br>Percentage Change:%{customdata[1]:.2f}%"
st.plotly_chart(fig, use_container_width=True, sharing="streamlit")
time.sleep(500000)

