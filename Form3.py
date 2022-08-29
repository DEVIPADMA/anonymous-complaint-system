from ._anvil_designer import Form3Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    policestation_id=self.drop_down_1.selected_value
    password=self.text_box_1.text
    a=anvil.server.call('policeloginverification',policestation_id,password)
    if a==1:
      open_form('Form20')
    else:
      alert("Password doesn't match!!")
    anvil.server.call('addtocurrentlyloginpolice',policestation_id)
    pass


