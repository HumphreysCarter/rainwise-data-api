import json
import pandas as pd

def load_config(path='config.json'):
    """
    Loads configruation from config.json file. 
    Returns station mac address, interval, and units for data request
    """
    # Open config JSON
    with open(path) as f:
        # Load JSON file to dictionary
        config = json.load(f)
        
        # Return mac address, interval, and units
        return (config['station_max_address'], int(config['interval']), config['units'])
    
    
def build_data_request(mac, interval=1, units='english'):
    """
    Creates RainWise API request for Recent Data based on station mac, format (optional), and units (optional)
    """
    # Check if interval requested is valid interval
    if interval not in [1, 5, 10, 15, 30, 60]:
        raise ValueError('Invalid Request: Parameter interval must be 1, 5, 10, 15, 30, or 60')
    
    # Check if units requested are valid units
    if units.lower() not in ['english', 'metric']:
        raise ValueError('Invalid Request: Parameter units must be english or metric')
    
    # Build request URL
    request_url = f'http://api.rainwise.net/main/v1.4/get-recent.php?mac={mac}&interval={interval}&units={units}&format=json'
    
    return request_url

def GetRecentData(config_file=None, station_mac=None, interval=1, units='english'):
    """
    Makes request to RainWise API to get most recent data over the last 48 hours based on config file specifications, 
    or station ID, interval (optional) and units (optional). Specifying a config file will override and parms passed.
    """
    # Load configruation
    if config_file != None:
        station_mac, interval, units = load_config(config_file)
    elif station_mac == None and config_file == None:
        raise ValueError('Either config file or station mac address must be passed')
    
    # Get data API URL
    data_url = build_data_request(station_mac, interval, units)
    
    # Return station data as Pandas DataFrame
    return pd.read_json(data_url)