import streamlit as st
from datetime import datetime
import pandas as pd
import requests
import json
from streamlit_extras.app_logo import add_logo
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit as st
import pandas as pd


# add picture in sidebar:
add_logo("assets/card.jpg", height=300)

# Title
st.title("Data Visualization") # Displays title
st.subheader("") # Displays subheader

# Insert text field:

# if word in list return lat and lon if not return string : place not found


# Loading the weather data:
url ="https://api.open-meteo.com/v1/forecast?latitude=61.90&longitude=5.99&hourly=temperature_2m"
response = requests.request("GET", url)
result = response.text

data = json.loads(result)

# get current time:
now = datetime.now()
date_now = now.strftime("%d %B, %Y")
time_now = now.strftime("%H:%M:%S")
current_time = now.strftime("%H:00")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Today's Date :earth_africa:" , value=date_now, )
with col2:
    st.metric(label="Time :clock2::", value=time_now)

add_vertical_space(1)

city = st.text_input('City name', 'Nordfjordeid')
post = st.text_input('postcode', '6770')
country = st.text_input('Country', 'Norway')   #lag om til ei liste
st.write(city, post, country)





























#list of todays temperatures
temp = data["hourly"]["temperature_2m"]
temp = temp[0:24]

#list of hours, saving only time in list, not date
tim = data["hourly"]["time"]
tim = tim[0:24]
tim = [x[-5:] for x in tim]

# getting the current temperature: 
current_temp = []
for i in range(len(tim)):
    if tim[i] == current_time:
        current_temp.append(temp[i])
    else:
        current_temp.append(0)

d = {"Temp":temp, "Time": tim}
nooo = {"Temp":current_temp, "Time": current_time}


df1 = pd.DataFrame(d)
df2 = pd.DataFrame(nooo)

current = max(df2.Temp)
maximum = max(df1.Temp)
minimum = min(df1.Temp)


for i, row in df1.iterrows():
    if row["Temp"] == maximum:
        max_time = row["Time"]
    if row["Temp"] == minimum:
        min_time = row["Time"]
    if row["Temp"] == current:
        current_time = row["Time"]
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(label="Current Temperature", value=current)
with c2:
    st.metric(label="Max Temperature: " + max_time, value=maximum)
with c3:
    st.metric(label="Min Temperature: " + min_time, value=minimum)

max_temp = []
for i in range(len(tim)):
    if tim[i] == max_time:
        max_temp.append(temp[i])
    else:
        max_temp.append(0)

maxim = {"Tempm":max_temp, "Time": max_time}
df3 = pd.DataFrame(maxim)

min_temp = []
for i in range(len(tim)):
    if tim[i] == min_time:
        min_temp.append(temp[i])
    else:
        min_temp.append(0)

minim = {"Temp":min_temp, "Time": min_time}
df4 = pd.DataFrame(minim)

hmm = pd.merge(df1, df2, how='left', on='Time')
hmmm = pd.merge(hmm, df3, how='left', on='Time')
hmmmm = pd.merge(hmmm, df4, how='left', on='Time')

df = hmmmm.set_index("Time")

st.line_chart(df)







