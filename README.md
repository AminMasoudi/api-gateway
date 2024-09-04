# api-gateway
a gateway for api's :))

## What is api-gateway ??
an api gateway is an entry point for API calls. so you can keep your services local and use a gateway to call them 

## How to use ??
you can use docker, or run it from source code
### Docker
1. write your settings in settings directory and call it prod.py. it shoud has a format like `settings/dev.py`. check out that file.
3. run 
```
docker run -p 8000:8000 -v ./settings/:/app/settings aminmasoudii/api-gateway
```
## TODO:
- [ ] some debug for Docker image
- [ ] observations
- [ ] add db and admin pannel
- [ ] firwall and ...
