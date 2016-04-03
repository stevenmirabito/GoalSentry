# Goal Sentry API Documentation

### Tables
##### Get Tables
_Not currently implemented._

##### Table Status
Query for the status of a table. This will return the table name, game state, user(s) authenticated, and current scores. Tables have a maximum of two user slots.

```
GET /table/:id
```

Example Response:

```
{
    "status": {
        "success": true
    },
    "table": {
        "id": 1,
        "name": "Foosball",
        "in_use": true
    }
}
```

##### Create Table
_Not currently implemented._

##### Delete Table
_Not currently implemented._

##### Modify Table Metadata
_Not currently implemented._

--------------------

### Games

##### Get all games
Returns all registered games.

```
GET /games
```

Example Response:

```
{
    "status": {
        "success": true
    },
    "games": {
        {
            "id": "j0zkZ3NMe3zWOYM8jHuLhyQ7RDjMPaFM",
            "table": 1,
            "time_started": 1459676696,
            "time_completed": 1459676716,
            "completed": true,
            "users": {
                1: {
                    "authenticated": true,
                    "id": 32
                },
                2: {
                    "authenticated": true,
                    "id": 46
                }
            }
        },
        {
            "id": "wtouO3lgrfuOLbeCQtIxks6BAHQXTCzZ",
            "table": 1,
            "time_started": 1459543696,
            "time_completed": 1459446716,
            "completed": true,
            "users": {
                1: {
                    "authenticated": false
                },
                2: {
                    "authenticated": false
                }
            }
        },
    }
}
```

##### Get games for a table
_Not currently implemented._

##### Get game by UUID
Start a new game. Automatically updates the table's `in_use` property and returns the new game's alphanumeric UUID (along with its otherwise empty state).

```
GET /game/:uuid
```

Example Response:

```
{
    "status": {
        "success": true
    },
    "game": {
        "uuid": "wtouO3lgrfuOLbeCQtIxks6BAHQXTCzZ",
        "users": {
            1: {
                "authenticated": true,
                "id": 32
            },
            2: {
                "authenticated": false
            }
        }
    }
}
```

##### Start a New Game
Start a new game. Automatically updates the table's `in_use` property (based on API key) and returns the new game's alphanumeric UUID (along with its otherwise empty state).

```
POST /games
{
  "token": {
        "key": "TABLE_API_KEY"
  }
}
```

Example Response:

```
{
    "status": {
        "success": true
    },
    "game": {
        "id": "wtouO3lgrfuOLbeCQtIxks6BAHQXTCzZ",
        "table": 1,
        "time_started": 1459543696,
        "time_completed": null,
        "completed": false,
        "users": {
            1: {
                "authenticated": false
            },
            2: {
                "authenticated": false
            }
        }
    }
}
```

##### Authenticate to a Game
Authenticate a user to the game by passing the user's RFID or iButton tag identifier. This method will return the updated game state and the user's information for display. For convenience, this method will also register first-time users based on the data obtained from the configured authentication service.

```
POST /game/:uuid/authenticate
{
  "token": {
        "key": "TABLE_API_KEY"
  },
  "authenticate": {
        "identifier": "364bfldsh9sxx3fn3fmh734e"
  }
}
```

Example Response:

```
{
    "status": {
        "success": true
    },
    "game": {
        "id": "wtouO3lgrfuOLbeCQtIxks6BAHQXTCzZ",
        "table": 1,
        "time_started": 1459543696,
        "time_completed": null,
        "completed": false,
        "users": {
            1: {
                "authenticated": true,
                "id": 1
            },
            2: {
                "authenticated": false
            }
        }
    }
    "user": {
        "id": 1,
        "username": "sjohnson",
        "name": "Stanley Johnson",
        "rank": 146
    }
}
```

##### Cancel a Game
If the user chooses to end the game early, this method will delete the game and reset the table, including updaing the `in_use` property, clearing all authenticated users. Scores and rankings will not be retained or affected.

```
DELETE /game/:uuid
{
  "token": {
        "key": "TABLE_API_KEY"
  }
}
```

Example Response:

```
{
    "status": {
        "success": true
    }
}
```

--------------------

### Users

##### Get All Users
Returns all registered users.

```
GET /users
```

Example Response:

```
{
    "status": {
        "success": true
    },
    "users": {
        {
            "id": 1,
            "username": "sjohnson",
            "name": "Stanley Johnson",
            "rank": 146
        },
        {
            "id": 2,
            "username": "jbrown",
            "name": "Jody Brown",
            "rank": 54
        }
}
```

##### Get User by ID
Returns the data for the user with the specified ID.

```
GET /user/:id
```

Example Response:

```
{
    "status": {
        "success": true
    },
    "user": {
        "id": 1,
        "username": "sjohnson",
        "name": "Stanley Johnson",
        "rank": 146
    }
}
```

##### Add New User
_Not currently implemented._

##### Modify User Metadata
_Not currently implemented._

##### Get User by Authentication Identifier
_Not currently implemented._