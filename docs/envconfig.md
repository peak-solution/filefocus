## Basic Configuration

Copy the `.env.example` file to `.env`, open it in a text editor and adjust the values according to your setup.
To apply the configuration settings, **restart** the *PeakTDM FileFocus* environment by executing the following commands:

``` bash
docker compose down -v
```

and then

``` bash
docker compose up -d
```

### Index Folder

Configure the absolute path of your data file's index folder. 

`DATAFOLDER=./datafolder`

⚠️ Note: Docker on Windows cannot use UNC paths directly - you need to use the cifs driver for network shares. See `.env.example` file for examples.

### License

Configure the path to the folder containing license files.
Copy your license file into the `.\license` folder of your installation.

`LICENSE_PATH=./license`

### Jupyter Notebook

Configure the Jupyter notebook access token (pasword)

`JUPYTER_TOKEN=`