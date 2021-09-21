
# GUIDELINES FOR OPERATORS

## Creating the environment and Installing required packages

The file **gee_lc_requirement.txt** consists of all the packages required for using the Lancover generation code. Create a virtual environment and install the packages using the following code:

```
conda config --append channels conda-forge
conda create --name <environment_name> --file gee_lc_requirement.txt
```

All the packages can be installed using '**conda**'.

***

Use the provided credential files for authenticating different platform. Ensure the name of the file is **glodal_gee.json**.

If you haven't received the credential file, feel free to reach out [Rohit Khati](mailto:rhtkhati@gmail.com).

***
Before jumping to generate landcover map, modify the configuration parameters as per the requirement at [Config.py](https://github.com/ro-hit81/Landcover_GEE/blob/main/py/Config.py) file.

![Params to be changed.](https://github.com/ro-hit81/Landcover_GEE/blob/main/images/parameters_to_be_modified.png)

***
Once the configuration file is setup, the Internt python notebook (.ipynb) is ready to run. When the run is completed, the outputs are stored in Google Cloud & Remote/Local computer.

 The outputs in remote/ local computer can be obatained in a directory with user's name. The directory consists of following files:

- False Color Composite Image of Region of Interest. **(/fc-map)**
- Json files with image metedata information. **(/json)**
- Generated Landcover Map of Region of Interest. **(/lc-map)**
- Trained Best Model in .h5 format. **(/model)**

***
