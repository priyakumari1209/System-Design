# solution.py — Amazon Locker

from enum import Enum
from threading import Lock
import random
import string

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Package:
    def __init__(self, id, size, customer_id):
        self.id = id
        self.size = size
        self.customer_id = customer_id

class Locker:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.package = None

    def is_available(self):
        return self.package is None

    def assign_package(self, package):
        self.package = package

    def release_package(self):
        pkg = self.package
        self.package = None
        return pkg

class LockerStation:
    def __init__(self, id, lockers):
        self.id = id
        self.lockers = lockers
        self.reservations = {}   # pickupCode -> lockerId
        self.lock = Lock()

    def deposit_package(self, package):
        with self.lock:
            locker = self._find_available_locker(package.size)
            if not locker:
                raise Exception("No locker available")
            locker.assign_package(package)
            code = self._generate_code()
            self.reservations[code] = locker.id
            return code

    def pickup_package(self, code):
        with self.lock:
            if code not in self.reservations:
                raise Exception("Invalid code")
            locker_id = self.reservations.pop(code)
            locker = next(l for l in self.lockers if l.id == locker_id)
            return locker.release_package()

    def _find_available_locker(self, package_size):
        # find smallest available locker that fits
        fit = [l for l in self.lockers
               if l.is_available() and l.size.value >= package_size.value]
        fit.sort(key=lambda l: l.size.value)
        return fit[0] if fit else None

    def _generate_code(self):
        return ''.join(random.choices(string.digits, k=6))