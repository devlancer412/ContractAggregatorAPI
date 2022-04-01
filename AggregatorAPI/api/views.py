from rest_framework import viewsets

from .serializers import EventSerializer
from .models import ContractEvent

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = ContractEvent.objects.all().order_by('EventId')
    serializer_class = EventSerializer

# web3 side
import json
import asyncio
import threading
from web3 import Web3
from asgiref.sync import sync_to_async

# add your blockchain connection information
infura_url = 'https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
web3 = Web3(Web3.HTTPProvider(infura_url))

# address and abi
address = '0xe5E76675109613B4C86D7d641CAe8e4aa2735FfD'
contact_abi = json.load(open('api/Ballot.json'))

contract = web3.eth.contract(address=address, abi=contact_abi['abi'])

# define function to handle events and print to the console

@sync_to_async
def record_save(record):
  return record.save()

async def handle_event(event):
    Id = Web3.toJSON(event.blockNumber) + '_' + Web3.toJSON(
        event.transactionIndex) + '_' + Web3.toJSON(event.logIndex)
    voter = Web3.toJSON(event.args.voter)
    proposal = Web3.toJSON(event.args.proposal)
    nevent = ContractEvent(EventId=Id, VoterAddress=voter, ProposalName=proposal)
    await record_save(nevent)

    print(event.transactionHash)
    print(event)
    # and whatever


# asynchronous defined function to loop
# this loop sets up an event filter and is looking for new entires for the "PairCreated" event
# this loop runs on a poll interval
async def log_loop(event_filter, poll_interval):
    while True:
        for Voted in event_filter.get_new_entries():
            await handle_event(Voted)
        await asyncio.sleep(poll_interval)


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

# when main is called
# create a filter for the latest block and look for the "PairCreated" event for the uniswap factory contract
# run an async loop
# try to run the log_loop function above every 2 seconds


def background_process():
    # print('start listening')
    event_filter = contract.events.Voted.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = get_or_create_eventloop()
    print('Listening started')
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2)))
        # log_loop(block_filter, 2),
        # log_loop(tx_filter, 2)))
    finally:
        # close loop to free up system resources
        print('Listening terminated')
        loop.close()


# main()
t = threading.Thread(target=background_process, args=(), kwargs={})
t.setDaemon(True)
t.start()
