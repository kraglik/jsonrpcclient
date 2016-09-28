from .client import Client

class WebSocketsClient(Client):
    def __init__(self, ws):
        self.ws = ws

    async def _send_message(self, request, **kwargs):
        await self.ws.send(request)
        response = await self.ws.recv()
        return self._process_response(response)
