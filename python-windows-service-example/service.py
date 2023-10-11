from time import sleep
from datetime import datetime
import sys
import servicemanager
import win32event
import win32service
import win32service
import win32serviceutil

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = 'pywinsvcexample'
    _svc_display_name_ = 'Python windows service example'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.is_alive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                             servicemanager.PYS_SERVICE_STARTED,
                             (self._svc_name_, ''))
        self.main()

    def main(self):
        while self.is_alive:
            with open('./log.log', 'w') as log:
                now = datetime.now()
                log.write(now.strftime("%H:%M:%S"))
            sleep(1)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(Service)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(Service)
