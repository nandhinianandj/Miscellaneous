#!/usr/bin/python
# adr_conv.py
#
# Converts a vCard address book into abook addressbook format
#
# Original Author:   Gavin Costello
# Date:     19.02.2009
# Modified by: Anand Jeyahar
# Date: 15.08.2011

import sys
import os
name = '';
phone = '';
email = '';
count = 1;
out_file = open('/home/anand/.abook/addressbook','a')
for vcffile in os.listdir(sys.argv[1]):
    cfile = open(os.path.join(sys.argv[1],vcffile), 'r')
    for line in cfile.readlines():
        if (line.startswith('FN')):
            count += 1
            print out_file
            name = line.split(':')[1]
            out_file.write('[%d]'%count)
            out_file.write('name=%s' %(name))
        if (line.startswith('EMAIL')):
            email = line.split(':')[1]
            out_file.write('email=%s' % email)
        if (line.startswith('TEL')):
            tel = line.split(';')[1]
            fulltype = tel.split('=')[1]
            type = fulltype.split(':')[0]
            phone = line.split(':')[1]
            if (type.endswith('CELL')):
                out_file.write('mobile=%s'%phone)
            elif (type.endswith('HOME')):
                out_file.write('phone=%s' %phone)
            elif (type.endswith('WORK')):
                out_file.write('work=%s'%phone)
out_file.close()
