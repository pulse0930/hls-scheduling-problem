import re
class Fileoperation:
	def read_input(self,inputfile):
		  inp1 = []
		  count = 0
		  f = open(inputfile,"r")
		  for i in f.readlines():
		  		li = map(int,re.findall(r'\d+',i))
		  		if li == []:
		  			count += 1
		  			continue
		  		if count == 2:
		  			inp2 = li
		  		elif count == 3:
		  			inp3 = li
		  		elif count == 4:
		  			inp4 = li
		  		elif count == 5:
		  			inp5 = li[0]
		  		else:
		  			inp1.append(li)	  		
	   	  return inp1,inp2,inp3,inp4,inp5
    
	def write_output(self,outputfile,strn):
	   f = open(outputfile,"w")
	   f.write(strn)

	def get_X_VAR(self,inputfile):
	   f = open(inputfile,"r")
	   li = []
	   for i in f.readlines():
	   		if i == 'This problem is infeasible\n':
	   			return -1
			if re.search(r'(\d+) (\s+1)',i):
				match = re.search(r'(\d+) (\s+1)',i)
				li.append(map(int,match.group(1)))
	   li.sort()
	   li = sorted(li,key=len)
	   return li 
