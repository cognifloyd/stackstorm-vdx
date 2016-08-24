import xml.etree.ElementTree as ET
from st2tests.base import BaseActionTestCase

from interface_private_vlan_mode import interface_private_vlan_mode

__all__ = [
    'Testinterface_private_vlan_mode'
]


class MockCallback(object):
    returned_data = None

    def callback(self, call, **kwargs):
        xml_result = ET.tostring(call)
        self.returned_data = xml_result


class Testinterface_private_vlan_mode(BaseActionTestCase):
    action_cls = interface_private_vlan_mode

    def test_action(self):
        action = self.get_action_instance()
        mock_callback = MockCallback()
        kwargs = {
            'username': '',
            'name': '10/0/1',
            'int_type': 'tengigabitethernet',
            'ip': '',
            'password': '',
            'port': '22',
            'mode': 'host',
            'test': True,
            'callback': mock_callback.callback
        }

        action.run(**kwargs)

        expected_xml = """<config><interface xmlns="urn:brocade.com:mgmt:brocade-interface"><tengigabitethernet><name>10/0/1</name><switchport><mode><private-vlan><host /></private-vlan></mode></switchport></tengigabitethernet></interface></config>"""

        self.assertTrue(expected_xml, mock_callback.returned_data)
