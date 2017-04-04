
import platform

req_version = "2.7"
cur_version = platform.python_version()

if cur_version >= req_version and cur_version < "3.0":
   print("Current python version: "+cur_version)
   import Tkinter as tk
   import ttk as ttk
   import tkFileDialog as tkFileDialog
   import tkMessageBox as tkMessageBox

   #import myApp
   #myApp.run()

elif cur_version > "3.0":
    import tkinter as tk
    import tkinter.ttk as ttk
    import tkinter.filedialog as tkFileDialog
    import tkinter.messagebox as tkMessageBox

    # import myApp
    # myApp.run()

else:
    print("Current Python interpreter can not open this program.\n" +
          "This program can only work with Python versions between 2.7 and 3.0 .")



