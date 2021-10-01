from collections import defaultdict
from math import inf
import random
import csv
from cs506 import sim

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    return [sum(point[j] for point in points) / len(points) for j in range(len(points[0]))]

def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = max(assignments) + 1
    clusters = [[ex for i, ex in enumerate(dataset) if assignments[i] == l] for l in range(k)]
    return [point_avg(cluster) for cluster in clusters]

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return sim.euclidean_dist(a, b)

def distance_squared(a, b):
    return distance(a, b) ** 2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    indices = list(range(len(dataset)))
    random.shuffle(indices)
    return [dataset[i] for i in indices[:k]]

def cost_function(clustering):
    centers = {j: point_avg(clustering[j]) for j in clustering.keys()}
    return sum(sum(distance_squared(x_i, centers[j]) for x_i in clustering[j]) for j in clustering.keys())

def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centroids = [dataset[random.randint(0, len(dataset) - 1)]]
    for cid in range(1, k):
        distances = [find_min_dist(point, centroids) for point in dataset]
        max_dist = max(distances)
        max_ind = distances.index(max_dist)
        centroids.append(dataset[max_ind])
    return centroids

def find_min_dist(point, centroids):
    return min(distance(point, centroid) for centroid in centroids)

def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
