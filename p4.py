  #  def start_new_thread(function, args, kwargs={}):
     #def start_new_thread(function, args, kwargs={}):
    #"""Dummy implementation of _thread.start_new_thread().

    #Compatibility is maintained by making sure that ``args`` is a
    #tuple and ``kwargs`` is a dictionary.  If an exception is raised
    #and it is SystemExit (which can be done by _thread.exit()) it is
    #caught and nothing is done; all other exceptions are printed out
    #by using traceback.print_exc().

    #If the executed function calls interrupt_main the KeyboardInterrupt will be
    #raised when the function returns.

    #"""
    #if type(args) != type(tuple()):
    #    raise TypeError("2nd arg must be a tuple")
    #if type(kwargs) != type(dict()):
    #    raise TypeError("3rd arg must be a dict")
    #global _main
    #_main = False
    #try:
     #   function(*args, **kwargs)
    #except SystemExit:
     #   pass
    #except:
     #   import traceback
     #   traceback.print_exc()
  #  _main = True
   # global _interrupt
   # if _interrupt:
   #     _interrupt = False
   #     raise KeyboardInterrupt
   # def exit():
   # """Dummy implementation of _thread.exit()."""
   # raise SystemExit
def checkers() :
 from sys import stdin
 import requests
 import uuid
 import socket
 from urllib.request import urlopen, Request
 class color:
     PURPLE = '\033[95m'
     CYAN = '\033[96m'
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
 f = open("../downloads/i.txt")
 line = f.readline()
 totalLines = len(f.readlines())
 f.close()
 f = open("../downloads/i.txt")
 lines = f.readlines()
 url = "https://mailsac.com/inbox/" + lines[0].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
   print (color.RED + "SCRAPPING " + color.END)
 else:
   print (color.RED + "SCRAPPED" + color.GREEN + lines[0] + color.END)

 url = "https://mailsac.com/inbox/" + lines[1].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
     print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[1] + color.END)
  
 url = "https://mailsac.com/inbox/" + lines[2].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[2] + color.END)

 url = "https://mailsac.com/inbox/" + lines[3].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[3] + color.END)

 url = "https://mailsac.com/inbox/" + lines[4].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[4] + color.END)


 url = "https://mailsac.com/inbox/" + lines[5].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[5] + color.END)



 url = "https://mailsac.com/inbox/" + lines[6].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[6] + color.END)



 url = "https://mailsac.com/inbox/" + lines[7].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[7] + color.END)



 url = "https://mailsac.com/inbox/" + lines[8].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[8] + color.END)



 url = "https://mailsac.com/inbox/" + lines[9].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[9] + color.END)



 url = "https://mailsac.com/inbox/" + lines[10].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[10] + color.END)



 url = "https://mailsac.com/inbox/" + lines[11].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[11] + color.END)



 url = "https://mailsac.com/inbox/" + lines[12].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[12] + color.END)


 url = "https://mailsac.com/inbox/" + lines[13].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[13] + color.END)



 url = "https://mailsac.com/inbox/" + lines[14].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[14] + color.END)



 url = "https://mailsac.com/inbox/" + lines[15].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[15] + color.END)




 url = "https://mailsac.com/inbox/" + lines[16].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[16] + color.END)



 url = "https://mailsac.com/inbox/" + lines[17].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[17] + color.END)



 url = "https://mailsac.com/inbox/" + lines[18].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[18] + color.END)




 url = "https://mailsac.com/inbox/" + lines[19].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[19] + color.END)



 url = "https://mailsac.com/inbox/" + lines[20].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[20] + color.END)



 url = "https://mailsac.com/inbox/" + lines[21].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[21] + color.END)



 url = "https://mailsac.com/inbox/" + lines[22].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[22] + color.END)



 url = "https://mailsac.com/inbox/" + lines[23].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[23] + color.END)



 url = "https://mailsac.com/inbox/" + lines[24].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[24] + color.END)



 url = "https://mailsac.com/inbox/" + lines[25].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print ('done')
    
 url = "https://mailsac.com/inbox/" + lines[26].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[26] + color.END)    
    
 url = "https://mailsac.com/inbox/" + lines[27].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[27] + color.END)
        
 url = "https://mailsac.com/inbox/" + lines[28].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[28] + color.END)


 url = "https://mailsac.com/inbox/" + lines[29].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[29] + color.END)

 url = "https://mailsac.com/inbox/" + lines[30].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[30] + color.END)


 url = "https://mailsac.com/inbox/" + lines[31].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[31] + color.END)


 url = "https://mailsac.com/inbox/" + lines[32].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[32] + color.END)



 url = "https://mailsac.com/inbox/" + lines[33].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[33] + color.END)



 url = "https://mailsac.com/inbox/" + lines[34].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[34] + color.END)



 url = "https://mailsac.com/inbox/" + lines[35].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[35] + color.END)


 url = "https://mailsac.com/inbox/" + lines[36].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[36] + color.END)


 url = "https://mailsac.com/inbox/" + lines[37].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[37] + color.END)

 url = "https://mailsac.com/inbox/" + lines[38].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[38] + color.END)


 url = "https://mailsac.com/inbox/" + lines[39].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[39] + color.END)


 url = "https://mailsac.com/inbox/" + lines[40].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[40] + color.END)


 url = "https://mailsac.com/inbox/" + lines[41].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[41] + color.END)

 url = "https://mailsac.com/inbox/" + lines[42].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[42] + color.END)


 url = "https://mailsac.com/inbox/" + lines[43].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[43] + color.END)


 url = "https://mailsac.com/inbox/" + lines[44].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[44] + color.END)


 url = "https://mailsac.com/inbox/" + lines[45].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[45] + color.END)


 url = "https://mailsac.com/inbox/" + lines[46].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[46] + color.END)

 url = "https://mailsac.com/inbox/" + lines[47].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[47] + color.END)


 url = "https://mailsac.com/inbox/" + lines[48].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[48] + color.END)


 url = "https://mailsac.com/inbox/" + lines[49].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[49] + color.END)


 url = "https://mailsac.com/inbox/" + lines[50].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[50] + color.END)


 url = "https://mailsac.com/inbox/" + lines[51].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[51] + color.END)


 url = "https://mailsac.com/inbox/" + lines[52].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[52] + color.END)


 url = "https://mailsac.com/inbox/" + lines[53].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[53] + color.END)


 url = "https://mailsac.com/inbox/" + lines[54].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[54] + color.END)


 url = "https://mailsac.com/inbox/" + lines[55].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[55] + color.END)


 url = "https://mailsac.com/inbox/" + lines[56].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[56] + color.END)


 url = "https://mailsac.com/inbox/" + lines[57].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[57] + color.END)


 url = "https://mailsac.com/inbox/" + lines[58].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[58] + color.END)


 url = "https://mailsac.com/inbox/" + lines[59].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[59] + color.END)


 url = "https://mailsac.com/inbox/" + lines[60].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[60] + color.END)


 url = "https://mailsac.com/inbox/" + lines[61].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[61] + color.END)


 url = "https://mailsac.com/inbox/" + lines[62].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[62] + color.END)

 url = "https://mailsac.com/inbox/" + lines[63].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[63] + color.END)

 url = "https://mailsac.com/inbox/" + lines[64].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[64] + color.END)


 url = "https://mailsac.com/inbox/" + lines[65].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[65] + color.END)


 url = "https://mailsac.com/inbox/" + lines[66].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[66] + color.END)


 url = "https://mailsac.com/inbox/" + lines[67].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[67] + color.END)

 url = "https://mailsac.com/inbox/" + lines[68].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[68] + color.END)


 url = "https://mailsac.com/inbox/" + lines[69].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[69] + color.END)

 url = "https://mailsac.com/inbox/" + lines[70].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[70] + color.END)


 url = "https://mailsac.com/inbox/" + lines[71].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[71] + color.END)


 url = "https://mailsac.com/inbox/" + lines[72].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[72] + color.END)


 url = "https://mailsac.com/inbox/" + lines[73].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[73] + color.END)


 url = "https://mailsac.com/inbox/" + lines[74].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[74] + color.END)


 url = "https://mailsac.com/inbox/" + lines[75].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[75] + color.END)

 url = "https://mailsac.com/inbox/" + lines[76].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[76] + color.END)


 url = "https://mailsac.com/inbox/" + lines[77].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[77] + color.END)


 url = "https://mailsac.com/inbox/" + lines[78].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[78] + color.END)


 url = "https://mailsac.com/inbox/" + lines[79].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[79] + color.END)

 url = "https://mailsac.com/inbox/" + lines[80].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[80] + color.END)

 url = "https://mailsac.com/inbox/" + lines[81].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[81] + color.END)

 url = "https://mailsac.com/inbox/" + lines[82].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[82] + color.END)

 url = "https://mailsac.com/inbox/" + lines[83].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[83] + color.END)

 url = "https://mailsac.com/inbox/" + lines[84].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[84] + color.END)


 url = "https://mailsac.com/inbox/" + lines[85].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[85] + color.END)


 url = "https://mailsac.com/inbox/" + lines[86].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[86] + color.END)


 url = "https://mailsac.com/inbox/" + lines[87].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[87] + color.END)


 url = "https://mailsac.com/inbox/" + lines[88].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[88] + color.END)

 url = "https://mailsac.com/inbox/" + lines[89].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[89] + color.END)

 url = "https://mailsac.com/inbox/" + lines[90].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[90] + color.END)

 url = "https://mailsac.com/inbox/" + lines[91].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[91] + color.END)

 url = "https://mailsac.com/inbox/" + lines[92].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[92] + color.END)


 url = "https://mailsac.com/inbox/" + lines[93].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[93] + color.END)


 url = "https://mailsac.com/inbox/" + lines[94].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[94] + color.END)


 url = "https://mailsac.com/inbox/" + lines[95].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[95] + color.END)


 url = "https://mailsac.com/inbox/" + lines[96].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[96] + color.END)


 url = "https://mailsac.com/inbox/" + lines[97].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[97] + color.END)


 url = "https://mailsac.com/inbox/" + lines[98].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[98] + color.END)


 url = "https://mailsac.com/inbox/" + lines[99].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[99] + color.END)


 url = "https://mailsac.com/inbox/" + lines[100].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[100] + color.END)


 url = "https://mailsac.com/inbox/" + lines[101].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[101] + color.END)


 url = "https://mailsac.com/inbox/" + lines[102].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[102] + color.END)


 url = "https://mailsac.com/inbox/" + lines[103].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[103] + color.END)


 url = "https://mailsac.com/inbox/" + lines[104].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[104] + color.END)


 url = "https://mailsac.com/inbox/" + lines[105].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[105] + color.END)


 url = "https://mailsac.com/inbox/" + lines[106].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[106] + color.END)


 url = "https://mailsac.com/inbox/" + lines[107].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[107] + color.END)


 url = "https://mailsac.com/inbox/" + lines[108].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[108] + color.END)


 url = "https://mailsac.com/inbox/" + lines[109].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[109] + color.END)


 url = "https://mailsac.com/inbox/" + lines[110].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[110] + color.END)


 url = "https://mailsac.com/inbox/" + lines[111].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[111] + color.END)


 url = "https://mailsac.com/inbox/" + lines[112].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[112] + color.END)


 url = "https://mailsac.com/inbox/" + lines[113].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[113] + color.END)


 url = "https://mailsac.com/inbox/" + lines[114].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[114] + color.END)


 url = "https://mailsac.com/inbox/" + lines[115].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[115] + color.END)


 url = "https://mailsac.com/inbox/" + lines[116].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[116] + color.END)


 url = "https://mailsac.com/inbox/" + lines[117].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[117] + color.END)

 url = "https://mailsac.com/inbox/" + lines[118].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[118] + color.END)

 url = "https://mailsac.com/inbox/" + lines[119].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[119] + color.END)

 url = "https://mailsac.com/inbox/" + lines[120].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[120] + color.END)

 url = "https://mailsac.com/inbox/" + lines[121].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[121] + color.END)

 url = "https://mailsac.com/inbox/" + lines[122].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[122] + color.END)


 url = "https://mailsac.com/inbox/" + lines[123].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[123] + color.END)

 url = "https://mailsac.com/inbox/" + lines[124].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[124] + color.END)


 url = "https://mailsac.com/inbox/" + lines[125].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[125] + color.END)

 url = "https://mailsac.com/inbox/" + lines[126].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[126] + color.END)


 url = "https://mailsac.com/inbox/" + lines[127].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[127] + color.END)


 url = "https://mailsac.com/inbox/" + lines[128].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[128] + color.END)

 url = "https://mailsac.com/inbox/" + lines[129].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[129] + color.END)

 url = "https://mailsac.com/inbox/" + lines[130].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[130] + color.END)

 url = "https://mailsac.com/inbox/" + lines[131].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[131] + color.END)


 url = "https://mailsac.com/inbox/" + lines[132].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[132] + color.END)


 url = "https://mailsac.com/inbox/" + lines[133].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[133] + color.END)


 url = "https://mailsac.com/inbox/" + lines[134].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[134] + color.END)

 url = "https://mailsac.com/inbox/" + lines[135].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[135] + color.END)


 url = "https://mailsac.com/inbox/" + lines[136].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[136] + color.END)


 url = "https://mailsac.com/inbox/" + lines[137].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[137] + color.END)

 url = "https://mailsac.com/inbox/" + lines[138].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[138] + color.END)

 url = "https://mailsac.com/inbox/" + lines[139].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[139] + color.END)

 url = "https://mailsac.com/inbox/" + lines[140].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[140] + color.END)


 url = "https://mailsac.com/inbox/" + lines[141].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[141] + color.END)


 url = "https://mailsac.com/inbox/" + lines[142].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[142] + color.END)


 url = "https://mailsac.com/inbox/" + lines[143].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[143] + color.END)


 url = "https://mailsac.com/inbox/" + lines[144].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[144] + color.END)


 url = "https://mailsac.com/inbox/" + lines[145].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[145] + color.END)

 url = "https://mailsac.com/inbox/" + lines[146].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[146] + color.END)

 url = "https://mailsac.com/inbox/" + lines[147].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[147] + color.END)

 url = "https://mailsac.com/inbox/" + lines[148].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[148] + color.END)

 url = "https://mailsac.com/inbox/" + lines[149].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[149] + color.END)

 url = "https://mailsac.com/inbox/" + lines[150].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[150] + color.END)

 url = "https://mailsac.com/inbox/" + lines[151].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[151] + color.END)

 url = "https://mailsac.com/inbox/" + lines[152].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[152] + color.END)

 url = "https://mailsac.com/inbox/" + lines[153].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[153] + color.END)

 url = "https://mailsac.com/inbox/" + lines[154].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[154] + color.END)

 url = "https://mailsac.com/inbox/" + lines[155].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[155] + color.END)

 url = "https://mailsac.com/inbox/" + lines[156].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[156] + color.END)

 url = "https://mailsac.com/inbox/" + lines[157].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[157] + color.END)


 url = "https://mailsac.com/inbox/" + lines[158].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[158] + color.END)


 url = "https://mailsac.com/inbox/" + lines[159].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[159] + color.END)


 url = "https://mailsac.com/inbox/" + lines[160].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[160] + color.END)


 url = "https://mailsac.com/inbox/" + lines[161].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[161] + color.END)


 url = "https://mailsac.com/inbox/" + lines[162].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[162] + color.END)

 url = "https://mailsac.com/inbox/" + lines[163].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[163] + color.END)


 url = "https://mailsac.com/inbox/" + lines[164].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[164] + color.END)


 url = "https://mailsac.com/inbox/" + lines[165].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[165] + color.END)


 url = "https://mailsac.com/inbox/" + lines[166].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[166] + color.END)


 url = "https://mailsac.com/inbox/" + lines[167].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[167] + color.END)


 url = "https://mailsac.com/inbox/" + lines[168].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[168] + color.END)


 url = "https://mailsac.com/inbox/" + lines[169].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[169] + color.END)


 url = "https://mailsac.com/inbox/" + lines[170].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[170] + color.END)



 url = "https://mailsac.com/inbox/" + lines[171].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[171] + color.END)


 url = "https://mailsac.com/inbox/" + lines[172].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[172] + color.END)



 url = "https://mailsac.com/inbox/" + lines[173].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[173] + color.END)



 url = "https://mailsac.com/inbox/" + lines[174].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[174] + color.END)



 url = "https://mailsac.com/inbox/" + lines[175].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[175] + color.END)



 url = "https://mailsac.com/inbox/" + lines[176].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[176] + color.END)


 url = "https://mailsac.com/inbox/" + lines[177].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[177] + color.END)


 url = "https://mailsac.com/inbox/" + lines[178].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[178] + color.END)


 url = "https://mailsac.com/inbox/" + lines[179].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[179] + color.END)


 url = "https://mailsac.com/inbox/" + lines[180].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[180] + color.END)


 url = "https://mailsac.com/inbox/" + lines[181].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[181] + color.END)


 url = "https://mailsac.com/inbox/" + lines[182].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[182] + color.END)


 url = "https://mailsac.com/inbox/" + lines[183].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[183] + color.END)


 url = "https://mailsac.com/inbox/" + lines[184].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[184] + color.END)


 url = "https://mailsac.com/inbox/" + lines[185].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[185] + color.END)

 url = "https://mailsac.com/inbox/" + lines[186].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[186] + color.END)


 url = "https://mailsac.com/inbox/" + lines[187].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[187] + color.END)


 url = "https://mailsac.com/inbox/" + lines[188].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[188] + color.END)



 url = "https://mailsac.com/inbox/" + lines[189].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[189] + color.END)



 url = "https://mailsac.com/inbox/" + lines[190].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[190] + color.END)

 url = "https://mailsac.com/inbox/" + lines[191].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[191] + color.END)


 url = "https://mailsac.com/inbox/" + lines[192].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[192] + color.END)

 url = "https://mailsac.com/inbox/" + lines[193].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[193] + color.END)

 url = "https://mailsac.com/inbox/" + lines[194].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[194] + color.END)


 url = "https://mailsac.com/inbox/" + lines[195].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[195] + color.END)

 url = "https://mailsac.com/inbox/" + lines[196].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[196] + color.END)


 url = "https://mailsac.com/inbox/" + lines[197].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[197] + color.END)


 url = "https://mailsac.com/inbox/" + lines[198].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[198] + color.END)


 url = "https://mailsac.com/inbox/" + lines[199].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[199] + color.END)


 url = "https://mailsac.com/inbox/" + lines[200].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('netflix')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[200] + color.END)

    

