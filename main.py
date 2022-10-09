import wx
import logging
import datetime
import time
import os
import sys
import traceback
import Properties
import decimal
from math import *

#A Simple Calculator in Python wx GUI (vresion 1.0.8)
version = '1.0.8'
now = datetime.datetime.now()
dt = now.strftime("%Y-%m-%d-%H-%M-%S")
dt1 = now.strftime("%Y-%m-%d %H:%M:%S")
if os.path.isfile('config.properties'):
    config = Properties.Properties('config.properties').getProperties()
    try:
        history_enabled=eval(config['history_enabled'])
    except:
        history_enabled=True
    try:
        log_enabled=eval(config['log_enabled'])
    except:
        log_enabled=True
    try:
        HistoryDir=config['HistoryDir']
    except:
        HistoryDir='files\\'
    try:
        LogDir=config['LogDir']
    except:
        LogDir='files\\logs\\'
    try:
        HistoryName=eval(config['HistoryName'])
    except:
        HistoryName='history.txt'
    try:
        LogFileName=eval(config['LogFileName'])
    except:
        LogFileName='log-'+dt+'.txt'
    try:
        DefaltPrec=eval(config['DefaltPrec'])
    except:
        DefaltPrec=decimal.MAX_PREC
    try:
        LittlePrec=eval(config['LittlePrec'])
    except:
        LittlePrec=256
else:
    history_enabled=bool('True')
    log_enabled=bool('True')
    HistoryDir='files\\'
    LogDir='files\\logs\\'
    HistoryName='history.txt'
    LogFileName='log-'+dt+'.txt'
    DefaltPrec=decimal.MAX_PREC
    LittlePrec=256
if history_enabled==True:
    if not os.path.isdir(HistoryDir)==True:
        os.mkdir(HistoryDir)
if log_enabled==True:
    if not os.path.isdir(LogDir)==True:
        if not HistoryDir==LogDir:
            os.mkdir(LogDir)
