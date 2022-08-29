from ._anvil_designer import Form6Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form6(Form6Template):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def primary_color_1_click(self, **event_args):
    otp = self.text_box_1.text
    mail = self.text_box_2.text
    a=anvil.server.call('verifyotp',mail,otp)
    if(a==1):
      open_form('Form1.Form8')
    else:
      alert("WRONG OTP TRY AGAIN!!")
    pass

