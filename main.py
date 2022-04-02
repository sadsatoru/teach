import DEVICES
import workshop
import receipt


def mn():
    mn_workshop = workshop.Workshop(workshop.devices)
    rs = workshop.new_application()
    mn_workshop.application.append(rs)
    mn_workshop.print_application()


mn()
