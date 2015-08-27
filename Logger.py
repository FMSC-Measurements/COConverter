'''
Created on Jul 14, 2011

@author: benjaminjcampbell
'''


class Logger(object):
    __instance = None
    
    class __impl():
        def __init__(self):
            self.messageLog = []
            self.levels = {'high':1, 'norm':2, 'low':3, 'verbose':4}
        
        def lg(self, level, message):
            self.messageLog.append((self.levels[level], message))
            if self.levels[level] <= 2 : #print all incoming messages above 'norm'
                print(message)
                
               
        def display(self, level):
            #level = self.levels[level]
            for message in self.messageLog:
                l, m = message
                if l <= self.levels[level]:
                    print m
                    
        def dump(self, level, path):
            file = open(path, 'w')
            
            for message in self.messageLog:
                l, m = message
                if l <= self.levels[level]:
                    file.write(m + '\n')
                    
            file.close()
        
    
    def __init__(self):
        if Logger.__instance is None:
            Logger.__instance = Logger.__impl()
        self.__dict__['_Logger__instance'] = Logger.__instance
    
    def __getattr__(self,attr):
        return getattr(self.__instance, attr)
    
    def __setattr__(self,attr,value):
        return setattr(self.__instance, attr, value)
    
    