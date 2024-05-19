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
  curl -XPOST -d 'email=udeh@gmail.co' -d 'password=12345' http://0.0.0.0:5000/api/v1/register
{"id":"d63366d1-5590-40f6-83e2-fb0d650d1ad7","jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjEzMTIyMywianRpIjoiNWI3YmJjODgtNjM3Yi00YjRkLTlmNjUtNGI2NjNjMmVjZTRjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQ2MzM2NmQxLTU1OTAtNDBmNi04M2UyLWZiMGQ2NTBkMWFkNyIsIm5iZiI6MTcxNjEzMTIyMywiY3NyZiI6Ijk2MmIyNDI4LWM2NzAtNDc1ZC04Y2VhLTI0MzI3MmZhZDNhMiIsImV4cCI6MTcxNjEzMjEyM30.KqKrtk7hiketXCtF3jZNJneJ-bjjmu0N6bSHKu6ZIRk",
"message":"Registration successful"}
```
