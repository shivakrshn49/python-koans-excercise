#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

def triangle_check(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        raise TriangleError('Triangle must have positive sides or values')
    else:
        pass  
    if a + b <= c or a + c <= b or b + c <= a:
        raise TriangleError("The values provided doesn't make a triangle")       

def triangle(a, b, c):
    if a==b==c:
    	return 'equilateral'
    elif a==b or a==c or b==c:
    	return 'isosceles'
    elif a!=b!=c:
    	return 'scalene'



# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
