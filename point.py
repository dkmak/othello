#Project 5. Darryl Mak #50693792
#this Point Class is taken directly from Lecture on Tuesday, March 1-3, 2016

# point.py(ICS 32 Winter 2016, Code Example)



import math



class Point:
    def __init__(self, frac_x: float, frac_y: float):
        '''
        Initializes a Point object, given its fractional coordinates.
        '''
        self._frac_x = frac_x
        self._frac_y = frac_y


    def frac(self) -> (float, float):
        '''
        Returns an (x, y) tuple that contains fractional coordinates
        for this Point object.
        '''
        return (self._frac_x, self._frac_y)


    def pixel(self, width: float, height: float) -> (float, float):
        '''
        Returns an (x, y) tuple that contains pixel coordinates for
        this Point object.  The total_size parameter specifies the
        total size, in pixels, of the area in which the point needs
        to be specified -- this is used to make the appropriate
        conversion, since the pixel position of a fractional point
        changes as the size changes.
        '''
        return (int(self._frac_x * width), int(self._frac_y * height))


    def frac_distance_from(self, p: 'Point') -> float:
        '''
        Given another Point object, returns the distance, in
        terms of fractional coordinates, between this Point and the
        other Point.
        '''

        # Per the Pythagorean theorem from mathematics, the distance
        # between two points is the square root of the sum of the
        # squares of the differences in the x- and y-coordinates.
        return math.sqrt(
            (self._frac_x - p._frac_x) * (self._frac_x - p._frac_x)
            + (self._frac_y - p._frac_y) * (self._frac_y - p._frac_y))

        # Note, too, that there's a function in the Python standard
        # library, math.hypot, that does exactly this calculation.



def from_frac(frac_x: float, frac_y: float) -> Point:
    '''Builds a Point given fractional x and y coordinates.'''
    return Point(frac_x, frac_y)



def from_pixel(pixel_x: float, pixel_y: float, width: float, height: float) -> Point:
    '''
    Builds a Point given pixel x and y coordinates, along with
    the width and height of the area (necessary for conversion
    to fractional).
    '''
    return Point(pixel_x / width, pixel_y / height)
