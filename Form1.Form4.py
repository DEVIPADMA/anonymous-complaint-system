from ._anvil_designer import Form4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    reg_id=random.randint(1000,9999)
    username=self.text_box_1.text
    if(len(username)<8):
      alert("Usename must have atleast 8 characters!!",title="INVALID USERNAME")
    create_password=self.text_box_2.text
    if(len(create_password)<8):
      alert("Password must have atleast 8 characters and 1 number!!",title="INVALID PASSWORD")
    confirmpassword=self.text_box_3.text
    if(create_password==confirmpassword):
      email=self.text_box_4.text
      a=anvil.server.call('validateemail',email)
      if(a==1):
        alert("INVALID EMAILID PLEASE TRY AGAIN!!",title="INVALID EMAIL ADDRESS")
      else:
        location=self.drop_down_1.selected_value
        anvil.server.call('sendmail',email)
        mobile_no=self.text_box_6.text
        anvil.server.call('addtoregistertable',reg_id,username,create_password,confirmpassword,email,mobile_no,location)
        open_form('Form1.Form6')
    else:
      alert("Password doesn't match!!! Try again",title="Password Match Error",large=True)
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Form2')
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass



