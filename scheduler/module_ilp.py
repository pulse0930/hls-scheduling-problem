class ILPmodeller:
	def __init__(self,gob):
		self.__n = gob.total_nodes()
		self.__lmbda = gob.get_lambda()
		self.__nR = gob.total_resources()
		self.__R = gob.get_rtype_Op()
		self.__a = gob.get_ak()
		self.__E = gob.get_dependencies()
		self.__record = []
		self.__gob = gob

	def display(self):
		print self.__n
		print self.__lmbda
		print self.__nR
		print self.__R
		print self.__a
		print self.__E
		print self.__record
		print self.__gob


	def resource_constraint(self):
		return self.__apply_objective() + "\n" + self.__apply_constraint1() + "\n" + self.__apply_constraint2() + "\n" + self.__apply_constraint3() + "\n" + self.__apply_bin()

	def __apply_objective(self):
		#objective	
		strn = "min: "
		i=self.__n-1
		for j in range (1,self.__lmbda+2):
			if (j == self.__lmbda+1):
				strn = strn + "%d * X%d%d0; "%(j,i,j)
			else:
				strn = strn + "%d * X%d%d0 + "%(j,i,j)
		return strn

	def __apply_constraint1(self):	
		#constraint:1  each operation has a unique start time
		#only 1 X[i][j][k] corresponding to i can be 1
		strn = ""		
		for i in range(self.__n):
			if i==0:
				strn = strn +  "\nX000 = 1;\n"
				continue
				
			for j in range(self.__lmbda+2):
				k = self.__gob.get_rtype_node(i)
				if j == self.__lmbda+1:
					strn = strn +  "X%d%d%d = "%(i,j,k)		 
				else:			
					strn = strn +  "X%d%d%d + "%(i,j,k) 
				self.__record.append("X%d%d%d"%(i,j,k))
			strn = strn +  "1;\n" 
		return strn

	def __apply_constraint2(self):
		#constraint:2 oQ must start after the result of oP p*X (oQ,oP) is an edge
		strn = ""
		for e in self.__E:
			q = e[1] 
			for j in range(1,self.__lmbda+2):
				if j == self.__lmbda+1:
					strn = strn +  "%d * X%d%d%d"%(j,q,j,self.__R[q]) 		
				else:
					strn = strn +   "%d * X%d%d%d + "%(j,q,j,self.__R[q])
				self.__record.append("X%d%d%d"%(q,j,self.__R[q]))

			strn = strn +  " - " 
			p = e[0]
			for j in range(1,self.__lmbda+2):
				if j == self.__lmbda+1:
					strn = strn +  "%d * X%d%d%d"%(j,p,j,self.__R[p]) 		
				else:
					strn = strn +   "%d * X%d%d%d - "%(j,p,j,self.__R[p])
				self.__record.append("X%d%d%d"%(p,j,self.__R[p])) 
			strn = strn + " - "+format(self.__gob.get_di_node(p))+ " >= 0;\n"
		return strn


	def __apply_constraint3(self):
		strn = ""
		for j in range(self.__lmbda+2):
			for k in range(self.__nR+1):
				var_list = self.__gob.get_nodes_rtype(k)
				for it,i in enumerate(var_list):
					if it < len(var_list)-1:
						strn = strn + '' if i == 0 and k == 0 else strn + "X%d%d%d + "%(i,j,k)
					else:
						strn = strn + "X%d%d%d "%(i,j,k)
					self.__record.append("X%d%d%d"%(i,j,k))
				strn = strn + " <= %d;\n"%self.__a[k]
			strn = strn + '\n'
		return "X000 + " + strn

	def __apply_bin(self):
		li = list(set(self.__record))
		li.sort()
		li.remove('X000')
		return "bin " + ",".join(str(x) for x in li ) + ";"
