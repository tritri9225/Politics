import election
list_of_results = election.get_results()
import matplotlib.pyplot as plt
from matplotlib.pyplot import FuncFormatter
import numpy as np
import plotly.graph_objs as go

t_total = 0
s_total = 0

for i in range(len(list_of_results)):
    trump = int(list_of_results[i]["Vote Data"]["Donald Trump"]["Number of Votes"])
    t_total += trump
    sanders = int(list_of_results[i]["Vote Data"]["Bernie Sanders"]["Number of Votes"])
    s_total += sanders

#print("trump's total: " + str(t_total))
#print("bernie's total: " + str(s_total))

bars = ("Trump", "Sanders")
height = [t_total, s_total]
y_pos = np.arange(len(bars))
plt.bar(y_pos, height)
plt.xticks(y_pos, bars)

plt.yticks([0, 5000000, 10000000, 15000000], [0, '5 Million', '10 Million', '15 Million'])

plt.bar(y_pos, height, color=['red', 'blue'])


plt.title('2016 Election Results')
plt.xlabel('Candidates')
plt.ylabel('Number of Votes')
plt.text(-.19, 13302541, '13,302,541')
plt.text(0.82, 11959102, '11,959,102')

#fig = go.Figure()
#plt.show()
scl = (0, "rgb(0, 0, 255)"), (1, "rgb(255, 0, 0)")
#for i in range(len(list_of_results)):

loc_list = []
votes = 0
county_dict = {}

for i in range(len(list_of_results)):
    county_dict[list_of_results[i]["Location"]["County"]] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    #print(list_of_results[i]["Location"]["State Abbreviation"])
    #print(list_of_results[i]["Vote Data"]["Donald Trump"])
    '''if list_of_results[i]["Location"]["State Abbreviation"] == 'AL':
        state_dict['AL'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'AK':
        state_dict['AK'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'AZ':
        state_dict['AZ'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'AR':
        state_dict['AR'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'CA':
        state_dict['CA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'CO':
        state_dict['CO'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'CT':
        state_dict['CT'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'DE':
        state_dict['DE'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'FL':
        state_dict['FL'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'GA':
        state_dict['GA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'HI':
        state_dict['HI'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'ID':
        state_dict['ID'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'IL':
        state_dict['IL'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'IN':
        state_dict['IN'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'IA':
        state_dict['IA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'KS':
        state_dict['KS'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'KY':
        state_dict['KY'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'LA':
        state_dict['LA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'ME':
        state_dict['ME'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'MD':
        state_dict['MD'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'MA':
        state_dict['MA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'MI':
        state_dict['MI'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'MN':
        state_dict['MN'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'MS':
        state_dict['MS'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'MO':
        state_dict['MO'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'MT':
        state_dict['MT'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'NE':
        state_dict['NE'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'NV':
        state_dict['NV'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'NH':
        state_dict['NH'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'NJ':
        state_dict['NJ'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'NM':
        state_dict['NM'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'NY':
        state_dict['NY'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'NC':
        state_dict['NC'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'ND':
        state_dict['ND'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'OH':
        state_dict['OH'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'OK':
        state_dict['OK'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'OR':
        state_dict['OR'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'PA':
        state_dict['PA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'RI':
        state_dict['RI'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'SC':
        state_dict['SC'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'SD':
        state_dict['SD'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'TN':
        state_dict['TN'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'TX':
        state_dict['TX'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'UT':
        state_dict['UT'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'VT':
        state_dict['VT'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'VA':
        state_dict['VA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'WA':
        state_dict['WA'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'WV':
        state_dict['WV'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'WI':
        state_dict['WI'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]
    if list_of_results[i]["Location"]["State Abbreviation"] == 'WY':
        state_dict['WY'] = list_of_results[i]["Vote Data"]["Donald Trump"]["Percent of Votes"]'''
print(county_dict)


for i in range(len(list_of_results)):
    loc_list.append(list_of_results[i]["Location"]["State"])
#make a dictionary with states as keys and percentage of votes for values.
for state in loc_list:
    votes = state[i]['Vote Data']['Donald Trump']['Percentage of Votes']
fig = go.Figure(data=go.Choropleth(locationmode='USA-states', locations=loc_list, z = votes, colorscale = scl, colorbar_title = "Right to Left"))
fig.update_layout(title_text = '2016 Primary Results - Sanders vs. Trump', geo_scope = 'usa')

#fig.show()
