def sep():
  import hashlib
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
  print (color.BOLD + '' + color.END)
  print (color.BLUE + '''
              +++++++++++++++++++++++++++++++
              +  +      + +++++  +     ++
              +  +  +   + +    + +    +  +
              +  +    + + +    + +   ++++++
              +  +      + + +++  +  +      +
             +++++++++++++++++++++++++++++++++
 ''' + color.END)
  print("\033[1;31;40m             VTB ₴₦ł₣₣ł₦₲ ₮ØØⱠ ₳₦Đ ฿ⱤɄ₮Ɇ₣ØⱤ₵ɆⱤ         \033[0m")
  print("\033[1;31;40m             **********************************      \033[0m")
  key = input ("Key: ")
  keyvalid = hashlib.md5(key.encode())   
  keyvalidp = keyvalid.hexdigest()
  login = 'cddaa6e1ad5ba4c70c6c05db38099fa0'
  print (keyvalidp)
  if keyvalidp == login :
    print (color.CYAN + ''' 
           ++++++++++++++++++++++++++++++++++++
           +++++++Logged in Successfully+++++++
           ++++++++++++++++++++++++++++++++++++
    ''' + color.END)
    	     	 
  else :
    print (color.RED + 'LOL. ITS ENCRYPTED. contact @rohantripathi0096')
    exit()
    

def start():
 print ('''
    +++++++++++++++++++++++++++++++++++
     Starting NETFLIX SCRAPPER
    +++++++++++++++++++++++++++++++++++
     CODED BY : VIKASHTHEBRAINER
    +++++++++++++++++++++++++++++++++++
     FATHER OF BINS
    +++++++++++++++++++++++++++++++++++
     YOU CREATE I WILL STEAL
    ++++++++++++++++++++++++++++++++++++
     BA BA BLACK SHEEP 
    +++++++++++++++!!!!+++++++++++++++++
     DEVELOPED WITHIN 2HR
    ++++++++±+++++++++++++++++++++++++++
     USE FOR ILLEGAL PURPOSE
    ++++++++++++++++++++++++++++++++++++
    ENCRYPTED SOURCE CODE WITH ADVANCE IN
    PROGRAM SECURITY
    +++++++++++++++++++++++++++++++++++++
    HOW'S THE JOSH?
    +++++++++++++++++++++++++++++++++++++
    BUY:  CONTACT Telegram @rohantripathi0096
    +++++++++++++++++++++++++++++++++++++
    YOU HAVE BASIC PACKAGE : 25 KEYWORDS 
    +++++++++++++++++++++++++++++++++++++
    VIP PACKAGE : 1000 KEYWORDS. UPGRADE CONTACT
    +++++++++++++++++++++++++++++++++++++
    PREMIUM PACKAGE : 200 KEYWORDS 
    ++++++++++++++++++++++++++++++++++++++
    SUPER VIP PACKAGE : 10000 KEYWORDS
    +++++++++++++++++++++++++++++++++++++
''')