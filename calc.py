import wx
from sys import exit as sys_exit
import advcalclib
import decimal
class CalculatorGUI(wx.Frame):
    '''CalculatorGUI CalculatorGUI(parent, 
    id=ID_ANY, 
    title=EmptyString, 
    pos=DefaultPosition, 
    size=DefaultSize, 
    style=DEFAULT_FRAME_STYLE, 
    name=FrameNameStr, 
    DebugMode=False)\n\n
    Create an Calculator (GUI Mode).
    '''
    def __init__(self,DebugMode, **kwargs):
        '''Calculator Calculator(parent, 
        id=ID_ANY, 
        title=EmptyString, 
        pos=DefaultPosition, 
        size=DefaultSize, 
        style=DEFAULT_FRAME_STYLE, 
        name=FrameNameStr, 
        DebugMode=False)\n\n
        Create an Calculator (GUI Mode).
        '''
        super().__init__(**kwargs)
        self.init_ui()
        self.DebugMode = DebugMode
        if self.DebugMode == True:
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
        self.MenuAll = self.EditMenu.Append(self.MENU_SALL, 'Select All\tCtrl+A', 'SelectAll')
        self.EditMenu.AppendSeparator()
        self.MenuCopy = self.EditMenu.Append(self.MENU_COPY, 'Copy\tCtrl+C', 'Copy')
        self.MenuCut = self.EditMenu.Append(self.MENU_CUT, 'Cut\tCtrl+V', 'Cut')
        self.MenuPaste = self.EditMenu.Append(self.MENU_PASTE, 'Paste\tCtrl+V', 'Paste')
        self.SetMenuBar(self.MenuBar)
        
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
            self.result = advcalclib.final_calc(self.Expression_List)
            if self.result != None:
                self.ResCtrl.SetValue(str(self.result))
            else :
                self.ResCtrl.SetValue('')
        except Exception as e:
            if str(e) == "[<class 'decimal.DivisionByZero'>]":
                print('Division by Zero:"'+self.expression+'"')
                if self.Debug:
                    raise e
            elif str(e) == "[<class 'decimal.ConversionSyntax'>]":
                print('Incorrect formula:"'+self.expression+'"')
                if self.Debug:
                    raise e
            else:
                print('Unknown error:"'+self.expression+'"')
                if self.Debug:
                    raise e
    def cleardata(self, null):
        self.ResCtrl.SetValue('')
        self.ExpCtrl.SetValue('')
    def CopyData(self, null):
        self.data_object = wx.TextDataObject(self.ResCtrl.GetValue())
        wx.TheClipboard.SetData(self.data_object)
    def OnCopy(self, null):
        self.focus=self.FindFocus()
        if str(type(self.focus)) == "<class 'wx._core.TextCtrl'>":
            self.StringSel  = self.focus.GetStringSelection()
            self.CopyText =  wx.TextDataObject(str(self.StringSel))
            wx.TheClipboard.SetData(self.CopyText)
        else :
            pass
    def OnPaste(self, null):
        self.focus=self.FindFocus()
        if str(type(self.focus)) == "<class 'wx._core.TextCtrl'>":
            self.focus.Paste()
        else:
            pass
    def OnCut(self, null):
        self.focus=self.FindFocus()
        if str(type(self.focus)) == "<class 'wx._core.TextCtrl'>":
            self.focus.Cut()
        else:
            pass
    def OnSelectAll(self, null):
        self.focus=self.FindFocus()
        if str(type(self.focus)) == "<class 'wx._core.TextCtrl'>":
            self.focus.SelectAll()
        else:
            pass

if __name__ == '__main__':
    app = wx.App()
    calc = CalculatorGUI(parent=None,id = -1,title='Calculator',size = (335, 108), DebugMode = False)
    calc.Show()
    app.MainLoop()
