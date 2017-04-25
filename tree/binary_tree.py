class binaryNode(object):
	def __init__(self,key,value=None):
		self.key    = key
		self.value  = value
		self.left   = None
		self.right  = None
		self.parent	= None
		self.size   = 1

	def min_right(self):
		"""Returns minimum element from right subtree. 
		Returns None if right subtree does not exist."""
		prev = None
		current = self.right
		while current:
			prev = current
			current = current.left
		return prev

	def is_right(self):
		"""Returns True if self is the right child of another node."""
		return (self.parent is not None and self.parent.key < self.key)

	def set_left(self,node):
		"""Sets node to self.left, and self to node.parent."""
		if node is None:
			if self.left is not None:
				self.left.parent = None
			self.left = None
			return
		self.left = node
		node.parent = self

	def set_right(self,node):
		"""Sets node to self.right and self to node.parent."""
		if node is None:
			if self.right is not None:
				self.right.parent = None
			self.right = None
			return
		self.right = node
		node.parent = self

	def insert(self,key,value=None):
		"""Creates binaryNode(key,value) and inserts into subtree of self."""

		if key is None:
			raise ValueError('key must not be NoneType.')		

		newNode = binaryNode(key,value)
		current = self
		while current:
			if current.key == key:
				current.value = value
				return
			prev = current
			if current.key < key:
				current = current.right
			else:
				current = current.left
		if prev.key < key:
			prev.set_right(newNode)
		else:
			prev.set_left(newNode)
		self.size += 1

	def search(self,key):
		"""Binary search for key in subtree of self."""
		prev = None
		current = self
		while current:
			if current.key == key:
				return current
			prev = current
			if current.key < key:
				current = current.right
			else:
				current	= current.left
		# raise an error if not present; more pythonic way of exiting.
		raise KeyError('key not present in subtree of {}'.format(self))

	def isSorted(self,arr):
		for i in xrange(len(arr)-1):
			if arr[i] > arr[i+1]:
				return False
		return True

	def inOrder(self):
		"""Returns list of elements in subtree recovered by inOrder traversal."""
		
		stack = [self]
		ret = []
		current = self
		while stack:
			if current.left:
				current = current.left
				stack.append(current)
			else:
				while stack:
					current = stack.pop()
					ret.append(current)
					if current.right:
						current = current.right
						stack.append(current)
						break
		return ret

	def delete(self,key):
		"""Deletes node with key if exists in subtree and is not self."""
		
		try:
			node = self.search(key)
		except KeyError:
			return

		if node != None and node != self:
			self.size -= 1
			parent = node.parent
			if not node.left and not node.right:
				if parent.key < node.key:
					parent.right = None
				else:
					parent.left = None
			if node.left and not node.right:
				if parent.key < node.key:
					parent.set_right(node.left)
				else:
					parent.set_left(node.left)
				node.left        		= None
			if node.right and not node.left:
				if parent.key < node.key:
					parent.set_right(node.right)
				else:
					parent.set_left(node.right)
				node.right 	     	 	= None
			if node.right and node.left:
				minRight = node.min_right()
				Rparent  = minRight.parent
				if minRight == node.right:
					if parent.key < node.key:
						parent.set_right(minRight)
					else:
						parent.set_left(minRight)
					minRight.set_left(node.left)
					node.left 		 	 = None
					node.right       	 = None
				else:
					if minRight.right:
						Rparent.set_left(minRight.right)
						minRight.right   = None
					else:
						Rparent.left     = None
					if parent.key < node.key:
						parent.set_right(minRight)
					else:
						parent.set_left(minRight)
					minRight.set_left(node.left)
					minRight.set_right(node.right)
			del node
			return

	def __contains__(self,key):
		try: 
			self.search(key)
			return True
		except:
			return False

	def __repr__(self):
		return "binary tree node: key {}, value {}".format(self.key,self.value)

if __name__=='__main__':

	import numpy as np

	test_binary = False
	if test_binary:
		n = binaryNode(5)
		n.insert(None)
		print n.inOrder()