"""
"""
import time
import math
import itertools

__author__ = 'Kevin Ballard'


class Agency(object):
  """
  """

  def __init__(self, name, has_direction, mode, routes=None):
    """
    """
    self._name = name
    self._has_direction = has_direction
    self._mode = mode

    self._routes_by_name = {}
    self._routes_by_code = {}
    map(self.add_route, routes)

  #########################################################
  #
  #########################################################

  def GetName(self):
    """
    """
    return self._name

  def HasDirection(self):
    """
    """
    return self._has_direction

  def GetMode(self):
    """
    """
    return self._mode

  #########################################################
  #
  #########################################################

  def AddRoute(self, route):
    """
    """
    self._routes_by_name[route.name] = route
    self._routes_by_code[route.code] = route

  def GetAllRoutes(self):
    """
    """
    return self._routes_by_name.values()

  def GetRouteByName(self, route_name):
    """
    """
    return self._routes_by_name.get(route_name)

  def GetRouteByCode(self, route_code):
    """
    """
    return self._routes_by_code.get(route_code)


class Route(object):
  """
  """
  pass







class Stop(object):
  """
  """

  def __init__(self, name, code, departures=None):
    """
    """
    self._name = name
    self._code = code




class Departures(object):
  """
  """

  def __init__(self, departures=None, last_updated=None):
    """
    """
    self._departures_min = departures or []

    if last_updated is not None:
      self._last_updated_sec = last_updated
    else:
      self._last_updated_sec = time.time()

  @property
  def last_updated(self):
    return self._last_updated_sec

  def get_departures(self, now=None):
    """
    """
    now = now if now is not None else time.time()
    offset_min = (now - self._last_updated_sec) / 60.0

    return [
        math.floor(departure - offset_min)
        for departure in self._departures_min]

  def get_next_departure(self):
    """
    """
    departures = self.get_departures()
    departures = filter(lambda e: e > 0, departures)
    return departures[0] if departures else None

  def get_departures_raw(self):
    """
    """
    return self._departures_min
