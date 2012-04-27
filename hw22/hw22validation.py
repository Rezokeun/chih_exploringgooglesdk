#!/usr/bin/env python

def validate_username(user_n):
    if user_n:
	find_str = ' '
	if user_n.find(find_str) == -1:
	    return user_n
	else:
	    return 'False'
