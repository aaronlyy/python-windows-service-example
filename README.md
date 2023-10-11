# python-windows-service-example
Example on how to create a windows service with python

# Install

- Install pywin32 (```pip install pywin32```)
- Run pywin32 post-install script
- Install service (```py service.py install```)
- Start service (```net start pywinsvcexample```)

# Uninstall

- Stop service (```net stop pywinsvcexample```)
- Remove service (```py service.py remove```)