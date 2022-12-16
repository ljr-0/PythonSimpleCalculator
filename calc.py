import wx
from sys import exit as sys_exit
from sys import path as sys_path
from os import path as os_path
import advcalclib
import decimal
class Calculator(wx.Frame):
    def __init__(self, DebugModeOpened = True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os_path.isfile(sys_path[0]+'\\config.json'):
            try: self.config_list=eval(open(sys_path[0]+'\\config.json','r').read()) 
            except:self.config_list={'prec':1024}
        else:
            self.config_list={'prec':1024}
        self.init_ui()
        self.DebugModeOpened = DebugModeOpened
        if self.DebugModeOpened == True:
            self.Debug = True
        else:
            self.Debug = False
    def init_ui(self, *args, **kwargs):
        self.MENU_EXIT=0
        self.MENU_COPY=1
        self.MENU_CUT=2
        self.MENU_PASTE=3
        self.MENU_SALL=4
        self.panel = wx.Panel(self)
        self.h_box1 = wx.BoxSizer()
        self.h_box2 = wx.BoxSizer()
        self.ExpCtrl = wx.TextCtrl(self.panel,id=-1,style=wx.TE_PROCESS_ENTER|wx.TE_CENTER,size = (320, -1))
        self.h_box1.Add(self.ExpCtrl,flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.LaunchButton = wx.Button(self.panel, -1, label = '=',size = (40, -1), style = wx.CENTER)
        self.ClearButton = wx.Button(self.panel, -1, 'C', size = (40 ,-1), style = wx.CENTER)
        self.CopyButton = wx.Button(self.panel, -1, 'Copy', size = (40,-1), style = wx.CENTRE)
        self.ResCtrl = wx.TextCtrl(self.panel,id=-1,style=wx.TE_PROCESS_ENTER|wx.TE_CENTER,size = (160, -1))
        self.h_box2.Add(self.LaunchButton,flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.h_box2.Add(self.ResCtrl,flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.h_box2.Add(self.ClearButton,flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.h_box2.Add(self.CopyButton,flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.v_box = wx.BoxSizer(orient=wx.VERTICAL)
        self.v_box.Add(self.h_box1,flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.v_box.Add(self.h_box2,flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.Big_v_box = wx.BoxSizer()
        self.Big_v_box.Add(self.v_box, flag = wx.EXPAND|wx.ALL|wx.CENTER)
        self.panel.SetSizer(self.Big_v_box)
        self.ExpCtrl.SetMaxLength(0)
        self.ResCtrl.SetMaxLength(0)
        self.MenuBar = wx.MenuBar()
        self.FileMenu = wx.Menu()
        self.EditMenu = wx.Menu()
        self.MenuBar.Append(self.FileMenu, 'File')
        self.MenuBar.Append(self.EditMenu, 'Edit')
        self.MenuExit = self.FileMenu.Append(self.MENU_EXIT,'Exit\tAlt+F4','Exit')
        self.MenuAll = self.EditMenu.Append(self.MENU_SALL, 'Select All\tCtrl+A', 'Select All')
        self.EditMenu.AppendSeparator()
        self.MenuCopy = self.EditMenu.Append(self.MENU_COPY, 'Copy\tCtrl+C', 'Copy')
        self.MenuCut = self.EditMenu.Append(self.MENU_CUT, 'Cut\tCtrl+V', 'Cut')
        self.MenuPaste = self.EditMenu.Append(self.MENU_PASTE, 'Paste\tCtrl+V', 'Paste')
        self.SetMenuBar(self.MenuBar)
        self.statusbar = self.CreateStatusBar()
        #将状态栏分割为3个部分
        self.statusbar.SetFieldsCount(1)
        #分割状态栏的比例为3：2：1，用负数表示
        self.statusbar.SetStatusWidths([-1])
        #每部分状态栏显示的值，当鼠标停在menu上时，0号状态栏会临时显示上面menu里的提示信息
        self.statusbar.SetStatusText('None',0)
        self.SetStatusBar(self.statusbar)
        
        self.Bind(wx.EVT_MENU, lambda self:sys_exit(),self.MenuExit)
        self.Bind(wx.EVT_CLOSE, lambda self:sys_exit(0), self)
        self.Bind(wx.EVT_MENU, self.OnCopy,self.MenuCopy)
        self.Bind(wx.EVT_MENU, self.OnCut,self.MenuCut)
        self.Bind(wx.EVT_MENU, self.OnPaste,self.MenuPaste)
        self.Bind(wx.EVT_MENU, self.OnSelectAll,self.MenuAll)
        self.Bind(wx.EVT_BUTTON, self.launch, self.LaunchButton)
        self.Bind(wx.EVT_BUTTON, self.cleardata, self.ClearButton)
        self.Bind(wx.EVT_BUTTON, self.CopyData, self.CopyButton)
        self.Bind(wx.EVT_TEXT_ENTER, self.launch, self.ExpCtrl)
    
    def launch(self,null):
        try:
            self.expression = self.ExpCtrl.GetValue()
            self.Expression_List = advcalclib.formula_format(self.expression)
            self.result = advcalclib.final_calc(self.Expression_List,prec=self.config_list['prec'])
            if self.result != None:
                self.ResCtrl.SetValue(str(self.result))
                self.statusbar.SetStatusText(self.expression+"="+self.result,0)
            else :
                self.ResCtrl.SetValue('')
                self.statusbar.SetStatusText("None",0)
        except Exception as e:
            self.e=e
            if str(self.e) == "[<class 'decimal.DivisionByZero'>]":
                print('Division by Zero:"'+self.expression+'"')
                if self.Debug:
                    raise self.e
            elif str(self.e) == "[<class 'decimal.ConversionSyntax'>]":
                print('Incorrect formula:"'+self.expression+'"')
                if self.Debug:
                    raise self.e
            else:
                print('Unknown error:"'+self.expression+'"')
                if self.Debug:
                    raise self.e
    def cleardata(self, null):
        self.ResCtrl.SetValue('')
        self.ExpCtrl.SetValue('')
    def CopyData(self, null):
        self.data_object = wx.TextDataObject(self.ResCtrl.GetValue())
        wx.TheClipboard.SetData(self.data_object)
    def OnCopy(self, null):
        self.focus=self.FindFocus()
        print(type(self.focus))
        if type(self.focus) == wx._core.TextCtrl:
            self.StringSel  = self.focus.GetStringSelection()
            self.CopyText =  wx.TextDataObject(str(self.StringSel))
            wx.TheClipboard.SetData(self.CopyText)
        else :
            pass
    def OnPaste(self, null):
        self.focus=self.FindFocus()
        if type(self.focus) == wx._core.TextCtrl:
            self.focus.Paste()
        else:
            pass
    def OnCut(self, null):
        self.focus=self.FindFocus()
        if type(self.focus) == wx._core.TextCtrl:
            self.focus.Cut()
        else:
            pass
    def OnSelectAll(self, null):
        self.focus=self.FindFocus()
        if type(self.focus) == wx._core.TextCtrl:
            self.focus.SelectAll()
        else:
            pass

    

if __name__ == '__main__':
    app = wx.App()
    calc = Calculator(parent=None,id = -1,title='Calculator',size = (335, 133))
    calc.Show()
    app.MainLoop()
