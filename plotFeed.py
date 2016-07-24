import json
import matplotlib.pyplot as plt
import getFeed as gf
import numpy as np

loc = []
for i in range(0, gf.test.__len__()):
	a = json.loads(gf.test[i]).get("user").get("time_zone")
	loc.append(a.__str__())

unique = set(loc)
uniqueList = list(unique)

locDict = {}

for i in range(0, uniqueList.__len__()):
	locDict[uniqueList[i]] = loc.count(uniqueList[i])

X = np.arange(len(locDict))
plt.bar(X, locDict.values(), align='center', width=0.5)
plt.xticks(X, locDict.keys())
ymax = max(locDict.values()) + 1
plt.ylim(0, ymax)
plt.show()