class HdmiConnectableMixin:
    def connect_to_device_via_hdmi_cable(self, device):
        return f"{device} connected successful to the HDMI_CABLE"


class RcaConnectableMixin:
    def connect_to_device_via_rca_cable(self, device):
        return f"{device} connected successful to the RCA_CABLE"


class EthernetConnectableMixin:
    def connect_to_device_via_ethernet_cable(self, device):
        return f"{device} connected successful to the ETHERNET_CABLE"


class PowerOutletConnectableMixin:
    def connect_device_to_power_outlet(self, device):
        return f"{device} connected successful to the POWER_OTULET"


class EntertainmentDevice(PowerOutletConnectableMixin):
    pass


class Television(EntertainmentDevice, RcaConnectableMixin, HdmiConnectableMixin):
    def connect_to_dvd(self, dvd_player):
        return self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, HdmiConnectableMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HdmiConnectableMixin, EthernetConnectableMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        return self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetConnectableMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)
