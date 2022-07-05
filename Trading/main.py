import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler , Filters
from readingSignals import detectSignal_1




def Response(update,context):
    try:
        Chat_Id=update.message.chat_id
        is_channel=False
    except AttributeError:
        Chat_Id=update.channel_post['chat']['title']
        is_channel=True

    Message_text= str(update.channel_post['text']) if is_channel else update.message.text
    # print(Message_text)
    signal_dict=detectSignal_1(Message_text)
    print(f'''Mensaje Recibido
    de: {Chat_Id}
    {signal_dict}
    ''')
    bot.send_message(chat_id=1288815104,text=f'Mensaje de {Chat_Id} Recibido\nDel tipo: {signal_dict["Entity"]}')


if __name__=='__main__':
    with open('./tradingToken.txt','r') as f:
        TOKEN=f.read()
    # print(TOKEN)
    bot = telegram.Bot(token=TOKEN)
    updater = Updater(bot.token,use_context=True)

    dispatcher = updater.dispatcher

    Responses= MessageHandler(Filters.text, Response)
    dispatcher.add_handler(Responses)
    
    updater.start_polling()