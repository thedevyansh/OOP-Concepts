from config.config_manager_xml import ConfigManagerXml

config_manager = ConfigManagerXml()

def store_mysql_config(mysql_config):
    print('Storing mysql config of logistics team')
    config_manager.write_config('logistics_mysql_config', mysql_config)


def store_logistics_rest_server_config(rest_server_config):
    print('Storing rest_server config of logistics team')
    config_manager.write_config('logistics_rest_server', rest_server_config)


def read_mysql_config():
    print('Reading mysql config of logistics team')
    mysql_config = config_manager.read_config('logistics_mysql_config')
    return mysql_config


def read_logistics_rest_server_config():
    print('Reading rest_server config of logistics team')
    rest_server_config = config_manager.read_config('logistics_rest_server')
    return rest_server_config
