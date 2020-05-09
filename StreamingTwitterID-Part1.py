#!/usr/bin/env python

#creating the kinesis stream
import boto3

STREAM_NAME = 'twitter_bigdata'

client = boto3.client('kinesis')
response = client.create_stream(
   StreamName=STREAM_NAME,
   ShardCount=1
)

#importing the necessary packages
from TwitterAPI import TwitterAPI
import json
import boto3
import twitter


#accessing the API

kinesis = boto3.client('kinesis')

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

#r = api.request()

#for locations
r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
#for userids @abcdef:
#r = api.request('statuses/filter', {'follow':'123456'})
#for general text searches
#r = api.request('statuses/filter', {'track':'iphone'})
#r = api.request('user', {'screen_name':'realDonaldTrump'})

#r = api.GetUserTimeline(screen_name="akras14", count=10)



for item in r:
    tweets = [item.AsDict()]
    print (tweets)
    response = kinesis.put_record(StreamName=STREAM_NAME, Data=json.dumps(tweets), PartitionKey="filler")

import boto3
import time
import json
## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis")
shard_id = "shardId-000000000000" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName=STREAM_NAME, ShardId=shard_id, ShardIteratorType="TRIM_HORIZON")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
     out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
     shard_it = out["NextShardIterator"]
     print(out);
     time.sleep(1.0)


# In[ ]:
