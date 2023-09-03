''' WEBSOCKET CONSUMERS '''
from urllib.parse import parse_qs
from django.core.exceptions import ObjectDoesNotExist

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

class WSConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

        message_text = self.scope["query_string"]
        parameters = parse_qs(message_text)
        token = None
        if message_text == '':
            await self.send_json({"close": True})
            await self.close()
            raise ValueError("Missing text field. Closing channel")

        if b'token' in parameters:
            token = parameters[b'token'][0].decode("utf-8")
        else:
            await self.send_json({"close": True})
            await self.close()
            raise ValueError("Missing token field. Closing channel.")

        # Import here because djanngo app not loaded a this moment
        access_token = await get_token(token)
        if access_token is None:
            await self.send_json({
                "close": True,
                "text": "Token error"
            })
            await self.close()
            raise ValueError("Invalid token provided. Closing channel")

        user = access_token.user
        self.user = user
        # Join his own room group
        await self.channel_layer.group_add(
            user.username,
            self.channel_name
        )
        await self.send_json({
            "text": next(x[1].decode("utf-8") for x in self.scope["headers"] if x[0] == b"sec-websocket-key")
        })

    async def disconnect(self, message):
        self.close()
        print(self.user.username + ' disconnected')
        await self.channel_layer.group_discard(
            self.user.username,
            self.channel_name
        )
        if getattr(self, 'channel_group', None):
            print(f'{self.user.username} quiting project {self.channel_group}')
            await self.channel_layer.group_discard(
                self.channel_group,
                self.channel_name
            )

    async def receive(self, text_data):
        if getattr(self, 'channel_group', None):
            await self.channel_layer.group_discard(
                self.channel_group,
                self.channel_name
            )
            print(self.user.username + ' quitting ' + self.channel_group)
            self.channel_group = text_data
        else:
            self.channel_group = text_data

        # Define the group to listen
        await self.channel_layer.group_add(
            self.channel_group,
            self.channel_name
        )
        print(self.user.username + ' listenning to ' + text_data)

    async def message(self, event):
        await self.send_json(event["text"])


@database_sync_to_async
def get_token(token):
    from oauth2_provider.models import AccessToken
    try:
        access_token = AccessToken.objects.prefetch_related('user').get(token=token)
        return access_token
    except ObjectDoesNotExist:
        return None
