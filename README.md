# SIMPLE TASK MANAGEMENT SYSTEM
This is a simple task management system, for creating tasks, getting both all tasks and a single task, updating a task and deleting a task. 

## HOW TO START THE FLASK SERVER (TERMINAL 1)
* Clone the repository: `git clone https://github.com/Di-nobi/niyo-backend-assessment.git`
* Run: `pip install -r requirements.txt`
* Access the API directory: `cd api/v1`
* Run: `flask run`

## ON TERMINAL 2 (WHILE FLASK IS RUNNING)
* Firstly, authenticate the user to be able to access and create tasks
  ### REGISTER A USER
  ```
  siris@siris:~$ curl -XPOST -d 'email=udeh@gmail.co' -d 'password=12345' http://0.0.0.0:5000/api/v1/register
  {"id":"d63366d1-5590-40f6-83e2fb0d650d1ad7","jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTIyMywianRpIjoiNWI3YmJjODgtNjM3Yi00YjRkLTlmNjUtNGINjNjMmVjZTRjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTIyMywiY3NyZiI6Ijk2MmIyNDI4LWM2NzAtNDc1ZC04Y2VhLTI0MzI3MmZhZDNhiIsImV4cCI6MTcxNjEzMjEyM30.KqKrtk7hiketXCtF3jZNJneJ-bjjmu0N6bSHKu6ZIRk","message":"Registration successful"}
* Secondly, log in the user to retrieve the jwt, so to be able the work on the task creation
  ### LOGS IN A USER
  ```
  siris@siris:~$ curl -XPOST -d 'email=udeh@gmail.co' -d 'password=12345' http://0.0.0.0:5000/api/v1/login
  {"jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1Yi6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_oqGEuDt_Z8u_ORde48BOMq0MDXak","message":"Successfully logged in"}

### CREATES A NEW TASK WITH THE JWT GOTTEN AFTER LOGIN
```
siris@siris:~$ curl -XPOST -d 'subject=Create a task management system' -d 'comment=You can use any programming language of your choice preferably nextjs' -d 'due_date=20-05-2024' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_o7qGEuDt_Z8u_ORde48BOMq0MDXak" http://0.0.0.0:5000/api/v1/tasks
{"message":"Task successfully created","task_id":17}
```
### UPDATES A TASK
```
siris@siris:~$ curl -XPUT -d 'subject=Create a task management system' -d 'comment=You can use any programming language of your choice preferably nextjs' -d 'due_date=20-05-2024' -d 'status=Done' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_o7qGEuDt_Z8u_ORde48BOMq0MDXak" http://0.0.0.0:5000/api/v1/tasks/17
{"comment":"You can use any programming language of your choice preferably nextjs","due_date":"20-05-2024","message":"Task Info Updated successfully","status":"Done","subject":"Create a task management system"}
```
### READ A TASK
```
siris@siris:~$ curl -XGET  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_o7qGEuDt_Z8u_ORde48BOMq0MDXak" http://0.0.0.0:5000/api/v1/tasks/17
{"comment":"You can use any programming language of your choice preferably nextjs","created_at":"Sun, 19 May 2024 15:03:05 GMT","due_date":"20-05-2024","id":17,"status":"Done","subject":"Create a task management system"}
```
### READ ALL TASKS
```
siris@siris:~$ curl -XGET  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_o7qGEuDt_Z8u_ORde48BOMq0MDXak" http://0.0.0.0:5000/api/v1/tasks/
[{"comment":"It should use only mongodb","created_at":"2024-05-19T06:19:29.424793","due_date":"30-05-2024","id":14,"status":"pending","subject":"Create a Firebase backend","user_id":"578e5b55-ade2-4107-af34-178235187ae5"},{"comment":"It should use only mongodb","created_at":"2024-05-19T08:00:09.391503","due_date":"30-05-2024","id":15,"status":"pending","subject":"Create a Firebase backend","user_id":"578e5b55-ade2-4107-af34-178235187ae5"},{"comment":"Check out all codes","created_at":"2024-05-19T09:50:13.383456","due_date":"30-05-2024","id":16,"status":"pending","subject":"Create a Firebase backend","user_id":"578e5b55-ade2-4107-af34-178235187ae5"},{"comment":"You can use any programming language of your choice preferably nextjs","created_at":"2024-05-19T15:03:05.911996","due_date":"20-05-2024","id":17,"status":"Done","subject":"Create a task management system","user_id":"d63366d1-5590-40f6-83e2-fb0d650d1ad7"}]
```
### DELETES A TASK
```
siris@siris:~$ curl -XDELETE  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_o7qGEuDt_Z8u_ORde48BOMq0MDXak" http://0.0.0.0:5000/api/v1/tasks/17
```
P/S - Please create a user and log in to be able to use the jwt and work on the tasks

