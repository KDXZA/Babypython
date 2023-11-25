from tkinter import *
import random
import time
from tkinter.font import Font
window= Tk()
window.title('Game tai si ja')
window.geometry('700x840')

game_finished = False
score=0
lives=3

status_str=StringVar()

status_str.set('score: ',str(score),' | ','Lives: ','❤️'*lives)
show_status= Label(window,textvarible=status_str)
show_status.pack(pady=20)

word_dict ={
    'cherprang':
        {
            'category':'ดาราในดวงใจ',
            'hints' :['คนสวย','สมาชิก BNK48','เซนเตอร์ของวง'] 
        },
    'great':
        {
            'category':'ติวเตอร์ในดวงใจ',
            'hints' :['สอนฟิสิกส์','เมนเจนนี่','โอชิเฌอปราง'] 
        },
    'jaa':
        {
            'category':'ดาราในดวงใจ',
            'hints' :['สมาชิก BNK48','ลูกศิษย์พี่เกรท'] 
        }
}

words=list(word_dict.keys())

def get_new_sc():
    random.shuffle(words)
    sc=words.pop()
    clue=list('?'*len(sc))
    return sc,clue
sc , clue=get_new_sc()

category_str=StringVar()
category_str.set(word_dict[sc]['category'])
show_category= Label(window,textvarible=category_str, font=('Arial', 28))
show_category.pack(pady=10)

clue_str=StringVar()
clue_str.set(' | '.join(clue))
show_clue= Label(window,textvarible=clue_str, font=('Arial', 50))
show_clue.pack(padx=10,pady=30)




