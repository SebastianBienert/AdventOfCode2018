data = open('day8.txt', "r").readline().split()

def node_length(data, metas):
    if int(data[0]) == 0:
        return (int(data[1]) + 2)
    else:
        node_len = 0
        for x in range(0, int(data[0])):
            child_len = node_length(data[node_len + 2:], metas)
            index = node_len + 2 + child_len - int(data[node_len + 3])
            metas.extend(data[index  : node_len + 2 + child_len])
            node_len += child_len
        return node_len + 2 + int(data[1])

metas = []
node_length(data, metas)
metas.extend(data[-int(data[1]):])
print("RESULT: ", sum(map(lambda x : int(x), metas)))


