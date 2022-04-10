#c. Create one or more Python scripts in each subfolder, at each level.
# Each script should have a unique function (you may reuse previously-created functions and/or create new functions).
# Be sure to name the scripts aptly.

def freqMap(values):
    map={}
    for v in values:
        if not map.get(v):
             map[v]=1
        else:
             map[v]+=1
    return map