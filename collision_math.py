import numpy as np
from math import sqrt


def circle_triangle_collision(circle_center, circle_radius, triangle):
    """
    Determine if a circle and triangle are colliding.

    Parameters:
    circle_center -- (x, y) coordinates of circle center
    circle_radius -- radius of the circle
    triangle -- list of 3 points [(x1, y1), (x2, y2), (x3, y3)]

    Returns:
    True if colliding, False otherwise
    """
    # Find the closest point on the triangle to the circle center
    closest_point = closest_point_on_triangle(circle_center, triangle)

    # Calculate distance between circle center and closest point
    distance = distance_between(circle_center, closest_point)

    # Collision occurs if this distance is less than the radius
    return distance <= circle_radius


def distance_between(point1, point2):
    """Calculate Euclidean distance between two points"""
    return sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def closest_point_on_triangle(point, triangle):
    """Find the closest point on a triangle to a given point"""
    # Check if point is inside the triangle
    if is_point_in_triangle(point, triangle):
        return point  # The point itself is the closest

    # Check each edge of the triangle
    edges = [
        (triangle[0], triangle[1]),
        (triangle[1], triangle[2]),
        (triangle[2], triangle[0]),
    ]

    closest_point = None
    min_distance = float("inf")

    for edge_start, edge_end in edges:
        # Find closest point on this edge
        edge_closest = closest_point_on_line_segment(point, edge_start, edge_end)

        # Calculate distance to this edge
        dist = distance_between(point, edge_closest)

        # Update if this is the closest so far
        if dist < min_distance:
            min_distance = dist
            closest_point = edge_closest

    return closest_point


def closest_point_on_line_segment(point, line_start, line_end):
    """Find the closest point on a line segment to a given point"""
    # Convert to numpy arrays for vector operations
    point = np.array(point)
    line_start = np.array(line_start)
    line_end = np.array(line_end)

    # Vector from line_start to line_end
    line_vec = line_end - line_start

    # Length of line segment squared
    line_len_sq = np.sum(line_vec**2)

    # If line segment is just a point, return line_start
    if line_len_sq == 0:
        return tuple(line_start)

    # Calculate projection of point onto line segment
    point_vec = point - line_start
    t = max(0, min(1, np.dot(point_vec, line_vec) / line_len_sq))

    # Get the closest point
    closest = line_start + t * line_vec

    return tuple(closest)


def is_point_in_triangle(point, triangle):
    """Check if a point is inside a triangle using barycentric coordinates"""
    x, y = point
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]

    # Compute vectors
    v0x, v0y = x3 - x1, y3 - y1
    v1x, v1y = x2 - x1, y2 - y1
    v2x, v2y = x - x1, y - y1

    # Compute dot products
    dot00 = v0x * v0x + v0y * v0y
    dot01 = v0x * v1x + v0y * v1y
    dot02 = v0x * v2x + v0y * v2y
    dot11 = v1x * v1x + v1y * v1y
    dot12 = v1x * v2x + v1y * v2y

    # Compute barycentric coordinates
    inv_denom = 1.0 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    # Check if point is in triangle
    return (u >= 0) and (v >= 0) and (u + v <= 1)
