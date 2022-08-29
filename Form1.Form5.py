from ._anvil_designer import Form5Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def primary_color_1_click(self, **event_args,):
    """This method is called when the button is clicked"""
    otp =self.text_box_1.text
    phno =self.text_box_2.text
    a=anvil.server.call('verifyotp',phno,otp)
    if a==1:
      open_form('Form1.Form9')
    else:
      alert("Wrong otp tr again!!")
    pass
 
