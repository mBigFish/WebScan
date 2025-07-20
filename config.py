import configparser
import os


# 操作config类
class MyConfig:
    def __init__(self, path="config.ini"):
        # 创建一个ConfigParser对象
        self.path = path
        self.config = configparser.ConfigParser()
        # 禁用自动转换为小写
        self.config.optionxform = str
        # 读取配置文件
        # self.config.read('con.ini')
        # 指定文件编码并读取配置
        with open(self.path, encoding='utf-8') as f:
            self.config.read_file(f)

    # 获取keys
    def get_config(self, section):
        keys_dict = {}
        # 访问配置文件中的key
        keys = self.config[section]
        for key in keys:
            keys_dict[key] = keys[key]
        return keys_dict

    # 修改flags
    def change_config(self, section, change_dict):
        # 检查并修改 [flag] 部分
        for key in change_dict:
            print(change_dict[key])
            self.config[section][key] = str(change_dict[key])
        with open(self.path, 'w', encoding="utf-8") as configfile:
            self.config.write(configfile)


if __name__ == '__main__':
    m = {'ALLOW_REDIRECT': True, 'VERITY': True, 'TIMEOUT': False, 'TRYAGAIN': True}

    a = MyConfig()
    b = a.get_config("web_content")
    # a.change_bool("requests", m)
    print(b)