from signals import signal

def enlistSignals(signal):
    for key in signal:
        if key=='signal_1':
            print(signal[key])

def IsFullSignal(signal):
    return True if len(signal)>6 else False

def IsMidSignal(signal):
    return True if len(signal)==6 else False

def HasEntryZone(signal):
    entry_line = signal[3].split(' ')
    return True if len(entry_line)>2 else False
    

def IsEntryTargets(signal):
    for line in signal:
        if line.lower().find('entry')!=-1:
            if line.lower().find('zone')!=-1 or line.lower().find('targets')!=-1:
                return True
    return False
    
def IsTakeProfit(signal):
    for idx, lines in enumerate(signal):
        has_tp=lines.find('Take-Profit')
        if has_tp!=-1:
            return idx, True
    return 0, False

def IsThirdTP(signal):
    for idx, line in enumerate(signal):
        has_tp=line.find('Take-Profit')
        
        if has_tp!=-1:
            word=line.split(' ')
            print(word[-2])
            return True if word[-2]=='3' else False
    return False
    
def IsStopLoss(signal):
    for line in signal:
        if line.lower().find('stoploss')!=-1:
            return True
    return False
def IsClosing(signal):

    for line in signal:
        if line.lower().find('opposite')!=-1:
            return True
    return False

def IsCanceled(signal):
    for line in signal:
        if line.lower().find('cancelled')!=-1:
            return True
    return False
def _get_Target(line):
    tgt=float(line.split(' ')[2])
    try:
        tgt_out=float(line.split(' ')[4][:line.split(' ')[4].find('%')])
        return [tgt, tgt_out]
    except IndexError:
        return [tgt,0.25]

def _getTagrgets(lined_signal):
    targets= [None,None,None,None,None,None,None,None]
    for line in lined_signal:
        if line.lower().find('target 1')!=-1:
            targets[0], targets[1]=_get_Target(line)
        elif line.lower().find('target 2')!=-1:
            targets[2], targets[3]=_get_Target(line)
        elif line.lower().find('target 3')!=-1:
            targets[4], targets[5]=_get_Target(line)
        elif line.lower().find('target 4')!=-1:
            targets[6], targets[7]=_get_Target(line)
        elif line.lower().find('stoploss')!=-1 or line.lower().find('stop loss')!=-1:
            SL=float(line.split(' ')[1])

    None_counter=0
    for t_idx, target in enumerate(targets):
        if target==None:
            targets[t_idx]=targets[t_idx-2]
            

    tgt1=targets[0]
    tgt1_out=targets[1]
    tgt2=targets[2]
    tgt2_out=targets[3]
    tgt3=targets[4]
    tgt3_out=targets[5]
    tgt4=targets[6]
    tgt4_out=targets[7]
    return tgt1, tgt1_out, tgt2, tgt2_out, tgt3,tgt3_out, tgt4, tgt4_out, SL

def FullSignal(lined_signal):

    exchange=lined_signal[0]
    pair=getPair(lined_signal)
    trade=getTrade(lined_signal)
    leverage=float(lined_signal[2].split(' ')[2][:lined_signal[2].split(' ')[2].find('x')])

    entry=float((lined_signal[3].split(' ')[-1]))
    tgt1, tgt1_out, tgt2, tgt2_out, tgt3,tgt3_out, tgt4, tgt4_out ,SL = _getTagrgets(lined_signal)

    signal_dict={'Entity':'Orders','Exchange':exchange, 'Pair':pair, 'Trade': trade, 'Leverage':leverage,
    'Entry': entry,'Target 1':tgt1,'Target 1 out':tgt1_out,'Target 2':tgt2,'Target 2 out':tgt2_out,
    'Target 3':tgt3,'Target 3 out':tgt3_out,'Target 4':tgt4,'Target 4 out':tgt4_out,'Stop Loss':SL}
    return signal_dict
    
