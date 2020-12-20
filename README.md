# RainWise Python API
A simple Python interface to the RainWise Public Data API for accesing current conditions and recent data of [RainWise](https://www.rainwise.com/) stations.


## Dependencies
* Python 3.7 or higher
* Pandas

## Install
Clone the git repo to a desired location. 

    git clone https://github.com/HumphreysCarter/rainwise-data-api.git
    
If you plan to utilize the config file, copy the example json to config.json, and then modify the config file match the desired parameters.

    cd rainwise-data-api
    cp config.json.example config.json

## Usage
First copy RainwiseAPI.py (and optionally config.json.example) into the working directory and import the API, `import RainwiseAPI`. All API requests will be returned as a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

### Current Conditions Request
#### Using a Configuration File

To obtain current conditions and station metadata for a station based on the config file, pass the config file path to the API:

    RainwiseAPI.GetCurrentData(config_file='/path/to/config.json')

#### Directly Passing Parameters
Alternativly, the station mac address parameter can be directly passed to the API request:

    RainwiseAPI.GetCurrentData(station_mac='FF0000000000')
    
### Recent Data Request
#### Using a Configuration File

To obtain data over the last 48 hours for a station based on the config file, pass the config file path to the API:

    RainwiseAPI.GetRecentData(config_file='/path/to/config.json')

#### Directly Passing Parameters
Alternativly, the station mac address, interval (optional, default=1), and units (optional, default='english') parameters can be directly passed to the API request:

    RainwiseAPI.GetRecentData(station_mac='FF0000000000', interval=5, units='metric')
    
## Licensing
This project is licensed under the BSD-3-Clause License. This project is not associated or endorsed by RainWise, Inc.
