#!/usr/bin/env python
#coding:utf-8

import sys

if len(sys.argv) != 2:
	print 'Usage: %s FILE' % sys.argv[0]
	exit(1)

with open(sys.argv[1], 'r') as infile:
	A = [int(e) for e in infile.readlines()]

acc = 0

def choose_pivot1(A, l, r):
	return l

def choose_pivot2(A, l, r):
	return r-1

def choose_pivot3(A, l, r):
	m = l + (r-l+1)//2 - 1
	r -= 1
	tmp = {A[l]:l, A[m]:m, A[r]:r}
	return tmp[sorted(tmp.keys())[1]]

def quick_sort(A, l, r):
	if r - l <= 1:
		return
	#p = choose_pivot1(A, l, r)
	#p = choose_pivot2(A, l, r)
	p = choose_pivot3(A, l, r)
	i = partition(A, l, r, p)
	quick_sort(A, l, i)
	quick_sort(A, i+1, r)

def swap(A,i,j):
	if i != j:
        	tmp = A[j]
        	A[j] = A[i]
        	A[i] = tmp

def partition(A, l, r, p):
	global acc
	acc += r-l-1
	swap(A, l, p)
	i = l+1
	for j in xrange(i, r):
		if A[j] < A[l]:
			swap(A, i, j)
			i += 1
	swap(A, l, i-1)
	return i-1

quick_sort(A, 0, len(A))
#assert A == range(1, len(A)+1)
print 'Answer:', acc
