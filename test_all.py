from unittest import TestCase
import numpy as np
from tropical_lib import mut_mul, power


class TestAll(TestCase):
    def setUp(self) -> None:
        self.a = np.array([[157, 308, 112, 850,  77],
                        [228, 984, 240, 773, 953],
                        [215, 777, 562, 662, 445],
                        [542, 466, 834,  89, 123],
                        [171, 361, 432, 395, 522]])
        self.b = np.array([[959, 872, 237, 573, 337],
                           [ 56, 758, 875, 231, 136],
                           [ 70, 791, 816, 964, 737],
                           [169, 121, 915, 891, 355],
                           [798,   1, 685, 668, 672]])
        self.ab = np.array([[182, 78, 394, 539, 444],
                            [310, 894, 465, 801, 565],
                            [632, 446, 452, 788, 552],
                            [258, 124, 779, 697, 444],
                            [417, 516, 408, 592, 497]])
        self.ba = np.array([[452, 698, 769, 662, 682],
                            [213, 364, 168, 320, 133],
                            [227, 378, 182, 920, 147],
                            [326, 477, 281, 750, 246],
                            [229, 985, 241, 757, 791]])
        self.a3 = np.array([[405, 556, 360, 561, 325],
                         [476, 666, 497, 700, 462],
                         [463, 653, 484, 687, 449],
                         [383, 573, 406, 267, 301],
                         [419, 609, 440, 573, 405]])
        self.b7 = np.array([[668, 869, 1025, 843, 748],
                         [467, 668, 824, 642, 547],
                         [858, 682, 838, 1033, 938],
                         [686, 532, 688, 861, 766],
                         [588, 412, 568, 763, 668]])

    def test_mut_mul(self):
        self.assertTrue(np.array_equal(mut_mul(self.a, self.b), self.ab))
        self.assertTrue(np.array_equal(mut_mul(self.b, self.a), self.ba))

    def test_power(self):
        self.assertTrue(np.array_equal(power(self.a, 3), self.a3))
        self.assertTrue(np.array_equal(power(self.b, 7), self.b7))

