'''
Tests for the measure module
'''
# import
import molecool
import numpy as np

# unit testing function names should start with 'test'
def test_calculate_distance():

    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1,r2)


    # test: compare expected result and calculated result (from your code)

    assert expected_distance == calculated_distance

# unit testing function names should start with 'test'
def test_calculate_angle():

    rA = np.array([0,0,-1])
    rB = np.array([0,0,0])
    rC = np.array([1,0,0])

    expected_angle = np.radians(90)

    calculated_angle = molecool.calculate_angle(rA,rB,rC)


    # test: compare expected result and calculated result (from your code)

    assert expected_angle == calculated_angle
