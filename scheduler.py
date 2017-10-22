#!/usr/bin/python

import sys, getopt
from scheduler import *
import os

def main(argv):
   lpsolverfilepath = "lpsolverfiles/"
   iofilepath = ""
   try:
      opts, args = getopt.getopt(argv,"hp:",["path="])
   except getopt.GetoptError:
      print 'usage : python scheduler.py -p <input-file-path>'
      sys.exit(1)
   for opt, arg in opts:
      if opt == '-h':
         print 'python scheduler.py -p <input-file-path>'
         sys.exit()
      elif opt in ("-p", "--path"):
         iofilepath = arg
   
   fob = module_file.Fileoperation()      
   inp1,inp2,inp3,inp4,inp5 = fob.read_input(iofilepath+"input.txt") 
   gob = module_graph.OCG(inp1,None,inp2,inp3,inp4,inp5)
   
   rcob = module_ilp.ILPmodeller(gob)
   
   strn = rcob.resource_constraint()   
   fob.write_output(lpsolverfilepath+"lpinput.lp",strn) 
   
   os.system('lp_solve '+lpsolverfilepath+"lpinput.lp"+'>'+lpsolverfilepath+"lpoutput.txt")
   
   header = "o/p:\nTi\tOi\tRi\tDi\n----------------------------\n"
   result = fob.get_X_VAR(lpsolverfilepath+"lpoutput.txt")
   
   if result == -1:
   		print 'This problem is infeasible'
   else:
   		gob.update_ocg_Data(result)
		print header+gob.get_ocg_Data()
	   	fob.write_output(iofilepath+"output.txt",header+gob.get_ocg_Data())
	   	print "Output stored in '"+iofilepath+"output.txt'"
 

if __name__ == "__main__":
   main(sys.argv[1:])

