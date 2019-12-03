import sys
import os
import json
import gseapy

class gsea:
  def __init__(self):
      pass

  def build_gsea_command(self):
      if not os.path.exists('/kb/module/work/tmp/gsea_out'):
          os.mkdir('/kb/module/work/tmp/gsea_out')
    
      command="gseapy.gsea(data='/kb/module/work/gseapy_test/Ath.exp_matrix', gene_sets='/kb/module/work/gseapy_test/Ath.gmt', cls='/kb/module/work/gseapy_test/Ath.cls', method='signal_to_noise', outdir='/kb/module/work/tmp/gseapy_out')"
      return command

  def run_gsea_command(self, command):
      os.system(command)
  
