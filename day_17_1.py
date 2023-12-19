from heapq import heappop, heappush

import itertools
import sys

class Node:
	def __init__(self, coords, loss):
		self.accumulated_loss = {}
		self.coords = coords
		self.loss = loss
		self.neighbors = []

class PriorityQueue:
	def __init__(self):
		self.REMOVED = 'REMOVED'
		self.counter = itertools.count()
		self.finder = {}
		self.queue = []

	def __len__(self):
		return len(self.queue)

	def add(self, item, priority):
		if item in self.finder:
			self.remove(item)

		count = next(self.counter)
		e = [priority, count, item]

		self.finder[item] = e

		heappush(self.queue, e)

	def pop(self):
		while len(self.queue) > 0:
			priority, count, item = heappop(self.queue)

			if item is not self.REMOVED:
				del self.finder[item]

				return item

		raise KeyError('Can\'t pop from an empty priority queue.')

	def remove(self, item):
		e = self.finder.pop(item)
		e[-1] = self.REMOVED

def traverse(nodes, priority_queue):
	w = len(grid[0])
	h = len(grid)
	visited = set()

	while len(priority_queue) > 0:
		triple = priority_queue.pop()

		if triple in visited:
			continue

		visited.add(triple)
		current, v, straight = triple
		key = (v[0], v[1], straight)
		accumulated = current.accumulated_loss[key]

		if current.coords == (w - 1, h - 1):
			return accumulated

		eX, eY = triple[1]

		for neighbor in current.neighbors:
			vX = neighbor.coords[0] - current.coords[0]
			vY = neighbor.coords[1] - current.coords[1]

			if (vX != 0 and vX == -eX) or (vY != 0 and vY == -eY):
				continue

			straight = 1 if eX * vX + eY * vY == 0 else triple[2] + 1

			if straight == 4:
				continue

			key = (vX, vY, straight)
			stored = neighbor.accumulated_loss[key] if key in neighbor.accumulated_loss else sys.maxsize
			tentative = neighbor.loss + accumulated

			if tentative < stored:
				neighbor.accumulated_loss[key] = tentative
				priority_queue.add((neighbor, (vX, vY), straight), tentative)

grid = []

with open('day_17.txt') as f:
	for line in f:
		grid.append([int(c) for c in line.rstrip()])

size = len(grid)
nodes = {}
w = len(grid[0])
h = len(grid)

for y in range(h):
	for x in range(w):
		nodes[(x, y)] = Node((x, y), grid[y][x])

for y in range(h):
	for x in range(w):
		neighbors = nodes[(x, y)].neighbors

		if x > 0:
			neighbors.append(nodes[(x - 1, y)])

		if x < w - 1:
			neighbors.append(nodes[(x + 1, y)])

		if y > 0:
			neighbors.append(nodes[(x, y - 1)])

		if y < h - 1:
			neighbors.append(nodes[(x, y + 1)])

start = nodes[(0, 0)]
start.accumulated_loss[(1, 0, 0)] = 0
start.accumulated_loss[(0, 1, 0)] = 0
priority_queue = PriorityQueue()
priority_queue.add((start, (1, 0), 0), 0)
priority_queue.add((start, (0, 1), 0), 0)

print(traverse(nodes, priority_queue))
