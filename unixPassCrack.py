'''
Title: Unix Password Cracking using Dictionary based Attack and Shadow file
Author: Qaidjohar Jawadwala
For Educational Purpose Only

Status: In Progress
Usage: python unixPassCrack.py
'''

import crypt

#Code for calculating SHA512 Hash Shadow
h_id = 6
salt = '/zpAihl2'
#input_salt = $6$/zpAihl2
input_salt = '${}${}'.format(h_id,salt)
password = 'abc1234'

calcHashValue = crypt.crypt(password,input_salt)
print(calcHashValue)

#Code for calculating default md5 Hash Shadow
password = 'toor'
input_salt='X0'
calcHashValue = crypt.crypt(password,input_salt)
print(calcHashValue)



