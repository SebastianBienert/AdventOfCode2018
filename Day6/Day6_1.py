import numpy
import sys

lines = open("day6.txt", "r").readlines()
points = { index+1 : ( int(line.split(',')[0].strip()), int(line.split(',')[1].strip()) ) for (index,line) in enumerate(lines) }

def is_infinite(source, points):
        finiteRight = False
        finiteLeft = False
        finiteTop = False
        finiteBottom = False
        for index, cords in points.items():
                delta_y = source[1] - cords[1]
                delta_x = source[0] - cords[0]
                #IF PROCESSED POINT IS TO THE RIGHT AND CORDS COVERS IT:
                if delta_x < 0 and abs(delta_x) >= abs(delta_y):
                        finiteRight = True
                #IF PROCESSED POINT IS TO THE LEFT AND CORDS COVERS IT:
                if delta_x > 0 and abs(delta_x) >= abs(delta_y):
                        finiteLeft = True
                #IF PROCESSED POINT IS TO THE TOP AND CORDS COVERS IT:
                if delta_y < 0 and abs(delta_y) >= abs(delta_x):
                        finiteTop = True
                if delta_y > 0 and abs(delta_y) >= abs(delta_x):
                        finiteBottom = True
        return not (finiteRight and finiteLeft and finiteTop and finiteBottom)


def manhattan_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

def init_plane(plane, points):
        for point in points:
                plane[points[point][1], points[point][0]] = point
        for x in range(0, plane.shape[0]):
                for y in range(0, plane.shape[1]):
                        plane[x,y] = get_nearest_point((y,x), points)

def get_plane_results(plane): 
        unique, counts = numpy.unique(plane, return_counts=True)
        return dict(zip(unique, counts))

def get_minimum_value(dic):
        result = sys.maxsize
        result_index = 0
        repeated = 0
        for item in dic:
                if dic[item] < result:
                        result = dic[item]
                        repeated = 0
                        result_index = item
                elif dic[item] == result:
                        repeated += 1
        return result_index, repeated

def get_nearest_point(source, points):
        dic = {pointKey : manhattan_distance(source, points[pointKey]) for pointKey in points}
        minValue, repeated = get_minimum_value(dic)
        if repeated > 0:
                return 0
        return minValue

def remove_elements_from_dic(dic, list_to_remove):
        for item in list_to_remove:
                del dic[item]

maxY = points[int(max(points, key=lambda k: points[k][1]))][1]
maxX = points[int(max(points, key=lambda k: points[k][0]))][0]
plane = numpy.zeros((maxY + 1, maxX + 1), dtype=numpy.int8)
init_plane(plane, points)
infinite_points = [index for index, point in points.items() if is_infinite(point, points)]
result = get_plane_results(plane)
remove_elements_from_dic(result,infinite_points)

print("RESULT: {0}".format(result[max(result, key= lambda k: result[k])]))
