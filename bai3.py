from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#
# This is the Python code that makes this feedback form work.
# It's a Python class, with a method that runs when the user
# clicks the SUBMIT button.
#
# When the button is clicked, we send the contents of the
# text boxes to our Server Module. The Server Module records
# the feedback in the database, and sends an email to the
# app's owner (that's you!).
#
# To find the Server Module, look under "Server Code" on the
# left.
#
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

class HomeForm(HomeFormTemplate):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  
  def selection_sort(self,arr):
      n = len(arr)
      for i in range(n):
          min_idx = i
          for j in range(i+1, n):
              if arr[j] < arr[min_idx]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
  
  def bubble_sort(self,arr):
      n = len(arr)
      for i in range(n):
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
  
  def merge_sort(self,arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  def submit_button_click(self, **event_args):
    num_text = self.nums_box.text
    num_list = num_text.split()  # Tách chuỗi thành danh sách các chuỗi con
    try:
        num_list = [int(num) for num in num_list]  # Chuyển đổi từng chuỗi thành số nguyên
    except ValueError:
        print("Danh sách chứa các phần tử không phải là số nguyên")
        return

    # Sắp xếp danh sách
    insertion_sort(num_list)

    # Hiển thị danh sách đã sắp xếp
    sorted_text = ', '.join(map(str, num_list))
    self.result_box.text = sorted_text

    # Thông báo cho người dùng biết rằng đã sắp xếp xong
    Notification("Đã sắp xếp danh sách").show()

    # Xóa ô nhập liệu
    self.clear_inputs()

  def clear_inputs(self):
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""

