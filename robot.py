import wx
import gui
from EmuControl import Emu

class RobotFrame(gui.Mainframe):
	"""Class til GUI"""
	def __init__(self,parent):
		gui.Mainframe.__init__(self,parent)
		self.valgtId = 0

	def close_func( self, event ):
		self.Close()

	def findid_func( self, event ):
		Emu.start(self)
		self.ids = Emu.scanUnits(self)
		choice_values = []
		for id in self.ids:
			choice_values.append(str(id))
			Emu.jointMode(self, id)
			Emu.moveJoint(self,id, 0)
			pos = Emu.getPos(self, id)
			self.txtTest.AppendText(str(id)+': '+str(pos)+'\r')
		self.choice_id.SetItems(choice_values)

	def mode_select_func( self, event ):
		valg = self.radio_mode.GetSelection()
		if valg == 0:
			self.btn_koer.Enable(True)
			self.btn_stop.Enable(True)
			self.btn_bak.Enable(True)
			self.btn_m45.Enable(False)
			self.btn_p45.Enable(False)
			self.btn_midt.Enable(False)
			for id in self.ids:
				Emu.wheelMode(self, id)
		if valg == 1:
			self.btn_koer.Enable(False)
			self.btn_stop.Enable(False)
			self.btn_bak.Enable(False)
			self.btn_m45.Enable(True)
			self.btn_p45.Enable(True)
			self.btn_midt.Enable(True)
			for id in self.ids:
				Emu.jointMode(self, id)
				Emu.moveJoint(self, id, 0)

	def drive_func( self, event ):
		for id in self.ids:
			Emu.moveWheel(self,id,200)

	def stop_func( self, event ):
		for id in self.ids:
			Emu.moveWheel(self,id,0)

	def tilbage_func( self, event ):
		for id in self.ids:
			Emu.moveWheel(self, id, -200)

	def m45_func( self, event ):
		for id in self.ids:
			Emu.moveJoint(self,id, -45)
			pos = Emu.getPos(self, id)
			self.txtTest.AppendText(str(id) + ': ' + str(pos) + '\r')

	def p45_func( self, event ):
		for id in self.ids:
			Emu.moveJoint(self, id, 45)
			pos = Emu.getPos(self, id)
			self.txtTest.AppendText(str(id) + ': ' + str(pos) + '\r')

	def midt_func( self, event ):
		for id in self.ids:
			Emu.moveJoint(self, id, 0)
			pos = Emu.getPos(self, id)
			self.txtTest.AppendText(str(id) + ': ' + str(pos) + '\r')

	def select_id( self, event ):
		self.valgtId= int(self.choice_id.GetStringSelection())
		self.spinPos.Value = 0

	def turn( self, event ):
		# Dette giver problemer i wxPython GUI'en, men ikke som rent kommendoprompt
		vpos = self.spinPos.GetValue()
		Emu.moveJoint(self, self.valgtId, vpos)
		pos = Emu.getPos(self, self.valgtId)
		self.txtTest.AppendText(str(self.valgtId) + ': ' + str(pos) + '\r')

app = wx.App(False)
frame = RobotFrame(None)
frame.Show(True)
#app.MainLoop()
