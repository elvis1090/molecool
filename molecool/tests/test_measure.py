'''
Tests for the measure module
'''
# import
import numpy as np
import pytest

import molecool

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

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(rA,rB,rC,degrees=True)

    # test: compare expected result and calculated result (from your code)

    assert pytest.approx(expected_angle) == calculated_angle
