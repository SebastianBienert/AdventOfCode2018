lines = open("day7.txt", "r").readlines()
tuples = [(line.split()[1], line.split()[7]) for line in lines]

dic = dict()
childs = set()
parents = set()

def mark_as_available(l, dic):
    for item in l:
        dic[l] = True

def get_next_node(current, available, reversed_dic):
    # print(available)
    real_available = set([x for x in available if x == start or processed.issuperset(set(reversed_dic[x]))])
    print("REAL_AVAIL: {0}".format(real_available))
    mini = min(real_available, key= lambda k : k)
    # print(mini)
    return mini


for parent, child in tuples:
    parents.add(parent)
    childs.add(child)
    if parent in dic:
        dic[parent].append(child)
    else:
        dic[parent] = [child]

reversed_dic = dict()
for parent, child in tuples:
    if child in reversed_dic:
        reversed_dic[child].append(parent)
    else:
        reversed_dic[child] = [parent]

allLetters = set(childs.union(parents))
start = min(allLetters.difference(childs))



for starter in allLetters.difference(childs):
    reversed_dic[starter] = []

end = allLetters.difference(parents).pop()
# print("end: ", end)
print("DIC: ", dic)
print("REVERSED DIC: ", reversed_dic)

current = start
result = ""
available = set(allLetters.difference(childs))
processed = set()
while current != end:
    result += current
    print(result)
    processed.add(current)
    available.update(dic[current])
    # print("PROCESSED: {0} REVERSED_SET: {1}".format(processed, set(reversed_dic[current])))
    current = get_next_node(current, [x for x in available if x not in processed], reversed_dic)

result += end

print(dic)
print(result)
