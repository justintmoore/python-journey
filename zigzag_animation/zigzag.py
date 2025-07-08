import time
import sys

indent = 0
indentIncreasing = True # Flag Variable used to control the while loops

try:
    while True:  # Never ending
        print(' ' * indent, end='')  # Prints space multiplied by indent number
        print('********')
        time.sleep(0.1)  # Pauses 10th of a second

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False  # If it reaches the max indent, set to false, so it can drop to "else" block
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True  # Vice Versa
except KeyboardInterrupt:  # KeyboardInterrupt is the exception raise when a user presses Ctrl+C
    sys.exit()  # Terminates Python interpreter

# Output
PS C:\Users\...
********
 ********
  ********
   ********
    ********
     ********
      ********
       ********
        ********
         ********
          ********
           ********
            ********
             ********
              ********
               ********
                ********
                 ********
                  ********
                   ********
                    ********
                   ********
                  ********
                 ********
                ********
               ********
              ********
             ********
            ********
           ********
          ********
         ********
        ********
       ********
      ********
     ********
    ********
   ********
  ********
 ********
********
 ********
  ********
   ********
    ********
     ********
      ********
       ********
        ********
         ********
          ********
           ********
            ********
             ********
              ********
               ********
                ********
                 ********
                  ********
                   ********
                    ********
