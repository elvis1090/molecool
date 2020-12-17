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


