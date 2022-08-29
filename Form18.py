from ._anvil_designer import Form18Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form18(Form18Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def primary_color_1_click(self, **event_args):
    open_form('Form7')
    pass

  def primary_color_3_click(self, **event_args):
    open_form('Settingsform')
    pass

  def primary_color_2_click(self, **event_args):
 
    pass

  def primary_color_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form19')
    pass

  def primary_color_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form15')
    pass








