import election
list_of_results = election.get_results()
#import pandas as pd
import matplotlib.pyplot as plt
#df = pd.read_csv("election(2).csv")

t_total = 0
b_total = 0

for i in range(len(list_of_results)):
    trump = int(list_of_results[i]["Vote Data"]["Donald Trump"]["Number of Votes"])
    t_total += trump
    sanders = int(list_of_results[i]["Vote Data"]["Bernie Sanders"]["Number of Votes"])
    b_total += sanders

print("trump's total: " + str(t_total))
print("bernie's total: " + str(b_total))
