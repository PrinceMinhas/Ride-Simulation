from location import Location
"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """A rider
    """

    # =====Attributes======
    # @type unique_identifier: str
    #     This is a factor that is used to differentiate riders
    # @type origin: Location
    #     This represents the current location of the rider
    # @type destination: Location
    #     This represents the destination of the rider
    # @type status: str
    #     Whether the rider is "waiting", has "cancelled", or is
    #     "satisfied" (has been picked up)
    # @type patience_attribute: int
    #     The number of minutes a rider is willing to wait for a driver.

    def __init__(self, unique_identifier, origin, destination, status,
                 patience_attribute):
        """Initialize the properties of a Rider

        @type self: Rider
        @type unique_identifier: str
        @type origin: Location
        @type destination: Location
        @type status: str
        @type patience_attribute: int
        @rtype: None
        """
        self.id = unique_identifier
        self.origin = origin
        self.destination = destination
        self.status = status
        self.patience = patience_attribute

    def __str__(self):
        """Return a user-friendly representation of the Rider self

        @type self: Rider
        @rtype: str

        >>> location1 = Location(1, 2)
        >>> destination1 = Location(2, 7)
        >>> rider1 = Rider("Jim", location1, destination1, WAITING,\
        3)
        >>> str(rider1)
        Jim
        """
        return "{}".format(self.id)

    def __eq__(self, other):
        """Return True if and only if Rider self is equivalent to
        Rider other.

        @type self: Rider
        @type other: Rider|Any
        @rtype: bool

        >>> rider1 = Rider("Tom", Location(1,1), Location(2,2), \
        WAITING, 3)
        >>> rider2 = Rider("Sally", Location(5,1), Location(9, 8), \
        WAITING, 3)
        >>> rider3 = Rider("Tom", Location(1,1), Location(2,2), \
        WAITING, 3)
        >>> rider1 == rider2
        False
        >>> rider1 == rider3
        True
        """
        return type(self) == type(other) and self.id == other.id

