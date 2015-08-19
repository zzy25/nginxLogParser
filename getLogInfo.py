import re
from operator import itemgetter
from collections import OrderedDict


class getLogInformation:
    # Constructor
    def __init__(self, filename):
        logFile = open(filename)
        self.data = logFile.read()

    # Get all Ips that accessed the page
    def getIpAddress():
        return re.findall(r'[0-9]+(?:\.[0-9]+){3}', self.data)


    # Get all unique ips
    def getUniqIpAddress(self):
        unique = getIpAddress()
        return list(set(unique))


    # Get all 40x codes
    def getMissedUrls(self):
        return re.findall(r'(\"GET\ [\\\/\\\ \w\.]+\"\ 40[0-9])', self.data)


    # Get all 20x codes
    def getCoolUrls(self):
        return re.findall(r'(\"GET\ [\\\/\\\ \w\.]+\"\ 20[0-9])', self.data)


    # Get all 50x codes
    def getServerErrosUrls(self):
        return re.findall(r'(\"GET\ [\\\/\\\ \w\.]+\"\ 50[0-9])', self.data)


    # Get all 30x codes
    def getRedirectsUrls(self):
        return re.findall(r'(\"GET\ [\\\/\\\ \w\.]+\"\ 30[0-9])', self.data)


    # Get all Codes
    def getAllErrorsCode(self):
        return re.findall(r'(\"GET\ [\\\/\\\ \w\.]+\"\ [0-9]{3})', self.data)


    # Get all code errors
    def getErrorsCode(self):
        listAllErros = self.getAllErrorsCode()
        e400 = []
        e500 = []
        for a in listAllErros:
            if bool(re.search(r'4[0-9]{2}', a)):
                e400.append(re.findall(r'4[0-9]{2}', a))
                if bool(re.search(r'5[0-9]{2}', a)):
                    e500.append(re.findall(r'5[0-9]{2}', a))

        return [e400, e500]


    # Get all accessed urls
    def getAccessedUrl(self):
        return re.findall(r'http://[\w\:\/\.]+', self.data)


    # Return URL and its hits (order by hits)
    def getNumberAccessedUrl(self):
        allUrls = self.getAccessedUrl()
        mostAccess = {}
        for a in allUrls:
            if mostAccess.has_key(a):
                mostAccess[a] += 1
            else:
                mostAccess[a] = 1
        return OrderedDict(sorted(mostAccess.items(), key=itemgetter(1), reverse=True))


    def getNumberOfError(self, errorCode):
        listAllErrors = self.getAllErrorsCode()
        errors = []
        for a in listAllErrors:
            if bool(re.search(r'%s' % errorCode, a)):
                errors.append(re.findall(r'errorCode', a))
        return len(errors)


    # Get hour access
    def getHourAccess(self):
        return re.findall(r'[0-9]{2}/[a-zA-z]{3}/[0-9]{4}\:[0-9]{2}', self.data)


    # Get number off access by hour
    def getNumberOfHourAccess(self):
        allHours = self.getHourAccess()
        mostAccess = {}
        for a in allHours:
            if mostAccess.has_key(a[-2:]):
                mostAccess[a[-2:]] = +1
            else:
                mostAccess[a[-2:]] = 1
        return sorted(mostAccess)


    # Get url peer httpCode
    def getUrlPeerCode(self, code):
        urlsAndCodesAndGarbage = re.findall(r'GET\ [/\w\.]+\ HTTP\/1\.1\"\ %s[0-9]{2}\ [0-9]+\ "[\w\:\\./]+"' % code, self.data)
        codesAndUrl = {}
        for a in urlsAndCodesAndGarbage:
            codesAndUrl[re.findall(r'http://[\w\:\/\.]+', a)[0]] = (re.findall(r'"\ [0-9]{3}', a))[0][2:], \
                                                                   re.findall(r'GET\ /[\w/\-\.\ ]+', a)[0]
        return codesAndUrl
