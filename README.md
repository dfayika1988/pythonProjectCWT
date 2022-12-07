# Project Setup

##


## Installation

Install the application dependencies:
```shell
make init
```

## Usage

1. Start the database:
    ```shell
    docker-compose up -d
    ```

2. Start the application in the development mode:
    ```shell
    make run
    ```

After executing the last command, application should start up and expose api at: <http://localhost:8080/graphql>
