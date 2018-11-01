import starry
import starry.maps
import numpy as np
npts = 100
lmax_array = [2, 5, 10, 20, 30]
nwav_array = [1, 10]


class TimeIO:
    """
    Timing suite for `starry` I/O operations.

    """
    params = [lmax_array, nwav_array]
    param_names = ["lmax", "nwav"]

    @property
    def one(self):
        if self.map.nwav == 1:
            return 1
        else:
            return np.ones(self.map.nwav)

    def setup(self, lmax, nwav):
        self.map = starry.Map(lmax=lmax, nwav=nwav)
        
    def time_instantiate(self, *args):
        starry.Map(lmax=self.map.lmax, nwav=self.map.nwav)

    def time_assign_one_ylm(self, *args):
        self.map[1, 0] = self.one
     
    def time_assign_all_ylm(self, *args):
        self.map[:, :] = np.squeeze(np.ones((self.map.N, self.map.nwav)))
    
    def time_assign_one_ul(self, *args):
        self.map[1] = self.one
     
    def time_assign_all_ul(self, *args):
        self.map[:] = np.squeeze(np.ones((self.map.lmax, self.map.nwav)))
    
    def time_load_image(self, *args):
        self.map.load_image("earth")

    def time_load_array(self, *args):
        self.map.load_image(np.ones((100, 100)))

    def time_gaussian(self, *args):
        self.map.add_gaussian(sigma=0.1, amp=1, lat=35, lon=50)


class TimeRotate:
    """
    Timing suite for `starry` rotations.

    """
    params = [lmax_array, nwav_array, [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]]
    param_names = ["lmax", "nwav", "axis"]

    @property
    def one(self):
        if self.map.nwav == 1:
            return 1
        else:
            return np.ones(self.map.nwav)

    def setup(self, lmax, nwav, axis):
        self.map = starry.Map(lmax=lmax, nwav=nwav)
        self.map[:, :] = self.one
        self.map.axis = axis

    def time_rotate(self, *args):
        self.map.rotate(17.5)


class TimeEvaluate:
    """
    Timing suite for `starry` map intensity evaluations.

    """
    params = [lmax_array, nwav_array]
    param_names = ["lmax", "nwav"]

    @property
    def one(self):
        if self.map.nwav == 1:
            return 1
        else:
            return np.ones(self.map.nwav)

    def setup(self, lmax, nwav):
        self.map = starry.Map(lmax=lmax, nwav=nwav)
        self.map[:, :] = self.one
        self.map.axis = [0, 1, 0]
        self.x = np.linspace(-1, 1, npts)
        self.y = np.linspace(-1, 1, npts)
        self.theta = np.linspace(0, 360, npts)
        self.theta_const = np.ones(npts) * 17.5

    def time_single(self, *args):
        self.map(x=0.3, y=0.45)
    
    def time_single_with_rotation(self, *args):
        self.map(theta=35, x=0.3, y=0.45)
    
    def time_array(self, *args):
        self.map(x=self.x, y=self.y)
    
    def time_array_with_rotation(self, *args):
        self.map(theta=self.theta, x=self.x, y=self.y)
    
    def time_array_with_rotation_cached(self, *args):
        self.map(theta=self.theta_const, x=self.x, y=self.y)


class TimePhaseCurve:
    """
    Timing suite for `starry` phase curve evaluations.

    """
    params = [lmax_array, nwav_array, [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]]
    param_names = ["lmax", "nwav", "axis"]

    @property
    def one(self):
        if self.map.nwav == 1:
            return 1
        else:
            return np.ones(self.map.nwav)

    def setup(self, lmax, nwav, axis):
        self.map = starry.Map(lmax=lmax, nwav=nwav)
        self.map[:, :] = self.one
        self.map.axis = axis
        self.theta = np.linspace(0, 360, npts)
        self.theta_const = np.ones(npts) * 17.5

    def time_single(self, *args):
        self.map.flux(theta=17.5)
    
    def time_array(self, *args):
        self.map.flux(theta=self.theta)
    
    def time_array_cached(self, *args):
        self.map.flux(theta=self.theta_const)


class TimeOccultation:
    """
    Timing suite for `starry` flux evaluations.

    """
    params = [lmax_array, nwav_array, [0.1, 100], ["y", "u", "both"]]
    param_names = ["lmax", "nwav", "ro", "maptype"]

    @property
    def one(self):
        if self.map.nwav == 1:
            return 1
        else:
            return np.ones(self.map.nwav)

    def setup(self, lmax, nwav, ro, maptype):
        self.map = starry.Map(lmax=lmax, nwav=nwav)
        self.map.axis = [0, 1, 0]
        if maptype == "y":
            self.map[:, :] = self.one
        elif maptype == "u":
            self.map[:] = self.one
        else:
            self.map[:(lmax // 2), :] = np.squeeze(np.ones(((lmax // 2 + 1) ** 2, nwav)))
            self.map[:(lmax // 2)] = np.squeeze(np.ones((lmax // 2, nwav)))
        self.theta = np.linspace(0, 360, npts)
        self.theta_const = np.ones(npts) * 17.5
        self.ro = ro
        self.xo = np.linspace(-1 - self.ro, 1 + self.ro, npts)
        self.yo = np.linspace(-1 - self.ro, 1 + self.ro, npts)

    def time_single(self, *args):
        self.map.flux(xo=0.3, yo=0.45, ro=0.1)
    
    def time_single_with_rotation(self, *args):
        self.map.flux(theta=35, xo=0.3, yo=0.45, ro=0.1)
    
    def time_array(self, *args):
        self.map.flux(xo=self.xo, yo=self.yo, ro=self.ro)
    
    def time_array_with_rotation(self, *args):
        self.map.flux(theta=self.theta, xo=self.xo, yo=self.yo, ro=self.ro)
    
    def time_array_with_rotation_cached(self, *args):
        self.map.flux(theta=self.theta_const, xo=self.xo, yo=self.yo, ro=self.ro)
