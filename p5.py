def check() :
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
 import p4 as bb
 print ('''
        1. Netflix
        2. Amazon
        3. Freecharge
        4. Blockchain
        5. Flipkart
        6. VPN
 ''') 		
 p = int(input ("Enter Checker ID (e.g - For Netflix Type 1) :   "))
 if p == 1:
   low = bb.checkers()
 elif p == 2:
   low2 = bb.checkersamz()
 else :
   print ("You have To Buy VIP Package from @rohantripathi0096")    