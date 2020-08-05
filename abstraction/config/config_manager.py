import os
import abc

class ConfigManager(metaclass=abc.ABCMeta):
    CONFIG_FOLDER = 'config_files/'

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read_config') and
                callable(subclass.read_config) and
                hasattr(subclass, 'write_config') and
                callable(subclass.write_config) or
                NotImplemented)

    @abc.abstractmethod
    def read_config(self, filename: str):
        print('Abstract method: Not implemented')
        raise NotImplementedError

    @abc.abstractmethod
    def write_config(self, filename: str, config_data: dict):
        print('Abstract method: Not implemented')
        raise NotImplementedError


try:
    os.stat(ConfigManager.CONFIG_FOLDER)
except:
    os.mkdir(ConfigManager.CONFIG_FOLDER)