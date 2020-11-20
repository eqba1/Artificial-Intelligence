import math

class State():

	def __init__(self,leftCan,leftMis,boat,rightCan,rightMis):
		self.leftCan = leftCan
		self.leftMis = leftMis
		self.boat = boat
		self.rightCan = rightCan
		self.rightMis = rightMis
		self.parent = None

	
	def isGoal(self):
		if self.leftCan == 0 and self.leftMis == 0:
			return True
		return False

	def valid_State(self):
		if self.leftCan>=0 and self.rightCan>=0 \
		and self.leftMis>=0 and self.rightMis>=0 \
		and (self.rightMis==0 or self.rightMis>=self.rightCan) \
		and (self.leftMis==0 or self.leftMis>=self.leftCan):
			return True
		return False


def successors(current_state):
	
	children = []
	if current_state.boat == 'LEFT':
		new_state = State(current_state.leftCan, current_state.leftMis - 2, 'RIGHT',
								  current_state.rightCan, current_state.rightMis + 2)
		# MM-->
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan - 2, current_state.leftMis, 'RIGHT',
								  current_state.rightCan + 2, current_state.rightMis)
		# CC -->
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan - 1, current_state.leftMis - 1, 'RIGHT',
								  current_state.rightCan + 1, current_state.rightMis + 1)
		# MC -->
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan, current_state.leftMis - 1, 'RIGHT',
								  current_state.rightCan, current_state.rightMis + 1)
		# M -->
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan - 1, current_state.leftMis, 'RIGHT',
								  current_state.rightCan + 1, current_state.rightMis)
		# C -->
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
	else:
		new_state = State(current_state.leftCan, current_state.leftMis + 2, 'LEFT',
								  current_state.rightCan, current_state.rightMis - 2)
		# <-- MM
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan + 2, current_state.leftMis, 'LEFT',
								  current_state.rightCan - 2, current_state.rightMis)
		## <--CC
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan + 1, current_state.leftMis + 1, 'LEFT',
								  current_state.rightCan - 1, current_state.rightMis - 1)
		# <-- CM
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan, current_state.leftMis + 1, 'LEFT',
								  current_state.rightCan, current_state.rightMis - 1)
		# <-- M
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
		new_state = State(current_state.leftCan + 1, current_state.leftMis, 'LEFT',
								  current_state.rightCan - 1, current_state.rightMis)
		# <--C
		if new_state.valid_State():
			new_state.parent = current_state
			children.append(new_state)
	return children

def BFS():
	init_state = State(3,3,'LEFT',0,0)

	if init_state.isGoal(): #for completness reasons
		return init_state

	queue = list()
	explored = set()
	queue.append(init_state)

	while queue:
		state = queue.pop(0)
		if state.isGoal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in queue):
				queue.append(child)
	return None


def print_path(solution):
	path = list()
	path.append(solution)
	parent = solution.parent
	while parent:
		path.append(parent)
		parent = parent.parent

	steps = len(path)
	for i in range(len(path)):
		state = path[len(path)-i-1]
		print((state.leftCan),(state.leftMis),state.boat,(state.rightCan),(state.rightMis))
	
	print("Num of Steps: ", steps) 

if __name__ == "__main__":
	print("Solution to the Cannibals and Missionaries problem")
	solution = BFS()
	print_path(solution)