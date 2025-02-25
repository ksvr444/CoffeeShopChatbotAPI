# This help to make the code more readable and follow coding rules

from typing import Protocol, List, Dict, Any

class AgentProtocol(Protocol):
    def get_response(self, messages:List[Dict[str, Any]]) -> Dict[str,Any]:
        
        pass