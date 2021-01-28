from pynos import device
from st2common.runners.base_action import Action


class interface_del_vlan_int(Action):
    def run(self, **kwargs):
        conn = (str(kwargs.pop('ip')), str(kwargs.pop('port')))
        auth = (str(kwargs.pop('username')), str(kwargs.pop('password')))
        test = kwargs.pop('test', False)
        callback = kwargs.pop('callback', None)
        with device.Device(
            conn=conn, auth=auth,
            test=test,
            callback=callback
        ) as dev:
            # pylint: disable=no-member
            dev.interface.del_vlan_int(**kwargs)
        return 0
