# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Mainframe
###########################################################################

class Mainframe ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Test af Dynamixels", pos = wx.DefaultPosition, size = wx.Size( 574,552 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.btn_checkid = wx.Button( self, wx.ID_ANY, u"Find ID'er", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btn_checkid, 0, wx.ALL, 5 )

		self.txtTest = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,200 ), wx.TE_MULTILINE|wx.VSCROLL )
		fgSizer1.Add( self.txtTest, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer1, 0, wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Vælg mode" ), wx.VERTICAL )

		radio_modeChoices = [ u"Wheel", u"Joint" ]
		self.radio_mode = wx.RadioBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Modes", wx.DefaultPosition, wx.DefaultSize, radio_modeChoices, 1, wx.RA_SPECIFY_COLS )
		self.radio_mode.SetSelection( 1 )
		sbSizer1.Add( self.radio_mode, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer1, 0, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.btn_koer = wx.Button( self, wx.ID_ANY, u"Kør", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_koer.Enable( False )

		fgSizer2.Add( self.btn_koer, 0, wx.ALL, 5 )

		self.btn_stop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_stop.Enable( False )

		fgSizer2.Add( self.btn_stop, 0, wx.ALL, 5 )

		self.btn_bak = wx.Button( self, wx.ID_ANY, u"Tilbage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_bak.Enable( False )

		fgSizer2.Add( self.btn_bak, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer2, 0, wx.EXPAND, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.btn_m45 = wx.Button( self, wx.ID_ANY, u"-45", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.btn_m45, 0, wx.ALL, 5 )

		self.btn_midt = wx.Button( self, wx.ID_ANY, u"Midt", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.btn_midt, 0, wx.ALL, 5 )

		self.btn_p45 = wx.Button( self, wx.ID_ANY, u"+45", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.btn_p45, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Vælg ID, der skal drejes:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		choice_idChoices = [ u"1", u"2" ]
		self.choice_id = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_idChoices, 0 )
		self.choice_id.SetSelection( 0 )
		bSizer5.Add( self.choice_id, 0, wx.ALL, 5 )

		self.spinPos = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, -180, 180, 0, 5 )
		self.spinPos.SetDigits( 0 )
		bSizer5.Add( self.spinPos, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.close_func, id = self.m_menuItem1.GetId() )
		self.btn_checkid.Bind( wx.EVT_BUTTON, self.findid_func )
		self.radio_mode.Bind( wx.EVT_RADIOBOX, self.mode_select_func )
		self.btn_koer.Bind( wx.EVT_BUTTON, self.drive_func )
		self.btn_stop.Bind( wx.EVT_BUTTON, self.stop_func )
		self.btn_bak.Bind( wx.EVT_BUTTON, self.tilbage_func )
		self.btn_m45.Bind( wx.EVT_BUTTON, self.m45_func )
		self.btn_midt.Bind( wx.EVT_BUTTON, self.midt_func )
		self.btn_p45.Bind( wx.EVT_BUTTON, self.p45_func )
		self.choice_id.Bind( wx.EVT_CHOICE, self.select_id )
		self.spinPos.Bind( wx.EVT_SPINCTRLDOUBLE, self.turn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close_func( self, event ):
		event.Skip()

	def findid_func( self, event ):
		event.Skip()

	def mode_select_func( self, event ):
		event.Skip()

	def drive_func( self, event ):
		event.Skip()

	def stop_func( self, event ):
		event.Skip()

	def tilbage_func( self, event ):
		event.Skip()

	def m45_func( self, event ):
		event.Skip()

	def midt_func( self, event ):
		event.Skip()

	def p45_func( self, event ):
		event.Skip()

	def select_id( self, event ):
		event.Skip()

	def turn( self, event ):
		event.Skip()


