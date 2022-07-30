'''Я не знал про такую технологию и почитал в интернете.
В целом я попробовал создать что-то напоминающее данную конструкцию самостоятельно.'''

class Buffer:
    def __init__(self,size):
        self.size = size
        self.array = [0]*size
        self.dot = 0
        
    def rewrite(self,*inputs):
        for i in inputs:
            if self.dot == self.size-1:
                self.array[self.dot] = i
                self.dot = 0
            else:
                self.array[self.dot] = i
                self.dot+=1
        return self.array
      
      
     ''' В целом это похоже на реализацию заданой задачи, правда на Python 3.*.
     Также я не могу рассказать о достоинствах и недостатках этого кода т.к. не знаком с технологией. И не знаю на что обратить внимание.'''
