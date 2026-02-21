from typing import List, Dict
from communication_protocol import ProtocolHandler

class InterfaceAnalysisModule:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.protocol_handler = ProtocolHandler()
    
    def analyze_interfaces(self, system_profiles: List[SystemProfile]) -> Dict:
        """Analyze interfaces of given systems and return compatibility details."""
        try:
            interface_map = {}
            
            for profile in system_profiles:
                interfaces = self._get_system_interfaces(profile)
                interface_map[profile.id] = {
                    'interfaces': interfaces,
                    'compatibility': self._determine_compatibility(interfaces)
                }
            
            return interface_map
            
        except Exception as e:
            self.logger.error(f"Interface analysis failed: {str(e)}")
            raise
    
    def _get_system_interfaces(self, system_profile: SystemProfile) -> List[str]:
        """Retrieve available interfaces for a given system."""
        try:
            # Simplified interface retrieval
            return [interface.name for interface in system_profile.interfaces]
        
        except Exception as e:
            self.logger.error(f"Failed to get interfaces for {system_profile.id}: {str(e)}")
            raise
    
    def _determine_compatibility(self, interfaces: List[str]) -> Dict:
        """Determine compatibility between interfaces."""
        try:
            compatibility = {}
            
            for interface in interfaces:
                compatible_interfaces = self.protocol_handler.check_compatibility(interface)
                compatibility[interface] = compatible_interfaces
            
            return compatibility
        except Exception as e:
            self.logger.error(f"Compatibility check failed: {str(e)}")
            raise

# Example usage:
if __name__ == "__main__":
    iam = InterfaceAnalysisModule()
    systems = [...]  # List of SystemProfile instances
    interface_data = iam.analyze_interfaces(systems)
    
    for system_id, data in interface_data.items():
        print(f"System {system_id}: Interfaces - {data['interfaces']}, Compatibility - {data['compatibility']}")