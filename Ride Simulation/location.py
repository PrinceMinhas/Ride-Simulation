class Location:

    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        self.row = row
        self.column = column

    def __str__(self):
        """Return a string representation.

        @type self: Location
        @rtype: str

        >>> location1 = Location (1,2)
        >>> str(location1)
        (1, 2)
        """
        return "({}, {})".format(self.row, self.column)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Location
        @rtype: bool

        >>> location1 = Location (1,2)
        >>> location2 = Location (4,5)
        >>> location3 = Location (1,2)
        >>> location1 == location2
        False
        >>> location1 == location3
        True
        """
        return self.row == other.row and self.column == other.column


def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int

    >>> origin = Location (0,0)
    >>> destination = Location (5,11)
    >>> print (manhattan_distance(origin, destination))
    16
    """
    return (int(abs(destination.row - origin.row) +
            abs(destination.column - origin.column)))


def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location

    >>> location_str = "2,16"
    >>> print (deserialize_location(location_str))
    (2, 16)
    """
    location = location_str.split(',')
    return Location(int(location[0]), int(location[-1]))
