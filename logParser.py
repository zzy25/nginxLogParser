import getLogInfo as log

class logParser:
    def __init__(self, fileName):
        self.getLogInfo = log.getLogInformation(fileName)

    def numberOfErrors(self):
        e2 = self.getLogInfo.getNumberOfError(2)
        e3 = self.getLogInfo.getNumberOfError(3)
        e4 = self.getLogInfo.getNumberOfError(4)
        e5 = self.getLogInfo.getNumberOfError(5)
        return [e2, e3, e4, e5]

    def parseNumberOfErrors(self):
        list = self.numberOfErrors()
        res = ("\tCod --- | --- Hits\t\n")
        res += ("\t2XX --- | --- %s\t\n" % (list[0]))
        res += ("\t3XX --- | --- %s\t\n" % (list[1]))
        res += ("\t4XX --- | --- %s\t\n" % (list[2]))
        res +=  ("\t5XX --- | --- %s\t\n" % (list[3]))
        return res

    def parseHoursAccess(self):
        list = self.getLogInfo.getNumberOfHourAccess()
        res = ("\tTime -- | --- Hits\t\n")
        for a in list.items():
            res += ("\t%s:00 - | --- %s\t\n" % (a[0], a[1]))
        return res

    def parseMostAccessUrl(self):
        list = self.getLogInfo.getNumberAccessedUrl()
        res =  ("\tHits -- URL\t\n")
        for a in list.items():
            res += ("\t%s -- %s\t\n" % (a[1], a[0]))
        return res

    def parseUrlPerCode(self, code):
        list = self.getLogInfo.getUrlPeerCode(code)
        nErrors = len(list)
        res =  ("Found %d error(s)" %(nErrors))
        if nErrors > 1:
            res += ("\tCODE\tURL + URI\n")
            for a in list.items():
                res += ("\t%s\t\t%s - %s\n" %(a[1][0], a[0], a[1][1]))
        else:
            res = ("\tCould not find any record for the query\n")
        return res