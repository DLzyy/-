import configparser as cp
import os

class Config():
    def __init__(self):
        self.config = cp.ConfigParser()
        if os.path.exists('Config.ini'):
            self.config.read('Config.ini', 'UTF_8')
        else:
            with open('Config.ini', 'w') as f:
                f.write('[drawlots]\n')
            self.config.read('Config.ini', 'UTF_8')
            self.config['drawlots']['greeting'] = "Good Luck"
            self.config['drawlots']['drawState'] = '抽取'
            self.config['drawlots']['lotCount'] = '0'
            self.config['drawlots']['historyLen'] = '1'
            self.config['drawlots']['lotsDir'] = "lots.json"
            self.Save()

    def Save(self):
        with open('Config.ini', 'w') as f:
            self.config.write(f)

    def __getitem__(self, key):
        result = self.config['drawlots'][key]
        try:
            result = int(result)
        except:
            pass
        return result
    
    def __setitem__(self, key, value):
        self.config['drawlots'][key] = str(value)

settings = Config()


