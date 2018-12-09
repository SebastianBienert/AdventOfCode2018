data = open('day8.txt', "r").readline().split()
data = [int(x) for x in data]

def node_length(data):
    if int(data[0]) == 0:
        node_len = data[1] + 2
        value = sum(data[2:node_len])
        return node_len, value
    else:
        node_len = 0
        child_values = []
        for x in range(0, int(data[0])):
            child_len, child_val = node_length(data[node_len + 2:])
            child_values.append(child_val)
            node_len += child_len

        ret_val = 0
        for meta in data[node_len + 2 : node_len + 2 + data[1]]:
            if meta >= 1 and meta < len(child_values) + 1:
                ret_val += child_values[meta - 1]
        return node_len + 2 + int(data[1]), ret_val

length, result = node_length(data)
print("RESULT: ", result)

