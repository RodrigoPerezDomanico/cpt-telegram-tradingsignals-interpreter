def signalTypeIsFull(first_line):
    if first_line=='Pair:' or first_line=='Pair':
        return False
    else:
        return True

def signalTypeFull(lined_signal):
    exchange=lined_signal[0]
    pair=lined_signal[1].split(' ')[0]
    trade=lined_signal[1].split(' ')[1]
    leverage=float(lined_signal[2].split(' ')[2][:lined_signal[2].split(' ')[2].find('x')])
    entry=float((lined_signal[3].split(' ')[1]))
    tgt1=float(lined_signal[4].split(' ')[2])
    tgt1_out=float(lined_signal[4].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    tgt2=float(lined_signal[5].split(' ')[2])
    tgt2_out=float(lined_signal[5].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    tgt3=float(lined_signal[6].split(' ')[2])
    tgt3_out=float(lined_signal[6].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    tgt4=float(lined_signal[7].split(' ')[2])
    tgt4_out=float(lined_signal[7].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    SL=float(lined_signal[8].split(' ')[1])

    # print(f'''{exchange}
    # {pair} {trade}
    # {leverage}
    # {entry}
    # {tgt1} {tgt1_out}
    # {tgt2} {tgt2_out}
    # {tgt3} {tgt3_out}
    # {tgt4} {tgt4_out}
    # {SL}
    # ''')

    signal={'Exchange':exchange, 'Pair':pair, 'Trade': trade, 'Leverage':leverage,
    'Entry': entry,'Target 1':tgt1,'Target 1 out':tgt1_out,'Target 2':tgt2,'Target 2 out':tgt2_out,
    'Target 3':tgt3,'Target 3 out':tgt3_out,'Target 4':tgt4,'Target 4 out':tgt4_out,'Stop Loss':SL}
    return signal

def signalTypeShorted(lined_signal):
    exchange=lined_signal[0]
    pair=str(lined_signal[1].split(' ')[1])+'USDT'
    trade=lined_signal[1].split(' ')[-1].replace('x', '')
    
    # leverage=float(lined_signal[2].split(' ')[2][:lined_signal[2].split(' ')[2].find('x')])
    # entry=float((lined_signal[3].split(' ')[1]))
    # tgt1=float(lined_signal[4].split(' ')[2])
    # tgt1_out=float(lined_signal[4].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    # tgt2=float(lined_signal[5].split(' ')[2])
    # tgt2_out=float(lined_signal[5].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    # tgt3=float(lined_signal[6].split(' ')[2])
    # tgt3_out=float(lined_signal[6].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    # tgt4=float(lined_signal[7].split(' ')[2])
    # tgt4_out=float(lined_signal[7].split(' ')[4][:lined_signal[2].split(' ')[2].find('%')])
    # SL=float(lined_signal[8].split(' ')[1])

    # print(f'''{exchange}
    # {pair} {trade}
    # {leverage}
    # {entry}
    # {tgt1} {tgt1_out}
    # {tgt2} {tgt2_out}
    # {tgt3} {tgt3_out}
    # {tgt4} {tgt4_out}
    # {SL}
    # ''')
    signal={}
    # signal={'Exchange':exchange, 'Pair':pair, 'Trade': trade, 'Leverage':leverage,
    # 'Entry': entry,'Target 1':tgt1,'Target 1 out':tgt1_out,'Target 2':tgt2,'Target 2 out':tgt2_out,
    # 'Target 3':tgt3,'Target 3 out':tgt3_out,'Target 4':tgt4,'Target 4 out':tgt4_out,'Stop Loss':SL}
    print(pair, trade)
    return signal


def readSignal(text):
    # with open(text,'r',encoding='utf-8') as f:
    #     SIGNAL = f.read()
    #     f.close()
    SIGNAL=text
    lined_signal=SIGNAL.splitlines()
    if signalTypeIsFull(lined_signal[1].split(' ')[0]):
        signal=signalTypeFull(lined_signal)
    else:
        signal=signalTypeShorted(lined_signal)

    

    return signal
# signal=readSignal("señal.txt")
# print(signal)

# f = open("señal.txt","r")
# Text=f.readlines()
# for idx, line in enumerate(Text):
#     # print(line)
#     if idx==1:
#         wordline = line.split(' ')
#         for word in wordline:
#             # print(word)
#             if word=='MANA':
#                 print('MANA/USDT')
