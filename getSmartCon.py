from subprocess import call
from xml.etree.ElementTree import tostring
from psycopg2 import connect
from thor_requests.connect import Connect
import codecs
from thor_requests.connect import Connect
from thor_requests.contract import Contract
from thor_devkit.cry import mnemonic
from thor_requests.wallet import Wallet

words=['upper','kiss', 'report', 'burst', 'heavy', 'witness', 'surge', 'carry', 'attend', 'mind', 'alien', 'similar']
_privatekey = mnemonic.derive_private_key(words, 0).hex()
_wallet = Wallet.fromPrivateKey(bytes.fromhex(_privatekey))
connector = Connect("https://testnet.veblocks.net")
_contract_addr = '0xBE6C91686BF4dB2cFD4Ea8def24A20fDE22F8510'

_contract = Contract("test.json")

def retrieve(id):
    res = connector.call(
        caller='0x240edd80b222AA55cCfEC327526B7F41e40b5dD0', 
        contract=_contract,
        func_name="retrieve",
        func_params=[id],
        to=_contract_addr,
    )
    return res['decoded']['0']

def store(id, str):
    send = connector.transact(_wallet, _contract, "store", [id, str], to=_contract_addr)
    print(send)
