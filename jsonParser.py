import getLogInfo as log


class jsonParser:

    def __init__(self, fileName):
        self.getLogInfo = log.getLogInformation("example");
    def numberOfErrors(self):
        e2 = self.getLogInfo.getNumberOfError(2)
        e3 = self.getLogInfo.getNumberOfError(3)
        e4 = self.getLogInfo.getNumberOfError(4)
        e5 = self.getLogInfo.getNumberOfError(5)
        return [e2, e3, e4, e5]

    def jsonNumberOfErrors(self):
        list = self.numberOfErrors()
        json = '{ "NumberErros" : {';
        json += ('"2xx": %s,' % (list[0]))
        json += ('"3xx": %s,' % (list[1]))
        json += ('"4xx": %s,' % (list[2]))
        json += ('"5xx": %s' % (list[3]))
        json += ' } }'
        return json

    def jsonHoursAccess(self):
        list = self.getLogInfo.getNumberOfHourAccess()
        json = '{ "HoursAccess" : { '
        for a in list.items():
            json += ('"%s": %d,' % (a[0], a[1]))
        json = json.rstrip(',')
        json += ' } }'
        return  json



    def jsonMostAccessUrl(self):
        list = self.getLogInfo.getNumberAccessedUrl()
        json = '{ "MostAccessUrl" : { '
        for a in list.items():
            json += ('"%s": %d,' % (a[0], a[1]))
        json = json.rstrip(',')
        json += ' } }'
        return  json

    def jsonUrlPerCode(self, code):
        list = self.getLogInfo.getUrlPeerCode(code)
        nErrors = len(list)
        if nErrors > 1:
            json = '{ "UrlPeerCode" : { '
            for a in list.items():
                json += ('"%s": "%s - %s",' % (a[1][0], a[0], a[1][1]))
            json = json.rstrip(',')
            json += ' } }'
        else:
            return '{}'
        return json