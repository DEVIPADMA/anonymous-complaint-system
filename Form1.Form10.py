from ._anvil_designer import Form10Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form10(Form10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    complaint_type=self.drop_down_1.selected_value
    file=self.file_loader_1.file
    desc=self.text_box_1.text
    identification=self.text_box_2.text
    loc=self.drop_down_2.selected_value
    anvil.server.call('addcomplaintinfo',complaint_type,file,desc,identification,loc)
    alert("YOUR COMPLAINT HAS BEEN SUBMITED")
    open_form('Form1.Form11')
    pass

  def primary_color_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form7')
    pass

  def primary_color_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Settingsform')
    pass

  def primary_color_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass





