import numpy as np

class DistanceCalculator:
    def __init__(self):
        pass

    def euclidean_distance(self, point1, point2):
        sub_points = point1[0]- point2[0], point1[1]- point2[1]
        square_points = sub_points ** 2
        sum_points = sum(square_points)
        squareroot_points = np.sqrt(sum_points)

        return squareroot_points
    
    def manhattan_Distance (self, point1, point2):
        sub_points = point1[0]- point2[0], point1[1]- point2[1]
        abs_value = (abs(sub_points[0]), sub_points[1])
        sum_points = sum(abs_value)

        return sum_points

 