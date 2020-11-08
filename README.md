# music-metadata-service #
The music-metadata-service is used to store metadata 
## Requirements ##
The music-metadaa-servuce is a Dockerized application. The system which the service is 
to be deployed needs to have installed  
 * docker v.
 * docker-compose v.
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

-TODO-
```
cd 
docker-compose up -d
```

## Assumptions ## 
The user provides csv files with metadata. This data is used to add new entries 
or update existing ones on the Database.  
It is assumed that:  

 * csv files contain the following headers:  
     * title 
     * contributors 
     * iswc 
     * source 
     * id
 * Every record on the csv file must contain an iswc  
   (In case no iswc the record is discarded)
 
     
## Services ##

The application consists of two services.  
 * metadata-api  
 * Postgres  
 
### metadata-api ###
The metadata-api API consist of two endpoints:  
* POST /upload  
  REQUEST    
  ```
  TODO
  ```
  RESPONSE 
  
  200 application/json  
  ```
  {
      "data": {
          "added": {
              "amount": "string"
          }, 
          "updated": {
              "ammount": "string"
          }, 
          "skipped": {
              "amount": "string", 
              "skipped_line": ["string"]
          }
      }, 
      "response": {
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

* GET /download?iswc=iswc_no  
  RESPONSE
 
  200 application/json
  
  ```
  TODO
  ```

  404 application/json
  -TODO-
  ```
  TODO
  ```
  
  500 application/json
  -TODO-
  ```
  TODO
  ```

* GET /metadata/iswc_no  
  RESPONSE  
  
  200 application/json  
  ```
  {
      "data": {
          "iswc": "string", 
          "title": "string", 
          "contributors": ["string"], 
          "source": [ 
              "source": "string", 
              "id", "string"
          ]
      }, 
      "response": {
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

### Postgres ###

As the data stored is metadata a relationship database is more suitable. Postgres is chosen for this implementation.  

The DB EERD is as follows  

![Alt text](./images/bmat_DB_EERD_dark.png?raw=true "Optional Title")  

The data is stored on three tables  

 * METADATA  
     * iswc  
     * title  
 * CONTRIBUTORS  
     * iswc  
     * contributor  
 * SOURCE  
     * iswc  
     * source  
     * id  
 
 
