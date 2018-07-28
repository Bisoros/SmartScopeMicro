import re

reg = re.compile

valid_regex = (
    reg('^load("*")$') ,
    reg('^wait(\d+)$') ,
    reg('^if"*"detected$') ,
    reg('^loop:$') ,
    reg('^scan:$') ,
    reg('^scan$') ,
    reg('^tweet$') ,
    reg('^end$') ,
)

def remove_white_spaces(string):
    return ''.join(string.split())


with open('tf_files/macro.txt') as f:
    lines = f.readlines()

printf = print

inloop = False
inscan = False

def check_valid(string):
    valid = False
    global inloop, inscan
    if string == 'loop:':
        inloop = True

    if string == 'scan:':
        inscan = True
    for regex in valid_regex:
        if regex.match(string):
            valid = True
            #print ('1')

    if not(inloop or inscan) and string not in ('loop:', 'scan:'):
        valid = False
        #print ('2')

    return valid

for line in lines:
    line = remove_white_spaces(line)
    if line  and line[0] != '#':
        if check_valid(line):
            print (line)
        else:
            print ('gay: ' + line)
        #if line == 'loop:':
        #    printf('def loop:')
