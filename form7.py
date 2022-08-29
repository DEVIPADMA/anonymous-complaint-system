from ._anvil_designer import Form7Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Form11')
    pass

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Form10')
    pass

  def primary_color_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form18')
    pass

  def primary_color_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def primary_color_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def primary_color_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form7')
    pass

  def primary_color_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Settingsform')
    pass
