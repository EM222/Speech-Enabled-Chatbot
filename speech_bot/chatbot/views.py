from django.shortcuts import render
from django.http import JsonResponse
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from .bot_logic import EchoBot

# Create your views here.
bot_settings = BotFrameworkAdapterSettings(app_id="BOT_APP_ID", app_password="BOT_APP_PASSWORD")
bot_adapter = BotFrameworkAdapter(bot_settings)
bot = EchoBot()

async def messages(request):
    if request.method == "POST":
        body = await request.body.decode(utf-8)
        auth_header = request.headeers.get("Authorization", "")
        activity = json.loads(body)
        
        response = await bot_adapter.process_activity(activity, auth_header, bot.on_turn)
        return JsonResponse(response)