"""Generated test for checking pynos based actions
"""
import xml.etree.ElementTree as ET
from st2tests.base import BaseActionTestCase
from bgp_update_source import bgp_update_source

__all__ = [
    'TestBgpUpdateSource'
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


class TestBgpUpdateSource(BaseActionTestCase):
    """Test holder class
    """
    action_cls = bgp_update_source

    def test_action(self):
        """Generated test to check action
        """
        action = self.get_action_instance()
        mock_callback = MockCallback()
        kwargs = {
            'username': '',
            'int_name': '1',
            'neighbor': '10.2.1.4',
            'get': False,
            'ip': '',
            'vrf': 'test',
            'int_type': 'tengigabitethernet',
            'password': '',
            'port': '22',
            'rbridge_id': '224',
            'test': True,
            'callback': mock_callback.callback
        }

        action.run(**kwargs)

        expected_xml = (
            '<config><rbridge-id xmlns="urn:brocade.com:mgmt:brocade-rbridge">'
            '<rbridge-id>224</rbridge-id><router><bgp xmlns="urn:brocade.com:m'
            'gmt:brocade-bgp"><vrf-name>test</vrf-name><router-bgp-cmds-holder'
            '><router-bgp-attributes><neighbor-ips><neighbor-addr><router-bgp-'
            'neighbor-address>10.2.1.4</router-bgp-neighbor-address><update-so'
            'urce><loopback>1</loopback></update-source></neighbor-addr></neig'
            'hbor-ips></router-bgp-attributes></router-bgp-cmds-holder></bgp><'
            '/router></rbridge-id></config>'
        )

        self.assertTrue(expected_xml, mock_callback.returned_data)
