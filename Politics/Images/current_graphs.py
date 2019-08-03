import matplotlib.pyplot as plt
import numpy as np

'''data = {'Bennet' : 0.2,
'Biden': 32.0,
'Booker' : 1.6,
'Bullock' : 0.2,
'Buttigieg' : 5.6,
'Castro' : 1.0,
'de Blasio' : 0.4,
'Delaney' : 0.8,
'Gabbard' : 1.0,
'Gillibrand' : 0.4,
'Harris' : 11.0,
'Hickenlooper' : 0.4,
'Klobuchar' : 0.6,
"O'Rourke" : 3.0,
'Ryan' : 0.6,
'Sanders' : 16.4,
'Steyer' : 0.8,
'Warren' : 14.8,
'Williamson' : 0.4,
'Yang' : 1.6}'''

names = ['Bennet','Biden','Booker','Bullock','Buttigieg','Castro','de Blasio','Delaney','Gabbard','Gillibrand','Harris','Hickenlooper','Inslee','Klobuchar','Messam','Moulton','O’Rourke','Ryan','Sanders','Sestak','Steyer','Warren','Williamson','Yang']
values = [0.2,32.0,1.6,0.2,5.6,1.0,0.4,0.8,1.0,0.4,11.0,0.4,0.6,3.0,0.6,16.4,0.8,14.8,0.4,1.6]

bars = names
height = values
y_pos = np.arange(len(bars))
bar_plot = plt.bar(y_pos, height, color='blue')
plt.xticks(y_pos, bars)
#plt.yticks([0, 0.5, 5, 50], ['0%', '0.5%', '5%', '50%'])
plt.title('Current Poll Data of Democratic Candidate Popularity')
plt.xlabel('Candidates')
plt.ylabel('Percentage of Voter Support')

plt.text

#create labels for each bar
def autolabel(i):
    for i in enumerate(bar_plot):
        height = i.get_height()
        plt.text(i.get_x() + i.get_width()/2, 1.05*height, bar_label(values[i]), ha='center', va='bottom', rotation=90)

autolabel(bar_plot)

plt.show()
