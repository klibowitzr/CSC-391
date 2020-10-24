# -*- coding: utf-8 -*-

"""
This is a partial set of browser agents for web scraping from a Mac.
More info:

https://developers.whatismybrowser.com/useragents/explore/software_name/chrome
"""

class agentsGalore:
    def __init__(self):
        self.agentSet = {
            "Android5.1" : ('Mozilla/5.0 (Linux; Android 5.1; '
                            'XT1032 Build/LPB23.13-58) '
                            'AppleWebKit/537.36 (KHTML, like Gecko)'
                            'Chrome/47.0.2526.83 Mobile Safari/537.36'),
            "iPad" : ('Mozilla/5.0 (iPad; CPIU OS8_3 like Mac OS X) '
                        'AppleWebKit/600.1.4 (KHTML, like Gecko) '
                        'CriOS/39.0.2171.50 Mobile/12F69 Safari/600.1.4'),

            "MacChrome64" : ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3)'
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/64.0.3282.140 Safari/537.36'),

            "MacFirefox58" : ('Mozilla/5.0'
                              '(Macintosh; Intel Mac OS X 10.13; rv:58.0)'
                              'Gecko/20100101 Firefox/58.0'),

            "MacSafari11" :  ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3)'
                           'AppleWebKit/604.5.6 (KHTML, like Gecko) '
                           'Version/11.0.3 Safari/604.5.6')
        }

        self.langSet = {
            "langUS" : 'en-US,en,q=0.8'
        }

        self.acceptSet = {
            "default" :  ('text/html,application/xhtml+xml,'
                        'application/xml;q=0.9,image/webp,*/*;q=0.8')
        }

        self.encodingSet = {
            "default" : 'gzip,deflate'
        }

    def getAgentTypes(self):
        return self.agentSet.keys()

    def getAgentString(self,agent):
        try:
            return self.agentSet[agent]
        except KeyError as e:
            print("KeyError:",e)
            print(agent,"is invalid agent type")
            return None

    def makeHeader(self,agentkey,acceptkey,encodekey,langkey):
        try:
            headers = {
                "User-Agent" : self.agentSet[agentkey],
                "Accept" : self.acceptSet[acceptkey],
                "Accept-Encoding" : self.encodingSet[encodekey],
                "Accept-Language" : self.langSet[langkey]
            }
            return headers
        except KeyError as e:
            print("KeyError:",e)
            return None


if __name__ == '__main__':
    ah = agentsGalore()
    print(ah.getAgentTypes())

    print(ah.getAgentString("iPad"))

    print(ah.makeHeader("iPad","default","default","langUS"))
