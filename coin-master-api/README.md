# CoinMaster API

An API for discovering currencies exchange rate.  
This application uses [Exchange Rate API](https://www.exchangerate-api.com/) behind the scenes.

## API Usage

There are two APIs:
1. Get currency rate
2. Health check

For further API documentaion you can use Swagger.

### Get Currency Rate

Get the exchange rate between two currencies.

```bash
# You can use curl here
# curl http://localhost:8000/rate/<FROM>/<TO>
# For example:
curl http://localhost:8000/rate/USD/ILS
```

The response looks like this:
```json
{
    "rate": 0.3081
}
```

### Health check

Check the health of the API.

```bash
# You can use curl here
curl http://localhost:8000/health
```

The response looks like this on success:
```json
{
    "health": true
}
```

Or like this on failure:
```json
{
    "health": false
}
```

## Getting Started

### Dependencies

In order to have working development environment you should have:
1. Exchange Rate API token [(signup for free)](https://app.exchangerate-api.com/sign-up)
2. python (3.9 or newer)
3. poetry
4. make (recommended)
5. docker (recommended)

*Note: Please don't use Windows...*

### Design

This is a simple FastAPI application that can be run with `uvicorn`.  
It depends on the third party Exchange Rate API so an API token should be generated and configured.

### Configuration

The app gets configuration via environment variables (case insensitive).
The following configurations are supported:

|Variable|Description|Required/Optional|
|--------|-----------|-----------------|
|EXCHANGE_BASE_URL|The base URL of Exchange Rate API<br> Example: `https://v6.exchangerate-api.com`|Required|
|EXCHANGE_API_KEY|The API key for Exchange Rate API|Required|
|LOG_LEVEL|Application log level<br> Options: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`<br> Defaults to `INFO`|Optional|
|JSON_LOGGING|If set, application logs will be JSON formatted<br> Defaults to `false`|Optional|

### Makefile

There are bunch of useful make targets so installing `make` would be great.

Some example `make` targets:
* `make deps` - Install dev dependencies
* `make start` - Start local instance of the application
* `make start-json` - Start local instance with JSON formatted logging
* `make docker-build` - Build a docker image of the application
* `make docker-run` - Spawn a cotainer of the recent version built
* `make docker` - Build & run at once

Configuration can be set via command line:
```bash
export LOG_LEVEL=DEBUG
make start-json

# Or in shorter way:
LOG_LEVEL=DEBUG make start-json
```

### API Docs

FastAPI has builtin support for API docs with Swagger (or Redoc).  
Once you `make start`, you can access the docs on `http://localhost:8000/docs`
