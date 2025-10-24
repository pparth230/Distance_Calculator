import numpy as np

class DistanceCalculator:
    def __init__(self):
        pass

    def euclidean_distance(self, point1, point2):
        sub_points = point1[0]- point2[0], point1[1]- point2[1]
        square_points = (sub_points[0]**2, sub_points[1]**2)
        sum_points = sum(square_points)
        squareroot_points = np.sqrt(sum_points)

        return squareroot_points
    
    def Manhattan_Distance (self, point1, point2):
        sub_points = point1[0]- point2[0], point1[1]- point2[1]
        abs_value = (abs(sub_points[0]), sub_points[1])
        sum_points = sum(abs_value)

        return sum_points
    
    def Cosine_function (self, vec1, vec2):
        dot_product = vec1[0]*vec2[0] + vec1[1]*vec2[1]
        Magnitude_vec1 = np.sqrt(vec1[0]**2 + vec1[1]**2)
        Magnitude_vec2 = np.sqrt(vec2[0]**2 + vec2[1]**2)
        similiarities = dot_product/(Magnitude_vec1 * Magnitude_vec2)

        return similiarities
    
    def find_K_nearest(self, data, query_point, k, metric = 'euclidean'):
        distances= []
        for point in data:
            if metric == 'euclidean':
                distance = self.euclidean_distance(point, query_point)
            elif metric == 'Manhattan':
                distance = self.Manhattan_Distance(point, query_point)
            elif metric == 'cosine':
                distance = self.Cosine_function(point, query_point)
            
            distances.append((distance, point))
        
        distances.sort()
        nearest = distances [:k]
            

        return [point for distance, point in nearest]
    


calc = DistanceCalculator()
data = [[1,2], [3,4], [5,6], [7,8]]
query = [2,3]
neighbors = calc.find_K_nearest(data, query, k=1)
print(neighbors)
        
    


 