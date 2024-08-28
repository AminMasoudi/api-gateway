from abc import ABC, abstractmethod
import httpx


class AbstractClient(ABC):
    @abstractmethod
    async def send_request(
            self,
            service,
            path,
            protocol:str="http",
            follow_redirects = True,
            **data
            ):
            
        ...

class HttpxClient(AbstractClient):

    async def send_request(
            self,
            service,
            path,
            protocol:str="http",
            follow_redirects = False,
            **data
            ):
            
        url = protocol + "://" + service + path
        headers = None
        try:
            async with httpx.AsyncClient() as Client:
                response = await Client.request(
                    **data,
                    follow_redirects=follow_redirects,
                    url=url,
                    )
            content, code = response.content, response.status_code
            headers = response.headers
        except httpx.ConnectError:
            code = httpx.codes.SERVICE_UNAVAILABLE
            content = "Service Unavailable"
            
        except Exception as e:
            print(e)            #TODO: logger
            code, content = 500, "Oops!! Something went wrong."

        return (content, code, headers)
    

class MockClient(AbstractClient):
    requests: list = []
    async def send_request(
            self,
            service,
            path,
            protocol:str="http",
            follow_redirects = True,
            **data
            ):
        self.requests.append({
            "service": service,
            "path": path,
            "protocol": protocol,
            "follow_redirects": follow_redirects,
            **data
        })
        return ("mock", 200, data["headers"] or {})