def MidSignal(lined_signal):

    exchange=lined_signal[0]
    pair=getPair(lined_signal)
    trade=getTrade(lined_signal)


    leverage=float(lined_signal[2].split(' ')[2][:lined_signal[2].split(' ')[2].find('x')])
    entry=float((lined_signal[3].split(' ')[-1]))
    tps=[]
    for idx in range(1,8,2):
        if lined_signal[4].split(' ')[idx]!='null':
            tps.append(lined_signal[4].split(' ')[idx])
        else:
            tps.append(lined_signal[4].split(' ')[idx-1])
    tgt1=tps[0]
    tgt2=tps[1]
    tgt3=tps[2]
    tgt4=tps[3]
    tgt1_out=0.25
    tgt2_out=0.25
    tgt3_out=0.25
    tgt4_out=0.25

    SL=float(lined_signal[5].split(' ')[1])

    signal_dict={'Entity':'Orders', 'Exchange':exchange, 'Pair':pair, 'Trade': trade, 'Leverage':leverage,
    'Entry': entry,'Target 1':tgt1,'Target 1 out':tgt1_out,'Target 2':tgt2,'Target 2 out':tgt2_out,
    'Target 3':tgt3,'Target 3 out':tgt3_out,'Target 4':tgt4,'Target 4 out':tgt4_out,'Stop Loss':SL}
    return signal_dict
def getTrade(signal):
    for line in signal:
        if line.find('SHORT')!=-1 or line.find('short')!=-1 or line.find('Short')!=-1:
            return 'SHORT'
        if line.find('LONG')!=-1 or line.find('long')!=-1 or line.find('Long')!=-1:
            return 'LONG'

    return None

def getPair(signal):
    for idx, line in enumerate(signal):
        words=line.split(' ')
        for word in words:
            pair_idx=word.find('USDT')
            if pair_idx!=-1:
                has_slash= True if word.find('/')!=-1 else False
                has_hash= True if word.find('#')!=-1 else False
                pair= word.replace('/','') if has_slash else word
                pair=pair.replace('#','') if has_hash else pair
                return pair
    return None

        
def getEntryPoint(pair):
    return 'in progress'
def CloseExPosition(signal):
    return 'In Progress'
def EntryFulfilled():

    signal_dict={'Entity':'Entry Fulfilled'}
    return signal_dict
def TakeProfit(signal,third_tp,tp_line):
    tp_number=int(signal[tp_line].split(' ')[-2])
    if third_tp:
        pair=getPair(signal)
        entry=getEntryPoint(pair)
        signal_dict={'Entity':'Order' ,'Pair':pair,'Stop Loss':entry}
    else:
        signal_dict={'Entity':f'Take Profit {tp_number}', 'Pair':{getPair(signal)}}
    return signal_dict
def StopLoss(signal):
    signal_dict={'Entity':'Stop loss achieved'}
    return signal_dict

def ClosePosition(signal):
    pair=getPair(signal)
    closed_position=CloseExPosition(signal)
    signal_dict={'Entity':'Close Possition', 'Pair':pair, 'Closed':closed_position}
    return signal_dict
def Cancelled(signal):
    pair=getPair(signal)
    closed_position=CloseExPosition(signal)
    signal_dict={'Entity':'Cancelled Possition', 'Pair':pair, 'Closed':closed_position}
    return signal_dict

def detectSignal_1(signal_1):
    SIGNAL=signal_1
    lined_signal=SIGNAL.splitlines()

    if IsFullSignal(lined_signal):
        signal_dict=FullSignal(lined_signal)
    elif IsMidSignal(lined_signal):
        signal_dict=MidSignal(lined_signal)
    elif IsEntryTargets(lined_signal):
        signal_dict=EntryFulfilled()
        # print('Entry levels achieved')
    elif IsTakeProfit(lined_signal)[1]:
        # print('Take-Profit Signal')
        third_tp= True if IsThirdTP(lined_signal) else False
        tp_line= IsTakeProfit(lined_signal)[0]
        signal_dict=TakeProfit(lined_signal,third_tp,tp_line)
    elif IsStopLoss(lined_signal):
        signal_dict=StopLoss(lined_signal)
        # print('Stop-Loss Signal')
    elif IsClosing(lined_signal):
        signal_dict=ClosePosition(lined_signal)
        # print('Closing Possition')
    elif IsCanceled(lined_signal):
        signal_dict=Cancelled(lined_signal)
        # print('Cancelled Position')
    else:
        signal_dict={'Entity':'Is not a preconfigured signal'}
        # print('Is not signal')
    # print(SIGNAL)
    return signal_dict


# signal_1=detectSignal_1(signal['take_profit_2'])
# print(signal_1)
