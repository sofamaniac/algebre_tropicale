from unittest import TestCase
import numpy as np
from tropical_lib import matrix_multiplication, power


class TestAll(TestCase):
    def setUp(self) -> None:
        inf = infinity = np.float("inf")
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

        self.c = np.array([[633, 728, 423, 538, 404, 704, 349, 790, 436,  39],
                               [787, 298, 218, 477, 684, 434,  93, 246, 807, 535],
                               [976, 283, 827, 994, 784, 225, 238, 479, 943, 536],
                               [800, 538,  63, 158, 771, 399, 915, 321, 568, 507],
                               [767,  87, 830, 831, 370, 700, 385, 339, 404, 293]])
        self.d = np.array([[151, 888, 225, 600, 972],
              [194, 310, 355, 720, 942],
              [695, 590, 764, 291, 207],
              [268, 616, 236, 883, 149],
              [877, 177, 127,  67, 884],
              [149, 278, 143,  53, 492],
              [641, 898, 712, 881, 580],
              [118, 765, 349,   9, 959],
              [399,   2, 597, 943,  98],
              [976, 826, 144, 457,  54]])

        self.cd = np.array([[784, 438, 183, 471, 93],
                            [364, 608, 577, 255, 425],
                            [374, 503, 368, 278, 590],
                            [426, 570, 394, 330, 270],
                            [281, 397, 437, 348, 347]])

        self.dc = np.array([[784, 508, 574, 689, 555, 450, 463, 704, 587, 190],
                            [827, 608, 528, 732, 598, 580, 403, 556, 630, 233],
                            [974, 294, 354, 449, 577, 690, 592, 546, 611, 500],
                            [901, 236, 691, 806, 519, 461, 474, 488, 553, 307],
                            [867, 410, 130, 225, 838, 352, 270, 388, 635, 574],
                            [782, 426, 116, 211, 553, 368, 371, 374, 585, 188],
                            [1274, 667, 944, 1039, 950, 937, 950, 919, 984, 680],
                            [751, 547, 72, 167, 522, 408, 467, 330, 554, 157],
                            [789, 185, 220, 479, 468, 436, 95, 248, 502, 391],
                            [821, 141, 520, 615, 424, 369, 382, 393, 458, 347]])

        self.e = np.array([[750, 767, 995, 886, 218],
                             [604, 393, 903, 522, 638],
                             [ 32, 530, 817, 869, 827]])

        self.ec = np.array([[985, 305, 949, 1044, 588, 918, 603, 557, 622, 511],
                         [1180, 691, 585, 680, 1008, 827, 486, 639, 1040, 643],
                         [665, 760, 455, 570, 436, 736, 381, 776, 468, 71]])

        self.f = np.array([[  0., -inf, -inf,  -7.,  -7.],
                            [ -5.,  -1.,  -4.,   4., -inf],
                            [ -2., -inf,   2., -inf,  -7.],
                            [ -6.,  -3.,   5.,  -7.,   0.],
                            [  5., -inf,  -2.,   2.,   4.]])
        self.g = np.array([[ -7.,   5.,  -5.,   3.,   6.],
                            [-inf, -inf, -inf,   3., -inf],
                            [ -4.,  -6.,   7., -inf, -inf],
                            [  3., -inf,   6.,  -6.,   6.],
                            [-inf,   4.,  -7., -inf,  -6.]])
        self.fg = np.array([[-infinity, -infinity, -infinity, -infinity, -infinity],
                           [-infinity, -infinity, -infinity, -infinity, -infinity],
                           [-infinity, -infinity, -infinity, -infinity, -infinity],
                           [-infinity, -infinity, -infinity, -infinity, -infinity],
                           [-infinity, -infinity, -infinity, -infinity, -infinity]])

        self.gf = np.array([[-7., -infinity, -infinity, -infinity, -infinity],
                            [-infinity, -infinity, -infinity, -infinity, -infinity],
                            [-infinity, -infinity, -infinity, -infinity, -infinity],
                            [-infinity, -infinity, -infinity, -infinity, -infinity],
                            [-infinity, -infinity, -infinity, -infinity, -infinity]])

    def test_mut_mul(self):
        self.assertTrue(np.array_equal(matrix_multiplication(self.a, self.b), self.ab))
        self.assertTrue(np.array_equal(matrix_multiplication(self.b, self.a), self.ba))
        self.assertTrue(np.array_equal(matrix_multiplication(self.c, self.d), self.cd))
        self.assertTrue(np.array_equal(matrix_multiplication(self.d, self.c), self.dc))
        self.assertTrue(np.array_equal(matrix_multiplication(self.e, self.c), self.ec))

        self.assertTrue(np.array_equal(matrix_multiplication(self.f, self.g), self.fg))
        self.assertTrue(np.array_equal(matrix_multiplication(self.g, self.f), self.gf))

    def test_power(self):
        self.assertTrue(np.array_equal(power(self.a, 3), self.a3))
        self.assertTrue(np.array_equal(power(self.b, 7), self.b7))
