from ._anvil_designer import Form15Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form15(Form15Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def primary_color_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    msg=self.text_box_1.text
    anvil.server.call('choose_video_room')
    anvil.server.call('send_request',msg)
    alert("YOUR REQUEST FOR VIDEO CONVERSATION HAS BEEN SEND!! PLEASE WAIT RESPONSE FROM POLICE",large=True)
    open_form('Form12')
    pass

  def primary_color_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('choose_voice_room')
    anvil.server.call('send_voicerequest',msg)
    alert("YOUR REQUEST FOR VOICE CONVERSATION HAS BEEN SEND!! PLEASE WAIT RESPONSE FROM POLICE",large=True)
    open_form('Form12')
    pass

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form7')
    pass

  def primary_color_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Settingsform')
    pass

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    msg=self.text_box_1.text
    anvil.server.call('choose_voice_room')
    anvil.server.call('text_request',msg)
    alert("YOUR REQUEST FOR TEXT CONVERSATION HAS BEEN SEND!! PLEASE WAIT RESPONSE FROM POLICE",large=True)
    pass






