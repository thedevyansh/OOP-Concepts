from config.config_manager_json import ConfigManagerJson

config_manager = ConfigManagerJson()

def store_mysql_config(mysql_config):
    print('Storing mysql config of inventory team')
    config_manager.write_config('inventory_mysql_config', mysql_config)


def read_mysql_config():
    print('Reading mysql config of inventory team')
    mysql_config = config_manager.read_config('inventory_mysql_config')
    return mysql_config

