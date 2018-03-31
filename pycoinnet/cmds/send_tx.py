import argparse
import asyncio

import binascii
from pycoin.message.InvItem import InvItem, ITEM_TYPE_BLOCK, ITEM_TYPE_TX
from pycoin.serialize import h2b_rev

from pycoinnet.networks import MAINNET, TESTNET, REGTEST
from pycoinnet.cmds.common import init_logging, peer_connect_pipeline
from pycoinnet.MappingQueue import MappingQueue
from pycoinnet.inv_batcher import InvBatcher
from pycoinnet.version import NODE_NETWORK, version_data_for_peer, NODE_WITNESS
from pycoinnet.PeerEvent import PeerEvent


async def connect_peers(network, max_peer_count=1):
    peers = []

    # add some peers to InvBatcher
    async def do_add_peer(peer, q):
        version = peer.version
        if version["services"] & NODE_NETWORK == 0:
            peer.close()
            return
        peers.append(peer)

    queue = MappingQueue(dict(input_q=peer_connect_pipeline(network), callback_f=do_add_peer))
    asyncio.get_event_loop().create_task(queue.get())

    return queue, peers


async def send_transaction(args, network):
    queue, peers = await connect_peers(network, max_peer_count=1)
    tb = binascii.unhexlify(transaction.encode())
    pad = b'\x00'

    missing = len(tb) % 32

    item = InvItem(ITEM_TYPE_TX, tb)
    await asyncio.sleep(1)

    for peer in peers:
        future = peer.send_msg('inv', items=[item])
        result = future


def main():

    #init_logging()
    #parser = argparse.ArgumentParser(description="Fetch a block by ID.")
    #parser.add_argument('id', nargs="+", help='Block ID as hex')
#
    #args = parser.parse_args()
#
    network = REGTEST
    tx = '00'
    asyncio.get_event_loop().run_until_complete(send_transaction(tx, network))


if __name__ == '__main__':
    main()
