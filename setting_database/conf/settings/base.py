import configparser
import pathlib

BASE_PATH = pathlib.Path(__file__).resolve().parent  # Đường dẫn tới thư mục chứa tệp mã nguồn
CONFIG_PATH = BASE_PATH / "config.ini"  # Đường dẫn tới tệp config.ini

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

DATABASE = {
    'USERNAME': config['database']['username'],
    'PASSWORD': config['database']['password'],
    'HOST': config['database']['host'],
    'PORT': config['database']['port'],
    'NAME': config['database']['name'],
}
