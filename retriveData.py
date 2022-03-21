from xml.etree.ElementTree import tostring
from thor_requests.connect import Connect
import codecs


def getData(transactionID):
    connector = Connect("https://testnet.veblocks.net")
    text = connector.get_tx(transactionID)
    data = text.get('clauses')[0].get('data')

    data = data[2:]
    binary_str = codecs.decode(data, "hex")
    return (str(binary_str,'utf-8'))
