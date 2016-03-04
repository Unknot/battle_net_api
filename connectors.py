#! python3

from urllib import request
import abc

class BaseConnector(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, apikey):
        self.apikey = apikey

    @abc.abstractmethod
    def __repr__(self):
        "Don't forget to overload this."

    @abc.abstractmethod
    def build_connector(self):
        "The method for building the url that will be used in the request"


class AuctionConnector(BaseConnector):
    __url_template = "https://{server}.api.battle.net/wow/auction/data/{realm}?locale={locale}&apikey={apikey}"

    @classmethod
    def get_url_template(cls):
        return cls.__url_template

    def __init__(self, apikey, server, realm, locale):
        BaseConnector.__init__(self, apikey)
        self.server = server
        self.realm = realm
        self.locale = locale


    def __repr__(self):
        return "AuctionConnector(apikey='{apikey}',server='{server}',realm='{realm}',locale='{locale}')".format(apikey=self.apikey,
            server=self.server,
            realm=self.realm,
            locale=self.locale)

    def build_connector(self):
        self.url = "https://{server}.api.battle.net/wow/auction/data/{realm}?locale={locale}&apikey={apikey}".format(apikey=self.apikey,
            server=self.server,
            realm=self.realm,
            locale=self.locale)
    

if __name__ == "__main__":
    apikey = "58dkavakqnjtvgqvasdvuqc4z3yys8p4"
    server = "us"
    realm = "medivh"
    locale = "en_US"

    con = AuctionConnector(apikey, server, realm, locale)
    print(con)
    # print(AuctionConnector.get_url_template())
    con.build_connector()
    print(con.url)