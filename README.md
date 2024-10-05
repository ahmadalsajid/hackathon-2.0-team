# hackathon-2.0-team

## Project setup

Copy the [sample.env](./sample.env) file into [](./.env), and update the
credentials according to you. Then, spin up the containers with

```
$ docker compoes up
```

This will create all the applications and create a django superuser from your
`.env` file credentials. A [scheduled task](./users/tasks.py) will run every
10 minutes to collect data from TikTok and store them into the database.
We have 2 different APIs, that we can use to extract data

```
http://localhost:8000/api/users/videos
http://localhost:8000/api/users/tiktokers
```

Also, you can use URL parameters for filtering,
i.e. `?items_per_page=10&page=1&username=some_user`