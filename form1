from ._anvil_designer import Form21Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date
  
from anvil.js.window import DailyIframe

class Form21(Form21Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def primary_color_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    dat=self.date_picker_1.date
    self.date_picker_1.max_date = date.today()
    anvil.server.call('get_file',dat)
    alert("COMPLAINTS FILED ON YOUR SELECTED DATE WAS SEND TO YOUR EMAIL")
    pass

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form20')
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