def checkersamz() :
 from sys import stdin
 import requests
 import uuid
 import socket
 from urllib.request import urlopen, Request
 class color:
     PURPLE = '\033[95m'
     CYAN = '\033[96m'
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
 f = open("../downloads/i.txt")
 line = f.readline()
 totalLines = len(f.readlines())
 f.close()
 f = open("../downloads/i.txt")
 lines = f.readlines()
 url = "https://mailsac.com/inbox/" + lines[0].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
   print (color.RED + "SCRAPPING " + color.END)
 else:
   print (color.RED + "SCRAPPED" + color.GREEN + lines[0] + color.END)

 url = "https://mailsac.com/inbox/" + lines[1].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
     print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[1] + color.END)
  
 url = "https://mailsac.com/inbox/" + lines[2].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[2] + color.END)

 url = "https://mailsac.com/inbox/" + lines[3].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[3] + color.END)

 url = "https://mailsac.com/inbox/" + lines[4].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[4] + color.END)


 url = "https://mailsac.com/inbox/" + lines[5].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[5] + color.END)



 url = "https://mailsac.com/inbox/" + lines[6].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[6] + color.END)



 url = "https://mailsac.com/inbox/" + lines[7].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[7] + color.END)



 url = "https://mailsac.com/inbox/" + lines[8].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[8] + color.END)



 url = "https://mailsac.com/inbox/" + lines[9].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[9] + color.END)



 url = "https://mailsac.com/inbox/" + lines[10].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[10] + color.END)



 url = "https://mailsac.com/inbox/" + lines[11].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[11] + color.END)



 url = "https://mailsac.com/inbox/" + lines[12].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[12] + color.END)


 url = "https://mailsac.com/inbox/" + lines[13].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[13] + color.END)



 url = "https://mailsac.com/inbox/" + lines[14].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[14] + color.END)



 url = "https://mailsac.com/inbox/" + lines[15].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[15] + color.END)




 url = "https://mailsac.com/inbox/" + lines[16].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[16] + color.END)



 url = "https://mailsac.com/inbox/" + lines[17].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[17] + color.END)



 url = "https://mailsac.com/inbox/" + lines[18].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[18] + color.END)




 url = "https://mailsac.com/inbox/" + lines[19].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[19] + color.END)



 url = "https://mailsac.com/inbox/" + lines[20].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[20] + color.END)



 url = "https://mailsac.com/inbox/" + lines[21].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[21] + color.END)



 url = "https://mailsac.com/inbox/" + lines[22].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[22] + color.END)



 url = "https://mailsac.com/inbox/" + lines[23].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[23] + color.END)



 url = "https://mailsac.com/inbox/" + lines[24].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print (color.RED + "SCRAPPED" + color.GREEN + lines[24] + color.END)



 url = "https://mailsac.com/inbox/" + lines[25].strip()+ '@mailsac.com'
 r = requests.get(url)
 text = r.text
 result = text.find('amazon')
 if result == -1:
    print (color.RED + "SCRAPPING " + color.END)
 else:
    print ('done')