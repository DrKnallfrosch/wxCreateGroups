import wx.grid
import gettext
import wx
_ = gettext.gettext


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame1(None)
        frame.SetMinSize((1000, 384))
        frame.Show(True)
        return True


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=_(u"Create Group"), pos=wx.DefaultPosition,
                          size=wx.Size(1000, 384), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.groups: dict[int, dict[str, list[str]]]

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        gSizer2 = wx.GridSizer(2, 3, 0, 0)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        gSizer2.Add(self.m_staticText9, 0, wx.ALL, 5)

        gSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_spinCtrl2 = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.SP_ARROW_KEYS, 0, 10, 0)
        gSizer2.Add(self.m_spinCtrl2, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        gSizer2.Add(self.m_staticText16, 0, wx.ALL, 5)

        gSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_spinCtrl1 = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.SP_ARROW_KEYS, 0, 10, 0)
        gSizer2.Add(self.m_spinCtrl1, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer2.Add(gSizer2, 1, wx.EXPAND, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"Groups")), wx.VERTICAL)

        self.m_grid1 = wx.grid.Grid(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(10, 2)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer1.Add(self.m_grid1, 0, wx.EXPAND, 5)

        bSizer2.Add(sbSizer1, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button4 = wx.Button(self, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0)

        bSizer8.Add(self.m_button4, 1, wx.RIGHT | wx.TOP, 5)
        self.m_button4.Bind(wx.EVT_BUTTON, self.current_size)

        self.m_button5 = wx.Button(self, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.Bind(wx.EVT_BUTTON, self.add_row)

        bSizer8.Add(self.m_button5, 1, wx.RIGHT | wx.TOP, 5)

        bSizer2.Add(bSizer8, 1, wx.ALIGN_RIGHT | wx.FIXED_MINSIZE, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def current_size(self, event):
        print(self.Size)

    def add_row(self, event):
        self.m_grid1.GetNumberRows()
        self.m_grid1.InsertRows(1)
        self.resize()

    def resize(self):
        new_size = self.GetSize()
        new_size[1] += 19
        self.Size = new_size

    def __del__(self):
        pass


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
