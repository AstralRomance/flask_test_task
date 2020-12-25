import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, connected_components

class Distance:
    def __init__(self):
        self.weight_matrix = np.load(open('matrix_distance', 'rb'))
        self.dist, self.predecessors = shortest_path(method='D',csgraph=self.weight_matrix, directed=False, return_predecessors=True)

    def length_find(self, path_start: int, path_finish: int) -> dict:
        response_info = {}
        response_info['path'] = self.find_path(path_start, path_finish)
        response_info['distance'] = int(self.dist[path_start, path_finish])
        return response_info

    def find_path(self, path_start: int, path_finish: int) -> list:
        path = [path_finish]
        temp = path_finish
        while self.predecessors[path_start, temp] != -9999:
            path.append(int(self.predecessors[path_start, temp]))
            temp = self.predecessors[path_start, temp]
        return path[::-1]
