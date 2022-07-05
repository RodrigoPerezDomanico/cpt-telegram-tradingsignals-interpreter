import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler , Filters
import re
from Utils import readSignal


with open('tradingToken.txt','r') as f:
    TOKEN=f.read()
    f.close()



def _ManageData(Message_text,currency):
    
    pass





def Response(update,context):
    try:
        Chat_Id=update.message.chat_id
    except AttributeError():
        Chat_Id='Channel Message'
    Message_text=update.message.text
    print(f'''Mensaje Recibido
    de: {Chat_Id}
    ''')
    signal=readSignal(Message_text)
    if signal=={}:
        Response_text='Señal Corta'
    else:
        Response_text='Señal Larga'
    bot.send_message(chat_id=update.message.chat_id,text=Response_text)


if __name__ == '__main__':

    bot = telegram.Bot(token=TOKEN)
    updater = Updater(bot.token,use_context=True)

    dispatcher = updater.dispatcher
    
    Responses= MessageHandler(Filters.text, Response)
    dispatcher.add_handler(Responses)
  
    updater.start_polling()