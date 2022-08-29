from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Form4')
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    username=self.text_box_1.text
    password=self.text_box_2.text
    mobile_no=self.text_box_4.text
    a=anvil.server.call('verifyuser',username,password,mobile_no)
    if(a==1):
      alert("YOUR PASSWORD IS WRONG PLEASE TRY AGAIN !!")
    if(a==2):
      alert("YOU ARE NEW USER PLEASE REGISTER FIRST",buttons=[
                 ("OK", open_form('Form1.Form4'))])
    open_form('Form1.Form5_copy')
    pass







