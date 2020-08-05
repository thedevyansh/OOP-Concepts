from config.config_manager_json import ConfigManagerJson

config_manager = ConfigManagerJson()

def store_mysql_config(mysql_config):
    print('Storing mysql config of vendor management team')
    config_manager.write_config('vendor_mysql_config', mysql_config)


def store_resolv_config(resolv_config):
    print('Storing resolv config of all vendor management servers')
    config_manager.write_config('vendor_server_resolv_config', resolv_config)


def read_mysql_config():
    print('Reading mysql config of vendor management team')
    mysql_config = config_manager.read_config('vendor_mysql_config')
    return mysql_config


def read_resolv_config():
    print('Reading resolv config vendor management servers')
    resolv_config = config_manager.read_config('vendor_server_resolv_config')
    return resolv_config
