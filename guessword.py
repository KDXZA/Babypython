import random
score=0
lives=3
words=['Great','cherprang','jaa']
def update_clue(guess,sc,clue):
  for i in range(len(sc)) :
      if guess == sc[i] :
         clue[i]=guess
  win=''.join(clue)== sc
  return win     
  

while (len(words)>0) and (lives>0):
    random.shuffle(words)
    sc=words.pop()
    clue=list('?'*len(sc))
    while True:
        print(clue)
        print('lives: '+str(lives))
        guess=input('เดามา:')
        if guess in sc:
            win=update_clue(guess,sc,clue)
            if win:
                print('congrates')
                score=score+1
                print('score: '+str(score))
                break
        else:
          print('ผิด')
          lives=lives-1
          if lives==0:
              print('lose!!!: ',sc)       
              break                 
print('final scores: ',str(score))
print('game end!')      


