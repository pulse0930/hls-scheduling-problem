class OCG:
	class Node:															
		def __init__(self, oid, cstep, rtype,di):						#constructor to set Node instance variables
			self.__oid = oid
			self.__cstep = cstep
			self.__rtype = rtype
			self.__di = di
		def set_oid(self,oid):												#operation id of an operation 		
		    self.__oid = oid

		def set_cstep(self,cstep):											#time step of an operation
		    self.__cstep = cstep

		def set_rtype(self,rtype):											#resource type of an operation
		    self.__rtype = rtype

		def get_oid(self):												#operation id of an operation 		
		    return self.__oid

		def get_cstep(self):											#time step of an operation
		    return self.__cstep

		def get_rtype(self):											#resource type of an operation
		    return self.__rtype

		def get_di(self):												#propagation delay of an operation
		    return self.__di


	def __init__(self,adj_mat, t_list, r_list, d_list,a_list, lmda):	#constructor to set OCG instance variables
		self.__adj_mat = adj_mat		
		self.__set_nodes(adj_mat,t_list,r_list,d_list)
		self.__set_dependencies(adj_mat)
		self.__a = a_list
		self.__d_list = d_list
		self.__lmda = lmda

	def __set_nodes(self,adj_mat,t_list,r_list,di_list):				#setter method for setting up all the nodes of OCG graph
				
		nodes=[]
		if t_list == None:
			t_list = [None for i in range(len(adj_mat))]
		if r_list == None:
			r_list = [None for i in range(len(adj_mat))]

		for i in range(len(adj_mat)):
			new_node = self.Node(i,t_list[i],r_list[i],di_list[i])		
			nodes.append(new_node)			
		self.__nodes = nodes		
	
	def get_nodes(self):											   #getter method for getting all nodes of OCG graph
		return self.__nodes

	def __set_dependencies(self,adj_mat):							   #setter method for setting edges between nodes of OCG graph
		dependencies = []
		for i, x in enumerate(adj_mat):
			for j in x:			
				if j == 1:
				    dependencies.append([i, x.index(j)])
				    adj_mat[i][x.index(j)] = 0	
		self.__dependencies = dependencies
		
	def get_dependencies(self):										   #getter method for getting all the edges between nodes of OCG graph
		dependencies = []
		return self.__dependencies

	def total_nodes(self):											   #method for finding total number of nodes of OCG graph
		return len(self.get_nodes())

	def total_dependencies(self):									   #method for finding total number edges available in OCG graph 
		return len(self.getdependencies())

	def total_resources(self):										   #method for finding total number of r_type assigned in OCG graph
		return max([i.get_rtype() for i in self.get_nodes()])

	def get_rtype_Op(self):											   #getter method for getting r_type assigned for each operations in OCG graph 
		return [i.get_rtype() for i in self.get_nodes()]

	def get_ak(self):#no_resource_rtype(self):				   #getter method for getting upper bound on number of resources of type k
		return self.__a

	def get_lambda(self):											   #represents a loose upper bound on the scheduled latency
		return self.__lmda

	def get_nodes_rtype(self,k):									   #getter method for getting all the operations using a particular r_type = k
		return [i.get_oid() for i in self.get_nodes() if i.get_rtype() == k]

	def get_rtype_node(self,oid):									   #getter method for getting r_type used by a particular operation
		for i in self.get_nodes():
			if i.get_oid() == oid:
				k = i.get_rtype()
				return k

	def get_di_node(self,oid): 			  						       #getter method for getting di for a particular operation
		for i in self.get_nodes():
			if i.get_oid() == oid:
				k = i.get_di()
				return k
	
	def get_ocg_Data(self):											   #getter method for getting the OCG graph data
		strn = ""
		li = [ [node.get_cstep(),'\t',node.get_oid(),'\t',node.get_rtype(),'\t',node.get_di() ] for node in self.get_nodes()]
		li.sort()		
		for i in li:
			strn = strn+''.join(map(str,i))+'\n'
		return strn

	def update_ocg_Data(self,updates):								   #method for updating the OCG graph data
		for i,node in enumerate(self.get_nodes()):
			oid = node.get_oid()
			if len(updates[i]) == 5 and oid == updates[i][0]*10+updates[i][1]:
				node.set_cstep(updates[i][2]*10+updates[i][3])			
			elif len(updates[i]) == 4 and oid == updates[i][0]:
				node.set_cstep(updates[i][1]*10+updates[i][2]) 		
			elif oid == updates[i][0]:
				node.set_cstep(updates[i][1])
