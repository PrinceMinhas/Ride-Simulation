from driver import Driver
from location import Location
from rider import Rider, WAITING


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        self._waiting_riders = []
        self._available_drivers = []

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str

        >>> dispatcher1 = Dispatcher()
        >>> dispatcher1.request_rider(Driver("Bob", \
        Location(1, 1), 1))
        >>> print(dispatcher1)
        Dispatcher
        Riders Waiting: []
        Drivers Waiting: [Bob]
        """
        dispatcher = "Dispatcher\n"
        dispatcher += "Riders Waiting: ["
        for riders in self._waiting_riders:
            dispatcher += str(riders) + ", "
        if dispatcher[-1] == "[":
            dispatcher += "]\n"
        else:
            dispatcher = dispatcher[0:-2] + "]\n"

        dispatcher += "Drivers Waiting: ["
        for drivers in self._available_drivers:
            dispatcher += str(drivers) + ", "
        if dispatcher[-1] == "[":
            dispatcher += "]"
        else:
            dispatcher = dispatcher[0:-2] + "]"
        return dispatcher

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None

        >>> dispatcher1 = Dispatcher()
        >>> driver1 = Driver("Bob", Location(2 ,3), 1)
        >>> rider1 = Rider("Jim", Location(1, 1), Location(2, 3),\
            WAITING, 1)
        >>> dispatcher1.request_rider(driver1)
        >>> print(dispatcher1.request_driver(rider1))
        Bob
        """
        driver = None
        if len(self._available_drivers) == 0:
            rider.status = WAITING
            self._waiting_riders.append(rider)
            return driver
        else:
            for i in range(len(self._available_drivers)):
                if (driver is None and
                        self._available_drivers[i].is_idle):
                    driver = self._available_drivers[i]
                elif (driver is not None and
                      self._available_drivers[i].is_idle and
                      self._available_drivers[i].get_travel_time(
                              rider.origin) < driver.get_travel_time(
                                      rider.origin)):
                    driver = self._available_drivers[i]
        return driver

    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None

        >>> dispatcher1 = Dispatcher()
        >>> driver1 = Driver("Sally", Location(2 ,3), 1)
        >>> rider1 = Rider("Joe", Location(1, 1), Location(2, 3),\
            WAITING, 1)
        >>> dispatcher1.request_driver(rider1)
        >>> print(dispatcher1.request_rider(driver1))
        Joe
        """
        rider = None
        done = False
        if driver not in self._available_drivers:
            self._available_drivers.append(driver)
        if len(self._waiting_riders) != 0:
            for i in range(len(self._waiting_riders)):
                if (self._waiting_riders[i].status == WAITING and
                        not done):
                    rider = self._waiting_riders[i]
                    done = True
        return rider

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        index = 0
        found = False
        while index < len(self._waiting_riders) and not found:
            if self._waiting_riders[index].id == rider.id:
                found = True
            else:
                index += 1
        if found:
            del self._waiting_riders[index]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
