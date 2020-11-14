# music-metadata-service #
The music-metadata-service is used to store metadata derived from uploaded csv files in a 
database as well as downloading records from a database to a csv file.
## Requirements ##
The music-metadata-service is a Dockerized application. The system which the service is 
to be deployed needs to have installed  
 * docker v19.03.13
 * docker-compose v1.23.1
 * port 5000
 * python 3.8 (optional for running the tests)

## Tests ## 
For running the tests there is no need to run the docker containers. In such case python3.8 
needs to be installed.

### Unit tests ### 
-TODO-
```
cd 
python
```

### Integration tests ### 
-TODO-
```
cd 
python
```

## Run the application ## 
From the application's root directory run 
```
docker-compose up -d
```

## Assumptions ## 
The user provides csv files with metadata. This data is used to add new entries 
or update existing ones in the Database.  
It is assumed that:  
* csv files contain the following headers:  
* title  
* contributors  
* iswc  
* source   
* id  
* Every record on the csv file must contain an iswc  
  (In case no iswc is provided, the record is discarded)  
* A contributor name is assigned to a particular iswc record only once  
  (contributor names are treated as unique)  
* source and id are stored on an array for a given iswc  
* Multiple contributors are returned in the csv file on the "contributors" column 
  seperated by "|"  
* Multiple ids as well as sources are returned in the csv file on their respected 
  columnsseperated by "|"   
 
     
## Services ##

The application consists of two services.  
 * metadata-api  
 * MongoDB 
 
### metadata-api ###
The metadata-api API consist of two endpoints:  
* POST /upload  
  REQUEST  
  Send the base64 encoded csv file   
  ```
  { 
    "file": "base64_string" 
  } 
  ```
  RESPONSE 
  
  200 application/json  
  ```
  {
    "data": [
        {
            "iswc": "string",
            "contributors": ["string"],
            "sources": [
                {
                    "source": "string",
                    "id": "string"
                }
            ],
            "title": "string"
        },
    ],
    "skipped": "string",
    "responce": {
        "code": "200",
        "status": "success"
    }
  } 
  ```
  
  400 application/json  
  ```
  { 
      "data": { 
          "message": "file upload error" 
      }, 
      "response": { 
          "code": "400", 
          "status": "client error" 
      } 
  } 
  ```
  
  500 application/json  
  ```
  { 
      "data": { 
          "message": "server error" 
      }, 
      "response": { 
          "code": "500", 
          "status": "server error" 
      } 
  } 
  ```

* POST /download  
  Make a POST request with a list of all the iswc records required for metadata retrieval.  
  REQUEST  
  ```
  { 
      "iswc": ["string"]
  } 
  ```
  
  RESPONSE
 
  200 application/json
  
  ```
  {
    "file": "string",
    "responce": {
        "code": "200",
        "status": "success"
    }
  }
  ```

  404 application/json  
  ```
  { 
      "data": { 
          message": "iswc is incorrect or does not exist" 
      }, 
      "response": { 
          "code": "404", 
          "status": "client error" 
      } 
  } 
  ```
  
  500 application/json
  ```
  { 
      "data": { 
          "message": "server error" 
      }, 
      "response": { 
          "code": "500", 
          "status": "server error" 
      } 
  } 
  ```

### MongoDB 
The database chosen for this application is MongoDB. Csv rows are entered on the 
"music-meta" database on one collection ("music") following the schema:  
```buildoutcfg
 {
    "_id" : ObjectId("string"), 
    "iswc" : "string", 
    "contributors" : ["string"], 
    "sources" : [ 
        { 
            "source" : "string", 
            "id" : "string" 
        }, 
    ], 
    "title" : "string" 
 }
```
**ATTENTIO !!!**  
The mongo container has no volumes attached to it. This results in data not 
being preserved once the container has been removed.  
This choice was made to avoid issues regarding user permissions on creating 
folders and files on the host OS.  

### Issues not addressed 
Contributors' names are currently handled as unique. This on the real world 
is certainly not the case as more than one person can share the same name.  
The source and id combination should be considered to be unique as it points to 
an external set of records (source: sony, id: 4). All ids and sources are 
concated in one column on the csv resulting in not having a clear picture of where 
this information has derived from. 
