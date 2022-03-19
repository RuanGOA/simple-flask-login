# Simple Flask API

This is a dockerized flask API that connects a Mongodb and uses JWT authentication, created to exercise those concepts.

## How to run

You're gonna need `Docker` and `docker-compose` installed on your machine.

First, you have to copy the `.env.example` file to a `.env` file and after that, fill the environment variables with values of your choice.

Finally you just have to execute the following command. It will make python and mongo docker containers run on your machine.

```sh
docker-compose up --build
```

> Created by [Victor Brandão](https://github.com/victorbrandaoa) and [Ruan Gomes](https://github.com/ruangoa)
