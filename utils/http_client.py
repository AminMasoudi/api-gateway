from abc import ABC, abstractmethod
import httpx


class AbstractClient(ABC):
    async def send_request(
            self,
            service: str,
            path: str,
            protocol:str
            ):
        ...

class HttpxClient(AbstractClient):

    async def send_request(
            self,
            service,
            path,
            protocol:str="http",
            follow_redirects = True,
            **data
            ):
            
        url = protocol + "://" + service + path

        try:
            async with httpx.AsyncClient() as Client:
                response = await Client.request(
                    **data,
                    follow_redirects=follow_redirects,
                    url=url,
                    )
            content, code = response.content, response.status_code

        except httpx.ConnectError:
            code = httpx.codes.SERVICE_UNAVAILABLE
            content = "Service Unavailable"
            
        except Exception as e:
            print(e)            #TODO: logger
            code, content = 500, "Oops!! Something went wrong."

        return (content, code)