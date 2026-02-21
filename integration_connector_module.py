from typing import Any
from connector_template import ConnectorTemplate

class IntegrationConnector:
    def __init__(self, system_a: str, system_b: str):
        self.logger = logging.getLogger(__name__)
        self.connector = ConnectorTemplate(system_a, system_b)
    
    def establish_connection(self) -> bool:
        """Establish a connection between two systems."""
        try:
            success = self.connector.initialize()
            if not success:
                raise ConnectionError(f"Failed to connect {self.connector.system_a} and {self.connector.system_b}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Connection failed: {str(e)}")
            return False
    
    def handle_communication(self, data: Dict) -> Any:
        """Handle communication between connected systems."""
        try:
            response = self.connector.send_data(data)
            return response
        except Exception as e:
            self.logger.error(f"Communication error: {str(e)}")
            raise
    
    def disconnect(self) -> bool:
        """Safely disconnect the integrated systems."""
        try:
            success = self.connector.shutdown()
            if not success:
                raise