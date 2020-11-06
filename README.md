# music-metadata-service #

## Services ##

The application consists of two services.  
 * metadata-api  
 * Postgres  
 
### metadata-api ###
The metadata-api is a Python Flask application. The API consist of two endpoints:  
* /upload  
  POST

* /metadata/<iswc>  
  GET  
  200 Response: application/json  
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
  
  404 Response: application/json  
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
  
  500 Response: application/json
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

![Alt text](/images/bmat_DB_EERD_dark.png?raw=true "Optional Title")  

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
 
 
