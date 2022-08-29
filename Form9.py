from ._anvil_designer import Form9Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form9(Form9Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    uname,create_p,con_p,mail,mobile,loc=anvil.server.call('retrieveregtable')
    self.label_4.text=uname
    self.label_6.text=create_p
    self.label_8.text=con_p
    self.label_10.text=mail
    self.label_12.text=mobile
    self.label_14.text=loc
    # Any code you write here will run when the form opens.
    

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def primary_color_3_click(self, **event_args):
    anvil.server.call('add_email_mobile',self.label_10.text,self.label_12.text)
    alert("THANK YOU!! \n You have successfully registered into ACS\n Please login to continue ",title="SUCCESSFULL REGISTRATION",large=True,buttons=[("OK",open_form('Form1.Form2'))])   
    pass


