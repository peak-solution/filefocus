## Quick Start Guide

The guide helps you get started with *PeakTDM FileFocus*.

### Install and Start *PeakTDM FileFocus*

Clone or [download](https://github.com/peak-solution/filefocus/archive/refs/heads/main.zip) this repository.
If downloaded as a ZIP, extract the archive to a local folder.

Open a terminal(cmd) and navigate to the repository folder and start the FileFocus environment:

``` bash
docker compose up -d
```

Your *PeakTDM FileFocus* instance is now up and running.

### Verify the installation

By default *PeakTDM FileFocus* runs on port 15000.

Copy the following URL into your browser to access the *PeakTDM FileFocus* Web UI:

👉 http://localhost:15000


### Adding Example Files

Example files are in an own container and can be installed using the following commmand

```bash
docker compose --profile examples up example-data
docker compose --profile examples down example-data
```

or copy your own data files to the `./datafolder` in your installation directory.

### Specify your Index Location

Copy the `.env.example` file to `.env`, open it in a text editor and adjust the values according to your setup.

Set the `DATAFOLDER` variable to the absolute path of your data files to index your specific file location. To apply the configuration settings, **restart** the *PeakTDM FileFocus* environment by executing the following commands:

``` bash
docker compose down -v
```

and then

``` bash
docker compose up -d
```

⚠️ Note: Docker on Windows cannot use UNC paths directly - you need to use the cifs driver for network shares. See `.env.example` file for examples.

### Import Your Own Data Files

*PeakTDM FileFocus* can deal with almost any measurement file format. In case your file format is not supported yet, you can develop your own **ExD data plugin**.

👉 Visit the [Data Management Learning Path](https://peak-solution.github.io/data_management_learning_path/exd_api/overview.html) for instructions and examples or [contact Peak Solution](https://www.peak-solution.de/contact.html).

### Python API

Access your data programmatically via Python using [Peak ASAM ODSBox](https://peak-solution.github.io/odsbox/) - a thin wrapper around the *PeakTDM FileFocus* HTTP(S)-APIs.

👉 Find more Python examples in the [Data Management Learning Path](https://peak-solution.github.io/data_management_learning_path/.)

