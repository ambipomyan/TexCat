import re
import os
import sys
import argparse

## inputs
def rep_input(match):
    val = match.group()
    l = len(val)
    out = '\n' + val[7 :(l - 1)] + '.tex'
    return out
    
def replace_input2(Str):
    Str = re.sub(r'\\input\{[a-zA-Z0-9/_]*\}', rep_input, Str)
    return Str
    
def insert_dot_tex_file(Str, file):
    if '.tex' in Str:
        #Str = 'please insert LaTex file here!\n'
        # clean spaces and \n
        Str = re.sub(r'\n', '', Str)
        Str = re.sub(r' ', '', Str)
        f1 = open(Str)
        line = f1.readline()
        while line:
            file.write(line)
            line = f1.readline()
    return 0
    
def gen_full_text(input):
# prepare input/tmp/output
    output = input[0:-4] + '.txt'
    tmp    = input[0:-4] + '_tmp.txt'
# read input by line, save to tmp: .txt files
    f1 = open(input)
    f2 = open(tmp, 'w')
    line = f1.readline()
    while line:
        f2.write(line)
        line = f1.readline()
        line = replace_input2(line)
    f1.close()
    f2.close()
# read tmp by line, save back to output: .tex files
    f1 = open(tmp)
    f2 = open(output, 'w')
    line = f1.readline()
    while line:
        f2.write(line)
        line = f1.readline()
        status = insert_dot_tex_file(line, f2)
    f1.close()
    f2.close()
    
    return output

######################
# generate full text #
######################
input  = 'main.tex'
output = gen_full_text(input)

#########
# tests #
#########
print(output)
