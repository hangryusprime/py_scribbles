import sys
import time
from random import random, randint
from math import sqrt, pi
from multiprocessing import Pool, cpu_count, Process


def compute_pi(n, id=1):
	i, inside = 0, 0
	while i < n:
		x = random()
		y = random()
		if sqrt(x*x + y*y) <= 1:
			inside += 1
		i += 1
	ratio = 4.0*inside / n
	time.sleep(randint(1,15))
	print(f'Id: {id}, My pi: {ratio}, Error: {ratio - pi}')
	sys.exit()


def mp1():
	numbers = [10000000]*50
	usable_cores = max(cpu_count()-1, 1)
	print(f'Using {usable_cores} cores')
	time_exec = time.time()
	start = 0
	jobs = []
	while len(numbers) > 0:
		index = 0
		if len(numbers) > usable_cores:
			for i in range(0, usable_cores):
				p = Process(target=compute_pi, args=(numbers[i],start + index))
				index += 1
				p.start()
				jobs.append(p)
		else:
			for i in numbers:
				p = Process(target=compute_pi, args=(i,start + index))
				index += 1
				p.start()
				jobs.append(p)
		time.sleep(10)
		start += usable_cores
		if len(numbers) >= usable_cores:
			numbers = numbers[usable_cores:]
		else:
			numbers = []
	time_exec = time.time() - time_exec
	print(f"Finished processing data in {round(time_exec, 3)} sec")
	return jobs


def mp2():
	numbers = [10000000]*50
	usable_cores = max(cpu_count()-1, 1)
	# usable_cores = 5
	print(f'Using {usable_cores} cores')
	time_exec = time.time()
	init = 1
	jobs = []
	queue = []
	for i in range(0,len(numbers)):
		p = Process(target=compute_pi, args=(numbers[i],i))
		jobs.append(p)
	print(jobs)
	while True:
		if init != 1 and len(queue) == 0:
			break
		init = 0
		if len(queue) < usable_cores:
			for i in range(0, usable_cores - len(queue)):
				if len(jobs) > 0:
					p = jobs.pop(0)
					print(f"Process: {p}")
					p.start()
					queue.append(p)
		for process in queue:
			if not process.is_alive():
				print(f"Killing Process: {process}, queue_len: {len(queue)}")
				queue.remove(process)
			
					
def mp_pool():
	time_exec = time.time()
	numbers = [10000000]*20
	# usable_cores = max(cpu_count()-1, 1)
	usable_cores = 5
	print(f'Using {usable_cores} cores')
	with Pool(processes=usable_cores) as p:
		results = p.map(compute_pi, numbers)
	time_exec = time.time() - time_exec
	print(f"Finished processing data in {round(time_exec, 3)} sec")
	# results = [compute_pi(number) for number in numbers]


if __name__ == '__main__':
	# mp_pool()
	# jobs = mp1()
	# print(jobs)
	# print(sys.getsizeof(jobs))
	mp2()
	
	
