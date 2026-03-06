## Uninstall *PeakTDM FileFocus*

The *PeakTDM FileFocus* installation comprise of three components:
* Docker environment
* *PeakTDM FileFocus* docker container
* Files on your disk

To uninstall *PeakTDM FileFocus* follow these steps

### 1 Uninstall *PeakTDM FileFocus* docker container

To "uninstall" the containers of *PeakTDM FileFocus* use the following command:

``` bash
docker compose down -v
```

In case of installed examples also use

``` bash
docker compose --profile examples down example-data
```

Now all containers used by *PeakTDM FileFocus* are uninstalled from your computer.

You can double-check by open Docker Desktop and look for *PeakTDM FileFocus* containers. In case containers are still left, you can delete them manually.

### 2 Uninstall Docker Desktop

Use Windows to uninstall Docker Desktop. Follow the Windows instruction how to [Uninstall or remove apps and programs in Windwows](https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98). 

### 3 Delete local files

After uninstallation you can delete files left over in

* C:\Users\<username>\.docker
* C:\Users\<username>\AppData\Local\Docker*