from agents import (GuardAgent, ClassificatonAgent, DetailsAgent, AgentProtocol, RecommendationAgent, OrderTakingAgent)
import os
from typing import Dict
import sys

import pathlib
folder_path = pathlib.Path(__file__).parent.resolve()

class AgentController():
    def __init__(self):
        self.guard_agent = GuardAgent()
        self.classification_agent = ClassificatonAgent()
        self.recommendation_agent = RecommendationAgent(
                os.path.join(folder_path, "recommendation_objects/apriori_recommendations.json"),
                os.path.join(folder_path, "recommendation_objects/popularity_recommencation.csv")
            )
        self.agent_dict: Dict[str, AgentProtocol] = {
            'details_agent': DetailsAgent(),
            'recommendation_agent': self.recommendation_agent,
            'order_taking_agent': OrderTakingAgent(self.recommendation_agent)

        }

    
    def get_response(self, input):

        #extract user input\
        #structure
        # {
        #     "Input" : {"messages"}
        # }

        job_input = input["input"]
        messages = job_input['messages']

        # Get Guard Agent's response
        guard_agent_response = self.guard_agent.get_response(messages)
        print("GUARD AGENT OUTPUT: ", guard_agent_response)
        if guard_agent_response['memory']['guard_decision'] == 'not allowed':
            messages.append(guard_agent_response)
            return guard_agent_response
        
        # Get Classification Agent's response
        classification_agent_response = self.classification_agent.get_response(messages)
        print("CLASSIFICATOIN AGENT OUTPUT: ", classification_agent_response)
        chosen_agent = classification_agent_response['memory']['classification_decision']
        
        #Get the chosen agent's response
        agent = self.agent_dict[chosen_agent]
        response = agent.get_response(messages)

        return response

