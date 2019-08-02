import election
list_of_results = election.get_results()
import matplotlib.pyplot as plt
from matplotlib.pyplot import FuncFormatter
import numpy as np

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

for i in range(len(list_of_results)):
    loc_list.append(list_of_results[i]["Locations"]["State "])

#fig = go.Figure(data=go.Choropleth(locationmode = 'USA-states', locations=list_of_results[1]["Location"]["State"], z = list_of_results[1]["Vote Data"]["Donald Trump"]["Number of Votes"], colorscale = scl, colorbar_title = "Right to Left"))
fig = go.Figure(data=go.Choropleth(locationmode='USA-states', locations=tuple(list_of_results[]["Location"]["State Abbreviation"]), z))
fig.update_layout(title_text = '2016 Primary Results - Sanders vs. Trump', geo_scope = 'usa')

fig.show()
