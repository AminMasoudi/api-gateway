# api-gateway
A gateway for API Services using starlette and httpx :))

## What is API Gateway ?
an API Gateway is an entry point for API calls. So you can keep your services local and use a gateway to call them.

## How to use it??
you can use docker, or run it from source code
### Docker
1. write your settings in the settings directory and call it prod.py. it should have a format like `settings/dev.py`. check out that file.
3. run 
```
docker run -p <your-server-port>:<the-port-thst-you-defined-in-prod.py> -v ./settings/:/app/settings aminmasoudii/api-gateway
```
**Notice:** when you are using docker you should use DNS and/or hostnames like Kubernetes does or useing ip's. for internall services they start with 172.

## TODO:
- [ ] Cookies and CSRF :)
- [ ] Observations
- [ ] Add db and admin pannel
- [ ] firwall and ...
