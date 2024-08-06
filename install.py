# installer for the forecast extension
# Copyright 2014-2020 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return ForecastInstaller()

class ForecastInstaller(ExtensionInstaller):
    def __init__(self):
        super(ForecastInstaller, self).__init__(
            version="3.6",
            name='forecast',
            description='Generate and display weather and tide forecasts.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            archive_services=['user.forecast.ZambrettiForecast',
                              'user.forecast.NWSForecast',
                              'user.forecast.WUForecast',
                              'user.forecast.OWMForecast',
                              'user.forecast.UKMOForecast',
                              'user.forecast.AerisForecast',
                              'user.forecast.WWOForecast',
                              'user.forecast.DSForecast',
                              'user.forecast.XTideForecast',
                              'user.forecast.IcelandicMetForecast'], 
            config={
                'Forecast': {
                    'data_binding': 'forecast_binding',
                    'XTide': {'location': 'INSERT_LOCATION_HERE'},
                    'Zambretti': {'hemisphere': 'NORTH'},
                    'NWS': {'lid': 'INSERT_LOCATION_ID_HERE', 'foid': 'INSERT_FORECAST_OFFICE_ID_HERE'},
                    'WU': {'api_key': 'INSERT_WU_API_KEY_HERE'},
                    'OWM': {'api_key': 'INSERT_OWM_API_KEY_HERE'},
                    'UKMO': {'api_key': 'INSERT_UKMO_API_KEY_HERE', 'location': 'INSERT_UK_LOCATION_HERE'},
                    'Aeris': {'client_id': 'INSERT_AERIS_CLIENT_ID_HERE', 'client_secret': 'INSERT_AERIS_CLIENT_SECRET_HERE'},
                    'WWO': {'api_key': 'INSERT_WWO_API_KEY_HERE'},
                    'DS': {'api_key': 'INSERT_DS_API_KEY_HERE'},
                    'IcelandicMet': {'station_id': '6300'}  # Ensure this matches the default or is set by the user
                },
                'DataBindings': {
                    'forecast_binding': {
                        'manager': 'weewx.manager.Manager',
                        'schema': 'user.forecast.schema',
                        'table_name': 'archive',
                        'database': 'forecast_sqlite'
                    }
                },
                'Databases': {
                    'forecast_sqlite': {
                        'database_name': 'forecast.sdb',
                        'database_type': 'SQLite'
                    }
                },
                'StdReport': {
                    'forecast': {
                        'skin': 'forecast',
                        'HTML_ROOT': 'forecast'
                    }
                }
            },
            files=[('bin/user', ['bin/user/forecast.py']),
                   ('skins/forecast', [
                       'skins/forecast/skin.conf',
                       'skins/forecast/index.html.tmpl',
                       'skins/forecast/forecast.css'
                       # More files as in the original script
                   ]),
                   ('skins/forecast/icons', [
                       'skins/forecast/icons/CL.png',
                       # More icons as in the original script
                   ])
            ]
        )
