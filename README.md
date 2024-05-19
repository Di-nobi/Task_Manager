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
  {"id":"d63366d1-5590-40f6-83e2fb0d650d1ad7","jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTIyMywianRpIjoiNWI3YmJjODgtNjM3Yi00YjRkLTlmNjUtNGINjNjMmVjZTRjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTIyMywiY3NyZiI6Ijk2MmIyNDI4LWM2NzAtNDc1ZC04Y2VhLTI0MzI3MmZhZDNhiIsImV4cCI6MTcxNjEzMjEyM30.KqKrtk7hiketXCtF3jZNJneJ-bjjmu0N6bSHKu6ZIRk","message":"Registration successful"}```
* Secondly, log in the user to retrieve the jwt, so to be able the work on the task creation
  ### LOGS IN A USER
  ```
  siris@siris:~$ curl -XPOST -d 'email=udeh@gmail.co' -d 'password=12345' http://0.0.0.0:5000/api/v1/login
  {"jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1Yi6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_oqGEuDt_Z8u_ORde48BOMq0MDXak","message":"Successfully logged in"}```
### CREATES A NEW TASK WITH THE JWT GOTTEN AFTER LOGIN
```
siris@siris:~$ curl -XPOST -d 'subject=Create a task management system' -d 'comment=You can use any programming language of your choice preferably nextjs' -d 'due_date=20-05-2024' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTg2MCwianRpIjoiNTZmNjBmMTAtMjkzZC00MWI5LWI4MDktZTkxNjdlYzY0NjZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTg2MCwiY3NyZiI6IjcwODM2N2FmLTRjYzItNDMzZi1iZjM0LWY1YzI4NjJlOGIwNyIsImV4cCI6MTcxNjEzMjc2MH0.QrqNxWdzUSA8s_o7qGEuDt_Z8u_ORde48BOMq0MDXak" http://0.0.0.0:5000/api/v1/tasks
{"message":"Task successfully created","task_id":17}```

