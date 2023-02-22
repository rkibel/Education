import numpy as np

people, connections, days = (int(i) for i in input().strip().split())
peopleToIndices = dict()
peopleToSkept = list()
edges = [list() for i in range(people)]
for i in range(people):
    person, skepticism = input().strip().split()
    peopleToIndices[person] = i
    peopleToSkept.append(int(skepticism))
for i in range(connections):
    person1, person2 = input().strip().split()
    edges[peopleToIndices[person1]].append(peopleToIndices[person2])
    edges[peopleToIndices[person2]].append(peopleToIndices[person1])
origin = peopleToIndices[input()]

# which people broadcast the rumor
rumorers = [False for i in range(people)]
rumorers[origin] = True

# which people recently heard the rumor
newbies = set()
newbies.add(origin)

# current running amount of skepticism
currSkept = [0 for i in range(people)]
currSkept[origin] = 1

for i in range(days):
    newerbies = set()
    for _, newbie in enumerate(newbies):
        rumorers[newbie] = True
        for _, k in enumerate(edges[newbie]):
            if rumorers[k]: continue
            currSkept[k] += 1
            if currSkept[k] >= peopleToSkept[k]:
                newerbies.add(k)
    newbies = newerbies

print(np.count_nonzero(currSkept) - 1)