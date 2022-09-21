import wx
calc = wx.App()
calcgui =wx.Frame(None,-1,'计算器')
calcgui.SetSize(0,0,800,250)
calcgui.SetBackgroundColour("#FFFFFF")
calcgui.Centre()
calcpanel = wx.Panel(calcgui)
m1e = wx.TextCtrl(calcpanel, id=1,
                    pos=(20, 30), size=(160, -1), style = wx.TE_CENTER|wx.TE_PROCESS_ENTER)
te =wx.TextCtrl(calcpanel, id=10,
                    pos=(185, 30), size=(100, -1), style = wx.TE_CENTER|wx.TE_PROCESS_ENTER)
m2e =wx.TextCtrl(calcpanel, id=2,
                    pos=(290, 30), size=(160, -1), style = wx.TE_CENTER|wx.TE_PROCESS_ENTER)
clbtn = wx.Button(calcpanel,id=20,
                    pos=(455, 30),size=(80, -1), style=wx.CENTER, label="计算")
rese = wx.TextCtrl(calcpanel,id=3,
                    pos=(540, 30),size=(80, -1), style=wx.TE_CENTER)
clearb = wx.Button(calcpanel, id=40,
                    pos=(455, 5), size=(80, -1), style=wx.CENTER, label=" C ")
copyb = wx.Button(calcpanel, id=50,
                    pos=(540, 55), size=(80,-1), style=wx.CENTER, label="复制")
quitb = wx.Button(calcpanel, id=60,
                    pos=(455, 55), size=(80,-1), style=wx.CENTER, label="退出")
m1e.SetMaxLength(0)
m2e.SetMaxLength(0)
rese.SetMaxLength(0)
te.SetMaxLength(0)
def calculation(calc):
    m1=m1e.GetValue()
    m2=m2e.GetValue()
    sy=te.GetValue()
    result = ""
    if sy=="+" or sy=="-" or sy=="*" or sy=="/" or sy=="<" or sy==">" or sy=="=" or sy=="//" or sy=="%":
        result=str(eval(m1+sy+m2))
    elif sy=="^" or sy=="**":
        result=str(eval("pow(float(m1e.GetValue()),float(m2e.GetValue()))"))
    elif sy=="√":
        result=str(eval("pow(float(m2e.GetValue()),1/float(m1e.GetValue()))"))
    else:
        result=0
    rese.SetValue(result)
def clear(calc):
    m1e.SetValue("")
    m2e.SetValue("")
    rese.SetValue("")
    te.SetValue("")
def copy(self):
    data_object = wx.TextDataObject(rese.GetValue())
    wx.TheClipboard.SetData(data_object)
def ex(calc):
    calc.Destroy() 
calc.Bind(wx.EVT_BUTTON, calculation, clbtn)
calc.Bind(wx.EVT_TEXT_ENTER, calculation, source=None, id=1)
calc.Bind(wx.EVT_TEXT_ENTER, calculation, source=None, id=10)
calc.Bind(wx.EVT_TEXT_ENTER, calculation, source=None, id=2)
calc.Bind(wx.EVT_BUTTON, clear, source=None, id=40)
calc.Bind(wx.EVT_BUTTON, copy, source=None, id=50)
calc.Bind(wx.EVT_BUTTON, ex, source=None, id=60)
calcgui.Show()
calc.MainLoop()
