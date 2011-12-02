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
