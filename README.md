# UCU Data Engineering Cloud Providers HW2: Function as a Service

I built CLoud Function which is triggered by HTTP request and takes some data from user in json format and stores it in Google Cloud Storage bucket. 

To deploy a function I used this command:
```
gcloud functions deploy func_http --runtime python39 --trigger-http
```
It takes around 2 min to deploy a function. After it's completed, we can send requests to it like this:
```
gcloud functions call func_http --data '{"name":"X"}'
```
It should return the following message:
result: Hello X! Your request has been save to Cloud Storage object

To see the logs, please use:
```
gcloud functions logs read func_http
```

Function successfuly deployed screenshot:
<img width="1203" alt="image" src="https://user-images.githubusercontent.com/51317733/174136175-8dbe3c06-c0f4-4d8a-876e-25eab3c65b61.png">


Each request is stored in separate file in GSC with random generated name.

<img width="955" alt="image" src="https://user-images.githubusercontent.com/51317733/174136074-37967c97-daa7-4de2-aa59-25e375181c16.png">

Example call:
<img width="751" alt="image" src="https://user-images.githubusercontent.com/51317733/174136283-81d4b15f-b973-472f-ba84-6a42421c35e1.png">
Result:
<img width="954" alt="image" src="https://user-images.githubusercontent.com/51317733/174136336-c26c26d4-7d65-49f3-9791-934141d1d14a.png">
<img width="237" alt="image" src="https://user-images.githubusercontent.com/51317733/174136367-1b136a15-e28e-4449-a5cb-75b6eefc4633.png">

