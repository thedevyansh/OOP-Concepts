import json

from config.config_manager import ConfigManager

class ConfigManagerJson(ConfigManager):
    CONFIG_FOLDER = 'config_files/'
    FILE_SUFFIX = '.json'

    def read_config(self, filename: str):
        with open(ConfigManager.CONFIG_FOLDER + filename + ConfigManagerJson.FILE_SUFFIX) as inputfile:
            try:
                config_data = json.load(inputfile)
                return config_data
            except:
                print('Seems like the file is empty. Not a problem.')

    def write_config(self, filename: str, config_data: dict):
        with open(ConfigManager.CONFIG_FOLDER + filename + ConfigManagerJson.FILE_SUFFIX, 'w') as outfile:
            json.dump(config_data, outfile)
            outfile.write('\n')