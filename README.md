# PeakTDM FileFocus

<img src="docs/images/filefocus_en_2.png" alt="Motto image." height="250" />

**The Fastest Way to Turn Test & Measurement Files Into AI‑Ready Data**

Peak Test Data Manager (PeakTDM) **FileFocus** is the fastest way to transform your scattered test and measurement files into a unified, searchable, AI-ready data platform - *without disrupting your existing toolchains*.

## Quick Start Guide

The guide helps you get started with _PeakTDM FileFocus_. 

### Requirements

_PeakTDM FileFocus_ is delivered as a Docker container and requires a working Docker runtime. 
On Windows, install Docker Desktop[^1].

Log in to the Peak Solution Docker Image Repository[^2]:

``` bash
docker login https://docker.peak-solution.de
```

ℹ️ If Docker containers cannot be used in your organization, please [contact Peak Solution](https://www.peak-solution.de/contact.html) for alternatives.

### Install and Start _PeakTDM FileFocus_

Clone or [download](https://github.com/peak-solution/filefocus/archive/refs/heads/main.zip) this repository. 
If downloaded as a ZIP, extract the archive to a local folder.

Open a terminal(cmd) and navigate to the repository folder.
Then pull the required images:
``` bash
docker compose pull
```
And start the FileFocus environment:

``` bash
docker compose up -d
```

Your _PeakTDM FileFocus_ instance is now up and running.

## Usage and Examples

### Verify the installation

By default _PeakTDM FileFocus_ runs on port 15000. 

Open: 

👉 [http://localhost:15000](http://localhost:15000)

<img src="docs/images/FileFocus_Web_UI.png" alt="FileFocus WebUI" height="250" />

You can now:

* Use **PeakTDM Test Data Workplace** for interactive data exploration

* Use **Jupyter Notebooks** for programmatic access via Python

Start _PeakTDM FileFocus_ with some **example files**:

```bash
docker compose --profile examples up -d
```
or add your own data files to the `./datafolder` in your installation directory.

### Python API

Access your data programmatically via Python using [Peak ASAM ODSBox](https://peak-solution.github.io/odsbox/) - a thin wrapper around the _PeakTDM FileFocus_ HTTP(S)-APIs.

👉 Find more Python examples in the [Data Management Learning Path](https://peak-solution.github.io/data_management_learning_path/.) 

### Configure _PeakTDM FileFocus_

Copy the `.env.example` file to `.env`, open it in a text editor and adjust the values according to your setup.

Set the `DATAFOLDER` variable to the absolute path of your data files to index your specific file location. To apply the configuration settings, **restart** the PeakTDM FileFocus environment by executing the following commands:
``` bash
docker compose down -v
```
and then
``` bash
docker compose up -d
```
⚠️ Note: Docker on Windows cannot use UNC paths directly - you need to use the cifs driver for network shares. See `.env.example` file for examples.


### Import Your Own Data Files ###

_PeakTDM FileFocus_ can deal with almost any measurement file format. In case your file format is not supported yet, you can develop your own **ExD data plugin**.

👉 Visit the [Data Management Learning Path](https://peak-solution.github.io/data_management_learning_path/exd_api/overview.html) for instructions and examples or [contact Peak Solution](https://www.peak-solution.de/contact.html).

## Licensing

Running _PeakTDM FileFocus_ requires a valid license issued by Peak Solution. 

Copy your license file into the `.\license` folder of your installation.

Need an **evaluation license**:

👉 [Contact Peak Solution](https://www.peak-solution.de/contact.html).


## Roadmap

As the fastest way to turn test & measurement files into AI‑ready data,
we are actively exploring the use of PeakTDM data with **agentic AI frameworks**. 

👉 [Read the blog](https://www.peak-solution.de/testdatamanagement/test-and-measurement-data-management-in-the-age-of-ai.html#a12690) or [contact Peak Solution](https://www.peak-solution.de/contact.html) to learn how your data can be used with Github Copilot and other agentic tools.

## Contact

For questions about _PeakTDM FileFocus_ or other Peak Solution products feel free to 

👉 [Reach out to Peak Solution](https://www.peak-solution.de/contact.html) 


## Footnotes

[^1]: You can find the Docker Desktop installation instructions on the official Docker web site: [Get Docker Documentation](https://docs.docker.com/get-docker/)


[^2]: You need login credentials for the Peak Solution Docker Image Repository. In case you don't have them, please [contact Peak Solution](https://www.peak-solution.de/contact.html)