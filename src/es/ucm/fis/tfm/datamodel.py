from astropy.coordinates import SkyCoord

from astropy import units as u

class Source:
    def __init__(self, name, ra, dec, error):
        self.name = name
        self.coord = SkyCoord(ra, dec, unit=(u.degree, u.degree))
        self.error = error
