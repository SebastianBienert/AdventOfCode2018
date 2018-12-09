tuples = [(line.split()[1], line.split()[7]) for line in open("d:\\AoC2018\\Day7\\day7.txt", "r").readlines()]

reversed_dic = dict()
dic = dict()
childs = set()
parents = set()


def get_next_node(available, reversed_dic, current_result):
    real_processed = set(current_result)
    real_available = set([x for x in available if x == start or real_processed.issuperset(set(reversed_dic[x]))])
    if len(real_available) == 0:
        return None
    mini = min(real_available, key= lambda k : k)
    return mini

def get_available_len(available, reversed_dic, current_result):
    real_processed = set(current_result)
    real_available = set([x for x in available if x == start or real_processed.issuperset(set(reversed_dic[x]))])
    return len(real_available)


for parent, child in tuples:
    parents.add(parent)
    childs.add(child)
    if parent in dic:
        dic[parent].append(child)
    else:
        dic[parent] = [child]
    if child in reversed_dic:
        reversed_dic[child].append(parent)
    else:
        reversed_dic[child] = [parent]


# for parent, child in tuples:
#     if child in reversed_dic:
#         reversed_dic[child].append(parent)
#     else:
#         reversed_dic[child] = [parent]

allLetters = set(childs.union(parents))
start = min(allLetters.difference(childs))
for starter in allLetters.difference(childs):
    reversed_dic[starter] = []

end = allLetters.difference(parents).pop()
for end in allLetters.difference(parents):
    dic[end] = []

current = start
result = ""
available = set(allLetters.difference(childs))
processed = set()


result_sum = 0
options = 0

workers_num = 5
workers = []
for x in range(0, workers_num):
    workers.append((False, -1, None))


def assign_work_to_worker(workers, processed, current_result):
    node = get_next_node([x for x in available if x not in current_result and x not in processed], reversed_dic, current_result)
    available_workers = [(index, w) for index, w in enumerate(workers) if w[0] == False]

    if node != None and len(available_workers) > 0:
        processed.add(node)
        workers[available_workers[0][0]] = (True, ord(node) - 4, node)


while len(result) < len(allLetters):
    options = get_available_len([x for x in available if x not in result and x not in processed], reversed_dic, result)

    for x in range(0, options):
        assign_work_to_worker(workers, processed, result)
     
    for index, worker in enumerate(workers):
        workers[index] = (worker[0], worker[1] - 1, worker[2])
        if workers[index][1] == 0 and workers[index][0] == True:
            result += worker[2]
            available.update(dic[worker[2]])
            workers[index] = (False, -1, None)

    result_sum += 1

print(result_sum)