from brain.predict import final_verdict

def static(varname,value):
   def decor(func):
      setattr(func,varname,value)
      return func
   return decor

@static('count',0)
def bot(text=None):
   bot.count+=1
   print(bot.count)
   steps={
      1:'Hello,Im Your medical chatbot,Please type your symtomns in a paragraph',
      2:final_verdict(text),
      3:'err',
      4:'err',
      }

   return steps.get(bot.count,'Completed')

if __name__=='__main__':
   print(bot())
   print(bot('hello'))

   

