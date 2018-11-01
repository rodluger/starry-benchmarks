import starry
import starry.maps
import numpy as np


class TimeSuite:
    """
    Timing suite for `starry` I/O operations.

    """
    def setup(self):
        self.map2_1 = starry.Map(2)
        self.map2_10 = starry.Map(2, nwav=10)
        self.map10_1 = starry.Map(10)
        self.map10_10 = starry.Map(10, nwav=10)

    def time_instantiate_map2_1(self):
        map = starry.Map(2)

    def time_instantiate_map10_1(self):
        map = starry.Map(10)
    
    def time_instantiate_map2_10(self):
        map = starry.Map(2, nwav=10)

    def time_instantiate_map10_10(self):
        map = starry.Map(10, nwav=10)
    
    def time_assign_one_ylm_map2_1(self):
        self.map2_1[1, 0] = 1
    
    def time_assign_one_ylm_map10_1(self):
        self.map10_1[1, 0] = 1

    def time_assign_one_ylm_map2_10(self):
        self.map2_10[1, 0] = np.ones(10)
    
    def time_assign_one_ylm_map10_10(self):
        self.map10_10[1, 0] = np.ones(10)
    
    def time_assign_all_ylm_map2_1(self):
        self.map2_1[:, :] = np.ones(9)
    
    def time_assign_all_ylm_map10_1(self):
        self.map10_1[:, :] = np.ones(121)

    def time_assign_all_ylm_map2_10(self):
        self.map2_10[:, :] = np.ones((9, 10))
    
    def time_assign_all_ylm_map10_10(self):
        self.map10_10[:, :] = np.ones((121, 10))
    
    def time_assign_one_ul_map2_1(self):
        self.map2_1[1] = 1
    
    def time_assign_one_ul_map10_1(self):
        self.map10_1[1] = 1

    def time_assign_one_ul_map2_10(self):
        self.map2_10[1] = np.ones(10)
    
    def time_assign_one_ul_map10_10(self):
        self.map10_10[1] = np.ones(10)
    
    def time_assign_all_ul_map2_1(self):
        self.map2_1[:] = np.ones(2)
    
    def time_assign_all_ul_map10_1(self):
        self.map10_1[:] = np.ones(10)

    def time_assign_all_ul_map2_10(self):
        self.map2_10[:] = np.ones((2, 10))
    
    def time_assign_all_ul_map10_10(self):
        self.map10_10[:] = np.ones((10, 10))
    
    def time_load_image_map2_1(self):
        self.map2_1.load_image("earth")
    
    def time_load_image_map10_1(self):
        self.map10_1.load_image("earth")
    
    def time_load_image_map2_10(self):
        self.map2_10.load_image("earth")
    
    def time_load_image_map10_10(self):
        self.map10_10.load_image("earth")