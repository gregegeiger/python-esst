#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# 2020-08-17:geg
#


secret = 'swordfish'
pw = ''

max_tries = 5
try_count = 0
auth = False

#
# while repeats while expression is true
#
while pw != secret:
    try_count += 1
    #
    # continue short cuts the loop and it stars back at the top
    #
    if try_count == 3: continue
    pw = input(f"{try_count}: What's the secret word? ")
    if (try_count >= max_tries): break
#
# else: executes only if the loop terminated normally - not a break
#
else:auth=True
#
# Test auth
#
print ("Authorized" if auth else "Not Authorized...Calling the FBI")

    