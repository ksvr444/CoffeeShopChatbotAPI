from openai import OpenAI
import os
from .utils import get_chatbot_response, double_check_json_output
from copy import deepcopy
import dotenv
import json

dotenv.load_dotenv()


class GuardAgent():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("RUNPOD_TOKEN"),
            base_url=os.getenv("RUNPOD_CHATBOT_URL")
        
        )
        self.model_name = os.getenv('MODEL_NAME')

    def get_response(self, messages):
        messages = deepcopy(messages)

        system_prompt="""
                You are a helpful AI assistant for a coffee shop applicaton which serves drinks and pastreis.
                Your task is to determine whether the user is asking something relevant to the coffee shop or not.

                The user is allowed to:
                1. Ask questions about the coffee shop, like location ,working hours, menu items and coffee shop related questions.
                2. Ask questions about menu items ,they can ask for ingredients in a n item and more details about the item.
                3. Make an order.
                4. Ask about recommendations of what to buy.

                The user is not allowerd to:
                1. Ask questions about anything else other than our coffee shop.
                2. Ask question about the staff or how to make a certain menu  item.

                Your output should be in a structured json format like so. each key is a string and each value is a string. Make sure to allow the format exactly:
                {
                    "chain of thought": "go over each of the points and see if the message lies under this point or not. The you write some thoughts about what point is this input relevant to.",
                    "decision": "allowed" or "not allowed" . Pick one of those and only write the word.,
                    "message": leave the message empty "" if it's allowed, otherwise write "Sorry, I can't help with that. Can I help you with your order?"

                }

            """
        input_messages = [{"role": "system", "content":system_prompt}] + messages[-3:]

        chatbot_output = get_chatbot_response(self.client, self.model_name, input_messages)
        chatbot_output = double_check_json_output(self.client, self.model_name, chatbot_output)
        output = self.postprocess(chatbot_output)

        return output
    
    def postprocess(self, output):
        
        output = json.loads(output)
        # agents have memory to what steps to go to next based on previous chat
        # essential part of agent is memory
        dict_output = {
            "role": "assistant",
            "content": output['message'],
            "memory": {
                "agent": "guard_agent",
                "guard_decision": output["decision"]
            }
        }

        return dict_output
    
