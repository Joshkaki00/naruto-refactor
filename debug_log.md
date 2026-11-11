- I expected this to run and print out alert! Instead, the script returned a traceback at lines 8 and 18.

- Traceback error at lines 8 and 18

- Line 8

- The variable found is assigned later, so Python thinks it's a local variable. On the first loop iteration, line 8 reads found before any assignment, so it crashes with UnboundLocalError.