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

plt.show()