calc = wx.App()
iconcalc = wx.Icon(name="files\\calc.ico",type=wx.BITMAP_TYPE_ICO)
iconclk = wx.Icon("files\\clock32.png", type=wx.BITMAP_TYPE_PNG)
calcgui =wx.Frame(None,-1,'Calc')
sht = wx.Image("files\\exit32.png", type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
cpy = wx.Image("files\\copy32.png", type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
clk = wx.Image("files\\clock32.png", type=wx.BITMAP_TYPE_ANY).ConvertToBitmap()
calcgui.SetIcon(iconcalc)
calcgui.SetSize(0,0,800,250)
calcgui.SetBackgroundColour("#FFFFFF")
calcgui.Centre()
calcpanel = wx.Panel(calcgui)
m1e = wx.TextCtrl(calcpanel, id=1, pos=(20, 30), size=(160, -1), style = wx.TE_CENTER|wx.TE_PROCESS_ENTER)
te =wx.TextCtrl(calcpanel, id=10, pos=(185, 30), size=(100, -1), style = wx.TE_CENTER|wx.TE_PROCESS_ENTER)
m2e =wx.TextCtrl(calcpanel, id=2, pos=(290, 30), size=(160, -1), style = wx.TE_CENTER|wx.TE_PROCESS_ENTER)
clbtn = wx.Button(calcpanel,id=20, pos=(455, 30),size=(80, -1), style=wx.CENTER, label="=")
rese = wx.TextCtrl(calcpanel,id=3, pos=(540, 30),size=(80, -1), style=wx.TE_CENTER)
clearb = wx.Button(calcpanel, id=40, pos=(455, 5), size=(80, -1), style=wx.CENTER, label=" C ")
copyb = wx.BitmapButton(calcpanel, 50, cpy, pos=(560, 55))
quitb = wx.BitmapButton(calcpanel, 60, sht, pos=(475, 55))
hstb = wx.BitmapButton(calcpanel, 70, clk, pos=(517, 55))
m1e.SetMaxLength(0)
m2e.SetMaxLength(0)
rese.SetMaxLength(0)
te.SetMaxLength(0)
frm=wx.Frame(calcgui, title = 'History', size = (655, 677),style=wx.DEFAULT_FRAME_STYLE^(wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER))
frm.SetIcon(iconclk)
Control = wx.TextCtrl(frm, -1, size=(640, 500), style = wx.TE_MULTILINE)
Control.SetMaxLength(0)
cbtn = wx.Button(frm,id=80, pos=(320, 500),size=(320, 140), style=wx.CENTER, label="==Hide==")
rbtn = wx.Button(frm,id=90, pos=(0, 500),size=(320, 140), style=wx.CENTER, label="==Refresh==")
Control.SetMaxLength(0)
if os.path.isfile(HistoryDir+HistoryName):
    hstr=open(HistoryDir+HistoryName, encoding='utf-8')
    txhs=hstr.read()
    hstr.close()
    Control.SetValue(str(txhs))
def hs(self):
    frm.Show(True)
def hds(self):
    frm.Hide()
def refresh(self):
    if os.path.isfile(HistoryDir+HistoryName):
        hstr=open(HistoryDir+HistoryName, encoding='utf-8')
        txhs=hstr.read()
        hstr.close()
        Control.SetValue(str(txhs))
def calculation(self=None):
    global DefaltPrec,LittlePrec
    decimal.getcontext().prec=int(DefaltPrec)
    if log_enabled==True:
        test_log = logging.FileHandler(LogDir+LogFileName,'a',encoding='utf-8')
        logger = logging.getLogger('test_logger')
        formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s : %(process)s :\n '+traceback.format_exc())
        test_log.setFormatter(formatter)
        logger.addHandler(test_log)        
    try:
        global dt,dt1
        m1=str(m1e.GetValue())
        m2=str(m2e.GetValue())
        sy=str(te.GetValue())
        result = ""
        if sy=="+" or sy=="-" or sy=="*" or sy=="/" or sy=="<" or sy==">" or sy=="=" or sy=="//" or sy=="%" or sy=="":
            result=str(decimal.Decimal(eval('decimal.Decimal(m1)'+sy+'decimal.Decimal(m2)')))
        elif sy=="^" or sy=="**":
            decimal.getcontext().prec=int(LittlePrec)
            result=str(decimal.Decimal(eval("decimal.Decimal(decimal.Decimal(m1)**decimal.Decimal(m2))")))
        elif sy=="√":
            decimal.getcontext().prec=int(LittlePrec)
            result=str(decimal.Decimal(eval('decimal.Decimal(decimal.Decimal(m2)**(decimal.Decimal(1)/decimal.Decimal(m1)))')))
        elif sy=='sin' or sy=='cos' or sy=='tan' or sy=='radians' or sy=='degrees':
            result=str(decimal.Decimal(eval(sy+'(radians(decimal.Decimal('+m2+')))')))
        elif sy=='version':
            result=version
        else:
            result=0
        rese.SetValue(result)
        if history_enabled==True:
            history = open(str(HistoryDir+HistoryName),'a+', encoding='utf-8')
            history.write('\n'+dt1+'\n'+m1+sy+m2+'\n'+result)
            history.close()
        if log_enabled==True:
            formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s : %(process)s')
            logger.setLevel(logging.INFO)
            logger.info('Calculated : '+m1+sy+m2+' Result :'+result) 
    except:
        if log_enabled=='True':
            logger.setLevel(logging.ERROR)
            formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s : %(process)s - Error :\n '+traceback.format_exc())
            logger.error('Calculation Failed')
def clear(self=None):
    m1e.SetValue("")
    m2e.SetValue("")
    rese.SetValue("")
    te.SetValue("")
def copy(self=None):
    data_object = wx.TextDataObject(rese.GetValue())
    wx.TheClipboard.SetData(data_object)
def ex(self):
    calc.Destroy()
    sys.exit(0)
def historyv(self):
    hs(None)
            

calc.Bind(wx.EVT_BUTTON, calculation, clbtn)
calc.Bind(wx.EVT_TEXT_ENTER, calculation, source=None, id=1)
calc.Bind(wx.EVT_TEXT_ENTER, calculation, source=None, id=10)
calc.Bind(wx.EVT_TEXT_ENTER, calculation, source=None, id=2)
calc.Bind(wx.EVT_BUTTON, clear, source=None, id=40)
calc.Bind(wx.EVT_BUTTON, copy, source=None, id=50)
calc.Bind(wx.EVT_BUTTON, ex, source=None, id=60)
calc.Bind(wx.EVT_BUTTON, historyv, source=None, id=70)
calc.Bind(wx.EVT_BUTTON, hds, source=None, id=80)
calc.Bind(wx.EVT_BUTTON, refresh, source=None, id=90)
calcgui.Show()
calc.MainLoop()
