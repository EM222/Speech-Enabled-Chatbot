from botbuilder.ai.luis import LuisApplication, LuisRecognizer
from botbuilder.core import TurnContext, ActivityHandler

class EchoBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text
        
        await turn_context.send_activity(f"You said: {user_message}")
        
class LuisBot(ActivityHandler):
    def __init__(self, app_id, app_key, endpoint):
        luis_app = LuisApplication(app_id,app_key,endpoint)
        self.recognizer = LuisRecognizer(luis_app)
        
    async def on_message_activity(self,turn_cotext: TurnContext):
        results = await self.recognizer.recognize(turn_cotext)
        intent = results.get_top_scoring_intent()
        await turn_cotext.send_activity(f"Intent[0]")