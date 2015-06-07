#!/usr/bin/env python
#coding:utf-8

import sys

if len(sys.argv) != 2:
	print 'Usage: %s FILE' % sys.argv[0]
	exit(1)

with open(sys.argv[1], 'r') as infile:
	A = tuple([int(e) for e in infile.readlines()])

acc = 0

def sort_and_count(A):
	n = len(A)
	if n <= 1:
		return A
	left = sort_and_count(A[:n//2])
	right = sort_and_count(A[n//2:])
	return merge_and_count_split_inv(left, right, n)

def merge_and_count_split_inv(left, right, n):
	l = len(left)
	r = len(right)
	i = 0
	j = 0
	global acc
	res = []
	for k in xrange(n):
		if j == r or i != l and left[i] < right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
			acc += l-i
	return res

B = sort_and_count(A)
#assert B == range(1,len(A)+1)
print 'Answer:', acc
