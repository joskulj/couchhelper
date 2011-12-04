
import httplib

class CouchURI(object):
    """
    Helper class to create a URI
    """

    def __init__(self, endflag=False):
        """
        creates an instance
        Parameters:
        - endflag
          if True, the URI ends with a slash
        """
        self._endflag = endflag
        self._elements = []

    def get_element(self, index):
        """
        returns an element of the URI
        Parameters:
        - index
          index of an element
        Returns:
        - element or empty string
        """
        result = ""
        if  index >= 0 and index < len(self._elements):
            result = self._elements[index]
        return result

    def get_uri_string(self):
        """
        Returns:
        - URI as a string
        """
        stringlist = [ ]
        index = 0
        for element in self._elements:
            prev = self.get_element(index)
            if not prev.startswith("?"):
                stringlist.append("/")
            stringlist.append(element)
            index = index + 1
        if self._endflag:
            stringlist.append("/")
        return "".join(stringlist)

    def append(self, element, value=None):
        """
        appends an element or a variable to the URI
        Parameters:
        - element
          element or variable name
        - value
          optional variable name
        """
        newelement = element
        if value:
            newelement = "".join(["?", element, "=", value])
        self._elements.append(newelement)

class HttpHelper(object):
    """
    Helper class to support http communication
    """

    def __init__(self, host, port=5984):
        """
        creates an instance
        - host
          host to connect
        - port
          port to connect
        """
        self._host = host
        self._port = port

    def _connect(self):
        """
        connects to the server
        """
        return httplib.HTTPConnection(self._host, self._port)

    def get_host(self):
        """
        Returns:
        - host to connect
        """
        return self._host

    def get_port(self):
        """
        Returns:
        - port to connect
        """
        return self._port

    def get(self, uri):
        """
        invokes a get request
        Parameters:
        - uri
          URI to use
        Returns:
        - response of the request
        """
        c = self.connect()
        headers = {"Accept": "application/json"}
        c.request("GET", uri.get_uri_string(), None, headers)
        return c.getresponse()

    def post(self, uri, body):
        """
        invokes a post request
        Parameters:
        - uri
          URI to use
        - body
          body to transfer
        Returns:
        - response of the request
        """
        c = self.connect()
        headers = {"Content-type": "application/json"}
        c.request('POST', uri.get_uri_string(), body, headers)
        return c.getresponse()

    def put(self, uri, body):
        """
        invokes a put request
        Parameters:
        - uri
          URI to use
        - body
          body to transfer
        Returns:
        - response of the request
        """
        c = self.connect()
        if len(body) > 0:
            headers = {"Content-type": "application/json"}
            c.request("PUT", uri.get_uri_string(), body, headers)
        else:
            c.request("PUT", uri.get_uri_string(), body)
        return c.getresponse()

    def delete(self, uri):
        """
        invokes a post request
        Parameters:
        - uri
          URI to use
        Returns:
        - response of the request
        """
        c = self.connect()
        c.request("DELETE", uri.get_uri_string())
        return c.getresponse()

