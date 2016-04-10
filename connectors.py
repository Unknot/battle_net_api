#! python3

from urllib import request
import pymongo
import json
import abc

class BaseConnector(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, apikey):
        self.apikey = apikey

    @abc.abstractmethod
    def __repr__(self):
        "Don't forget to overload this."

    @abc.abstractmethod
    def build(self):
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

    def build(self):
        self.url = self.__url_template.format(apikey=self.apikey,
            server=self.server,
            realm=self.realm,
            locale=self.locale)

    def call(self):
        self.json_gate = json.loads(request.urlopen(self.url).read().decode())
        self.data_url = self.json_gate["files"][0]["url"]
        self.json_data = json.loads(request.urlopen(self.data_url).read().\
            decode())
        self.json_data["lastModified"] = self.json_gate["files"][0]["lastModified"]
    

if __name__ == "__main__":
    apikey = "58dkavakqnjtvgqvasdvuqc4z3yys8p4"
    server = "us"
    realm = "exodar"
    locale = "en_US"

    con = AuctionConnector(apikey, server, realm, locale)
    print(con)
    # print(AuctionConnector.get_url_template())
    con.build()
    print(con.url)
    con.call()
    print(con.json_gate)
    print(len(con.json_data))

    # sturingu = "hey{}dude"
    # print(sturingu)
    # print(sturingu.format(", "))