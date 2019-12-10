import sys
import os
import json
import gseapy
import uuid
import math
import pandas as pd
from collections import Counter

class rankutils:
  def __init__(self):
      pass

  def gen_rank(self, diffexpressionfile):
      outdirectory='/kb/module/work/tmp/'

      df = pd.read_csv(diffexpressionfile, delimiter='\t')
      pvalue_col = df.iloc[ : , 2]
      pvalue_col = pvalue_col[pvalue_col != 0]
      min_pvalue = pvalue_col.min()/10

      f = open(diffexpressionfile, "r")
      sorteddict = {}
      for line in f:
          if(not (line.startswith("gene_id"))):
             line=line.rstrip()
             seq=line.split("\t")
             geneid=seq[0]
             log_two_fold_change=seq[1]
             pvalue=float(seq[2])
             if(pvalue == 0):
                pvalue = min_pvalue
             if(float(log_two_fold_change) > 0):
                sorteddict[geneid]=1/pvalue
             else:
                sorteddict[geneid]=-1/pvalue
      f.close()

      fw = open(outdirectory+"/rank.txt", "w")
      fw.write("Id\tt\n")
      sorted_list=Counter(sorteddict).most_common()[::-1]
      for k in sorted_list:
          fw.write(k[0]+"\t"+str(k[1])+"\n")
      fw.close()
      
      
  
