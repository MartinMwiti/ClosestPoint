# A divide and conquer program in Python3 
# to find the smallest distance from a 
# given set of points. 
import math 
import copy 
from ast import literal_eval




# A utility function to find the 
# distance between the closest points of 
# strip of given size. All points in 
# strip[] are sorted accordint to 
# y coordinate. They all have an upper 
# bound on minimum distance as d. 
# Note that this method seems to be 
# a O(n^2) method, but it's a O(n) 
# method as the inner loop runs at most 6 times 
def stripClosest(strip, size, d): 
	
	# Initialize the minimum distance as d 
	min_val = d 

	
	# Pick all points one by one and 
	# try the next points till the difference 
	# between y coordinates is smaller than d. 
	# This is a proven fact that this loop 
	# runs at most 6 times 
	for i in range(size): 
		j = i + 1
		while j < size and (strip[j].y -
							strip[i].y) < min_val: 
			min_val = dist(strip[i], strip[j]) 
			j += 1

	return min_val 


# A class to represent a Point in 2D plane 
class Point(): 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 
  
  
# Driver code 
# P = [Point(2, 3), Point(12, 30), 
# 	Point(40, 50), Point(5, 1), 
# 	Point(12, 10), Point(3, 4)] 
# n = len(P) 

# print("The smallest distance is", 
# 				closest(P, n)) # 1.4142135623730951

def getClosestDistance(s):
    P = [Point(*x) for x in literal_eval(s)]
    n = len(P) 
    return closest(P, n)

# s = "(2,3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)"
# print(getClosestDistance(s))


# The main function that finds 
# the smallest distance. 
# This method mainly uses closestUtil() 
def closest(P, n): 
	P.sort(key = lambda point: point.x) # object sorted by x coordinate
	Q = copy.deepcopy(P) # to avoid override 
	Q.sort(key = lambda point: point.y)	# object sorted by y coordinate

	# Use recursive function closestUtil() 
	# to find the smallest distance 
	return closestUtil(P, Q, n) 



# A recursive function to find the 
# smallest distance. The array P contains 
# all points sorted according to x coordinate 
def closestUtil(P, Q, n): 
	
	# If there are 2 or 3 points, 
	# then use brute force 
	if n <= 3: 
		return bruteForce(P, n) # pythagoras theorem

	# Find the middle point 
	mid = n // 2
	midPoint = P[mid] 

	# Consider the vertical line passing 
	# through the middle point calculate 
	# the smallest distance dl on left 
	# of middle point and dr on right side 
	dl = closestUtil(P[:mid], Q, mid) 
	dr = closestUtil(P[mid:], Q, n - mid) 

	# Find the smaller of two distances 
	d = min(dl, dr) 

	# Build an array strip[] that contains 
	# points close (closer than d) 
	# to the line passing through the middle point 
	strip = [] 
	for i in range(n): 
		if abs(Q[i].x - midPoint.x) < d: 
			strip.append(Q[i]) 

	# Find the closest points in strip. 
	# Return the minimum of d and closest 
	# distance is strip[] 
	return min(d, stripClosest(strip, len(strip), d)) 


# A utility function to find the 
# distance between two points 
def dist(p1, p2): 
	return math.sqrt((p1.x - p2.x) *
					(p1.x - p2.x) +
					(p1.y - p2.y) *
					(p1.y - p2.y)) 

# A Brute Force method to return the 
# smallest distance between two points 
# in P[] of size n 
def bruteForce(P, n): 
	min_val = float('inf') 
	for i in range(n): 
		for j in range(i + 1, n): # next value
			if dist(P[i], P[j]) < min_val: 
				min_val = dist(P[i], P[j]) 

	return min_val 