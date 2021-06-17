
# GUIDELINES FOR OPERATORS

## Creating the environment and Installing required packages

The file **gee_lc_reqmnt.txt** consists of all the packages required for using the Lancover generation code. Create a virtual environment and install the packages using the following code:

```conda create --name <environment_name> --file gee_lc_reqmnt.txt```

All the packages can be installed using '**conda**'.

***

Use the provided credential files for authenticating different platform. Ensure the name of the file is **glodal_gee.json**. 

If you haven't received the credential file, feel free to reach out [Rohit Khati](mailto:rhtkhati@gmail.com).

***
Before jumping to generate landcover map, modify the configuration parameters as per the requirement at [Config.py](https://github.com/ro-hit81/Landcover_GEE/blob/main/py/Config.py) file.

![Params to be changed.](https://github.com/ro-hit81/Landcover_GEE/blob/main/images/parameters_to_be_modified.png)

***