#!/usr/bin/env python

import os
import sys
import argparse
import subprocess

#
if __name__ == '__main__':
    '''
    fathmm-MKL.py: Predict the Functional Consequences of Single Nucleotide Variants (SNVs)
    '''
    
    # fetch argument(s)
    parser = argparse.ArgumentParser(
                                      description = 'Predict the Functional Consequences of Single Nucleotide Variants (SNVs)',
                                      add_help = False
                                    )
    parser.add_argument(
                         "-h",
                         "--help",
                         action = "help",
                         help = argparse.SUPPRESS
                       )
    
    group = \
        parser.add_argument_group("Required")
    group.add_argument(
                        'fi',
                        metavar = '<F1>',
                        type = argparse.FileType("r"),
                        help = 'the mutation data to process'
                      )
    group.add_argument(
                        'fo',
                        metavar = '<F2>',
                        type = argparse.FileType("w"),
                        help = 'where predictions are written'
                      )
    
    group.add_argument(
                        'db',
                        metavar = '<db>',
                        type = argparse.FileType("r"),
                        help = 'precomputed database of fathmm-MKL predictions'
                      )
    
    Args = parser.parse_args()
    
    #
    
    Args.fo.write("\t".join([ 
                             "# Chromosome",
                             "Position",
                             "Ref. Base",
                             "Mutant Base",
                             "Non-Coding Score",
                             "Non-Coding Groups",
                             "Coding Score",
                             "Coding Groups",
                             "Warning"
                           ]) + "\n")

    for query in Args.fi:
        if not query.strip() or query.startswith("#"):
            continue
        query = query.strip().upper().split(",")
        Pred  = [ '', '', '', '', "No Prediction Found" ]
        
        
        # approve query ...
        try:
            assert query.__len__() == 4     # required data present in query
            
            int(query[1])                   # is position numeric
            assert query[2] in \
                [ "A", "C", "G", "T" ]      # expected base
            assert query[3] in \
                [ "A", "C", "G", "T" ]      # expected base
        except:
            Args.fo.write("\t".join([ '', '', '', '', '', '', '', '', "Error: Unexpected Format '" + ",".join(query) + "'" ] ) + "\n"); continue
        
        
        # fetch prediction ...
        proc      = subprocess.Popen([ "tabix " + Args.db.name + " " + query[0] + ":" + str(int(query[1]) + 1) + "-" + str(int(query[1]) + 1) ], stdout=subprocess.PIPE, shell=True)
        data, err = proc.communicate()
        if err:
            Pred[-1] = "Error: 'tabix' command"; continue
        if data:
            for record in data.split("\n"):
                if not record:
                    continue
                record = record.strip().split("\t")
                
                if not record[0] == query[0]:
                    Pred[-1] = "Error: Unexpected Chromosome"; break
                if not record[1] == query[1]:
                    Pred[-1] = "Error: Unexpected Position";   break
                if not record[3] == query[2]:
                    Pred[-1] = "Warning: Inconsistent Base (Expecting '" + record[3] + "')";   break
                if record[4] == query[3]:
                    Pred = record[5:] + [ '' ]
                    break
        
        Args.fo.write("\t".join( query + Pred ) + "\n")
