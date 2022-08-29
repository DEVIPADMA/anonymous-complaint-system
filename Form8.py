from ._anvil_designer import Form8Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form8(Form8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    uname,create_p,con_p,mail,loc=anvil.server.call('r_regtable')
    # Any code you write here will run when the form opens.
    self.label_4.text=uname
    self.label_6.text=create_p
    self.label_8.text=con_p
    self.label_10.text=mail
    self.label_13.text=loc

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    phno=self.text_box_1.text
    anvil.server.call('sendotpsms',phno)
    open_form('Form1.Form5')
    pass

  def primary_color_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("Please verify your mobile number!!",title="REQUIRED VERIFICATION ERROR",large=True)
    pass




