from datetime import date
from thor_devkit import cry, transaction
import requests
from random import randint
import json
from thor_requests.wallet import Wallet
from thor_devkit.cry import mnemonic
from sqlConnect import *



def postData(data, dataSent):
    _node_url = 'https://testnet.veblocks.net'
    _ChainTag = 39
    words=['upper','kiss', 'report', 'burst', 'heavy', 'witness', 'surge', 'carry', 'attend', 'mind', 'alien', 'similar']
    _privatekey = mnemonic.derive_private_key(words, 0).hex()
    BlockInfos = requests.get(_node_url + '/blocks/best')
    _BlockRef = BlockInfos.json()['id'][0:18]
    _Nonce = randint(10000000, 99999999)
    address = '0x240edd80b222AA55cCfEC327526B7F41e40b5dD0'
    
    _transaction_clauses = []
    _transaction_clauses.append({'to': address, 'value': 0, 'data': '0x' + data})

    
    body = {}
    body['chainTag'] = _ChainTag
    body['blockRef'] = _BlockRef
    body['expiration'] = 720
    body['clauses'] = _transaction_clauses
    body['gasPriceCoef'] = 0
    body['gas'] = 100000 # fixed to 100.000
    body['dependsOn'] = None
    body['nonce'] = _Nonce

    tx = transaction.Transaction(body)

    priv_key = bytes.fromhex(_privatekey)
    message_hash = tx.get_signing_hash()
    signature = cry.secp256k1.sign(message_hash, priv_key)

    tx.set_signature(signature)

    print('Created a transaction from ' + tx.get_origin() + ' with TXID: ' + tx.get_id() + '.')
    print('')

    encoded_bytes = tx.encode()
    print('The transaction will be send to the testnet node now.')

    tx_headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    tx_data = {'raw': '0x' + encoded_bytes.hex()}
    send_transaction = requests.post(_node_url + '/transactions', json=tx_data, headers=tx_headers)

    #Retrives Transaction ID
    txId = str(send_transaction.content)
    txId = txId[9:75]
    print('Response from Server: ' + str(send_transaction.content))

    #Date of creation and transaction ID stored in list
    
    today = date.today()
    sendToSql(today, txId)

