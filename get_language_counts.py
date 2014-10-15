#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 HumanGeo
# Authored by: Abe Usher (abe@thehumangeo.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time

#GLOBAL VARIABLES
counter = {}
infile = 'germany.txt'
outfile = 'language_counts.txt'

def compute_language_counts(input_file,output_file):
    """
    This function walks the lines of an input file and counts the number of geohashes
    that are related to the language specified by the variable 'lang_filter'.
    """
    line_counter = 0
    for line in open(input_file):
        try:
            line_counter +=1
            if line_counter % 10000 == 0:
                print line_counter
            line = line.strip()
            parts = line.split('\t')
            if len(parts) != 23:
                continue
                print len(parts)
            #print len(parts)
            #time.sleep(.1)
            language = parts[5]
            counter[language] = counter.get(language,0) +1
        except Exception, e:
            pass
    print line_counter
    #now that we have computed the counts of items according to each language, for each geohash box,
    #write the results to an external text file
    fout = open(output_file,"w")
    for key, value in counter.items():
        text = '%s\t%s\n'%(key,value)
        fout.write(text)
    print 'Done writing output from (%s) lines to (%s).' %(line_counter, output_file)

def main():
    """
    Standard main() method.  This is the entry point that tells the python interpreter how to run your program.
    """
    compute_language_counts(infile,outfile)

if __name__ == '__main__':
    main()