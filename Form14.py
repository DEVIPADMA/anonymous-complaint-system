from ._anvil_designer import Form14Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil.js.window import DailyIframe

class Form14(Form14Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def start_call_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    room_name = self.room_name_textbox.text
    if room_name:
      self.call_frame = DailyIframe.createFrame()
      try:
        self.start_call_button.visible = False
        self.end_call_button.visible= True
        self.call_frame.join({ 'url': 'https://y99.in/web/desktop/discover'})
      except Exception as e:
        if "The meeting you're trying to join does not exist" in str(e):
          alert("That room doesn't exist.")
          self.end_call_button_click()
        else:
          raise
      
    


  def end_call_button_click(self, **event_args):
    room_name = self.room_name_textbox.text
    self.call_frame.leave({ 'url': 'https://y99.in/web/desktop/discover'})
    self.call_frame.destroy({ 'url': 'https://y99.in/web/desktop/discover' })

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form7')
    pass

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Settingsform')
    pass



  
