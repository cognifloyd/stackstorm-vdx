"""Generated test for checking pynos based actions
"""
import xml.etree.ElementTree as ET
from st2tests.base import BaseActionTestCase
from snmp_del_snmp_host import snmp_del_snmp_host

__all__ = [
    'TestSnmpDelSnmpHost'
]


class MockCallback(object):  # pylint:disable=too-few-public-methods
    """Class to hold mock callback and result
    """
    returned_data = None

    def callback(self, call, **kwargs):  # pylint:disable=unused-argument
        """Mock callback method
        """
        xml_result = ET.tostring(call)
        self.returned_data = xml_result


class TestSnmpDelSnmpHost(BaseActionTestCase):
    """Test holder class
    """
    action_cls = snmp_del_snmp_host

    def test_action(self):
        """Generated test to check action
        """
        action = self.get_action_instance()
        mock_callback = MockCallback()
        kwargs = {
            'username': '',
            'host_info': ['10.0.2.1', '135'],
            'ip': '',
            'password': '',
            'port': '22',
            'community': 'test',
            'test': True,
            'callback': mock_callback.callback
        }

        action.run(**kwargs)

        expected_xml = (
            '<config><snmp-server xmlns="urn:brocade.com:mgmt:brocade-snmp"><h'
            'ost operation="delete"><ip>10.0.2.1</ip><community>test</communit'
            'y><udp-port>135</udp-port></host></snmp-server></config>'
        )

        self.assertTrue(expected_xml, mock_callback.returned_data)
