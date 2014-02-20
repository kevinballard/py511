"""
"""

_ROOT_URL = 'http://services.my511.org/Transit2.0/'

_GET_AGENCIES_PATH = 'GetAgencies.aspx'
_GET_ROUTES_FOR_AGENCY_PATH = 'GetRoutesForAgency.aspx'
_GET_ROUTES_FOR_AGENCIES_PATH = 'GetRoutesForAgencies.aspx'
_GET_STOPS_FOR_ROUTE_PATH = 'GetStopsForRoute.aspx'
_GET_STOPS_FOR_ROUTES_PATH = 'GetStopsForRoutes.aspx'
_GET_DEPARTURES_FOR_STOP_NAME_PATH = '/GetNextDeparturesByStopName.aspx'
_GET_DEPARTURES_FOR_STOP_CODE_PATH = '/GetNextDeparturesByStopCode.aspx'

class My511Client(object):
  """
  """

  def __init__(self, token):
    """
    """
    self._token = token
    self._session = None

  def GetAgencies(self):
    """
    """
