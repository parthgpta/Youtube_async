# About API 

The GET video API helps us in returning the stored video data in a paginated response sorted in descending order of published datetime .It takes parameter page ,and the maximum number of records it sends is 10 .

##### Endpoint - https://localhost/get/?page=x 

It send the Json response as - 
```
  {
    'items' : [
                {
                  'title': "" ,
                  'description' : "" ,
                  'thumbnail' : "" ,
                  'published' : ""
                } ,
                {
                  'title': "" ,
                  'description' : "" ,
                  'thumbnail' : "" ,
                  'published' : ""
                } , ...             
             ]
  }
```
