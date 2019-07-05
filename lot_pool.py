import json
from Settings import settings
import random
import os

class LotPool():
    def __init__(self):
        self.lots = []
        self.history = []
        self.running = False
        self.i = 0
        if os.path.exists(str(settings['lotsDir'])):
            with open(settings['lotsDir'],'r') as f:
                self.lots = json.load(f)
        else:
            with open('lots.json','wb') as f:
                f.write(json.dumps(self.lots, indent=4).encode('utf-8'))
            settings['lotsDir'] = 'lots.json'
        settings['lotCount'] = len(self.lots)
        if settings['historyLen'] < 1 or settings['historyLen'] > settings['lotCount']:
            settings['historyLen'] = 1 if len(self.lots)<=15 else 10
        for x in range(settings['historyLen']):
            self.history.append(None)

    def getLotPool(self):
        text = ''
        for lot in self.lots:
            text = "%s%s\n"%(text, lot)
        return text

    def setLotPool(self, text):
        self.lots.clear()
        self.lots.extend(text.splitlines())
        while '' in self.lots:
            self.lots.remove('')
        while '\n' in self.lots:
            self.lots.remove('\n')
        self.history.clear()
        settings['historyLen'] = 1 if len(self.lots)<=15 else 10
        for x in range(settings['historyLen']):
            self.history.append(None)
        with open(settings['lotsDir'],'wb') as f:
            f.write(json.dumps(self.lots, indent=4).encode('utf-8'))
        settings['lotCount'] = len(self.lots)
        settings.Save()
        self.i = 0

    def drawLot(self):
        if len(self.lots) > 0:
            result = random.choice(self.lots)
            if settings['historyLen'] != 0:
                while result in self.history:
                    result = random.choice(self.lots)
                del self.history[settings['historyLen']-1]
                self.history.insert(0, result)
        else:
            result = '签池不能为空!'
        return result

    def setHistory(self):
        self.history.clear()
        for x in range(settings['historyLen']):
            self.history.append(None)
        self.i = 0

    def next(self):
        if settings['lotcount'] != 0:
            result = self.lots[self.i]
            self.i += 1
            if self.i == settings['lotcount']:
                self.i = 0
        else:
            result = '签池不能为空!'
        return result


lotPool = LotPool()