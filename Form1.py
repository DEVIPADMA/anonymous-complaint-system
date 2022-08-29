from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    Usertype=self.drop_down_1.selected_value;
    if Usertype=="PUBLIC USER":
      open_form('Form1.Form2')
    if Usertype=="POLICE USER":
      open_form('Form3')
    pass



  
  




