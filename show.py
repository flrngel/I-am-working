#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib
import math
import time
import random

TIMER = 1

def fx():
    global TIMER
    sha = hashlib.new('sha256'); sha.update(str(random.random())); sha = sha.hexdigest()
    sha2 = hashlib.new('sha256'); sha2.update(str(random.random())); sha2 = sha2.hexdigest()

    print ("gcc -O2 -Wall -Wno-static build-centos-x86/q3cpp build-centos-x86/cpp/"+sha[0: int(math.ceil(random.random()*30))]+".o build-centos-x86/cpp/lex.o build-centos-x86/cpp/"+sha2[0: int(math.ceil(random.random()*50))]+".o build-centos-x86/cpp/"+sha[0: int(math.ceil(random.random()*10))]+".o build-centos-x86/cpp/"+sha+".o build-centos-x86/cpp/eval.o build-centos-x86/cpp/include.o build-centos-x86/cpp/hideset.o build-centos-x86/cpp/getopt.o build-centos-x86/cpp/"+sha2[0: int(math.ceil(random.random()*44))]);

    if (math.ceil(random.random()*1000) % 777 < 321): print("")
    if (math.ceil(random.random()*1000) % 778 == 777):
        print("Configuring.........")
        print("Setting...")
        print("Compiling.........")
        print("Checking.........")
        TIMER = 15
    else:
        TIMER = int(math.ceil(random.random()*2000)) / 1000

if __name__ == '__main__':
    while True:
        fx()
        time.sleep(TIMER)
