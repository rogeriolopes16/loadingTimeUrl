from modules.sendEmail import *

sd = SendEmail()

class FailureControl():
    def __init__(self):
        pass

    def failureCleaner(self,system):
        control = open('C:/Automations/loadingTimeUrl/control/countFails.txt', 'r').readlines()
        list_control = []

        for n in control:
            if system == (n[:n.find('=')]).strip() and int((n[n.find('=') + 1:]).strip()) > 0:
                system = (n[:n.find('=')]).strip()
                key = (system+'=0\n')
                list_control.append(key)
            else:
                list_control.append(n.rstrip()+"\n")

        log = open('C:/Automations/loadingTimeUrl/control/countFails.txt', 'w')
        for n in list_control:
            log.writelines(n)
        log.close()

    def failureCounter(self,system):
        control = open('C:/Automations/loadingTimeUrl/control/countFails.txt', 'r').readlines()
        list_control = []

        for n in control:
            if system == (n[:n.find('=')]).strip():
                system = (n[:n.find('=')]).strip()
                count = int((n[n.find('=') + 1:]).strip())
                count = 1 if count == 12 else count + 1
                key = (system+'='+str(count))
                list_control.append(key+"\n")
            else:
                list_control.append(n.rstrip()+"\n")

        log = open('C:/Automations/loadingTimeUrl/control/countFails.txt', 'w')
        for n in list_control:
            log.writelines(n)
        log.close()

    def failureSender(self):
        control = open('C:/Automations/loadingTimeUrl/control/countFails.txt', 'r').readlines()
        for n in control:
            if int((n[n.find('=') + 1:]).strip()) == 1:
                system = (n[:n.find('=')]).strip()
                sd.sendEmail(system)
