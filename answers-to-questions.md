# Part 1 

1. Describe briefly the matching and reconciling method chosen.  

Data coming in as csv files (base64 encoded). The metadata_api provides an endpoint 
(/upload) for these files to be uploaded. Files need to be sent over as a base64 
encoded string. The data is then decoded and by using a StringIO object (in memory 
file) converted into a python dict. Data is then stored in the database.  
Every row in the csv file needs to have at least an "iswc" No. As this number is 
international it is used to add additional information received in the future for the 
same piece of work. A check is being made of whether the particular "iswc" No. exists 
in the database. If this is the case the information is added to the alreafy existing 
record. Otherwise a new record is created. Fore every file uploaded the responce 
returns information of the data stored in the DB for the "iswc" No. contained in the 
csv file as well as the number of rows skipped due to not providing an "iswc".  

More information can be found on the [README.md](./README.md) api description). 


2. We constantly receive metadata from our providers, how would 
   you automatize the process?  
   
As stated above, the api provides the endpoint to upload csv files 
(base64 encoded) for streamlining the data ingestion.  

# Part 2 

1. Imagine that the Single View has 20 million musical works, do you 
think your solution would have a similar response time?  

Having a lot of data stored in the database will certainly have a cost 
on the response time. The larger the amount of data gets the response 
time gets slower.  

2. If not, what would you do to improve it?  

**Dowload**  
To address this issue different approaches can be had. 
It would depend on the amount of requests this api receives as well. 
In the case the requests are not many the database could be eployed 
on a cluster rather than on a single instance. In such case the response
time would not be much quicker but as requests are not frequent I believe 
it to be adequate. On the other hand, in case this is a popular api, 
receiving a lot of traffic, caching database data in an in memory DB, 
such as Redis, will bring response time down for at least the most 
frequently searched records. 

**Upload**  
File upload requires processing power rather than I/O throughput. 
To start, the service should be separated, one for file upload (mostly 
processor intensive) and one for download/searching (mostly I/O intensive). 
Being a dockerized application, spawning more than one instances of 
the service will address this issue. The bottleneck in this approach 
remains the DB, which can be solved in a similar manner as stated above.  