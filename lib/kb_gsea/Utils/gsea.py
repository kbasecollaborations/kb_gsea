import sys
import os
import json
import gseapy
import uuid

class gsea:
  def __init__(self):
      pass

  def create_index_html(self,outdirectory):
      htmlstring = "<html><body>";
      directory_list = os.listdir(outdirectory)

      for file_name in directory_list:
          htmlstring += "<a href=" + file_name + ">"+file_name+"</a></br>"
      htmlstring += "</body></html>";
      return (htmlstring)

  def run_gsea(self):
      #outdirectory='/kb/module/work/tmp/' + str(uuid.uuid1())
      outdirectory='/kb/module/work/tmp/'
      os.system("Rscript /kb/module/work/fgsea_test/run_Ath_Kbase.R "+ outdirectory)
      htmlstring = self.create_index_html(outdirectory)
      index_file_path = outdirectory + "/index.html"
      html_file = open(index_file_path, "wt")
      n = html_file.write(htmlstring)
      html_file.close()

      return (outdirectory)

  '''
  def run_gsea(self):
      expfile='/kb/module/test/data/Ath.exp_matrix'
      genesets='/kb/module/test/data/Ath_all.gmt'
      clsfile = '/kb/module/test/data/Ath.cls'
      rmethod = 'signal_to_noise'
      rankfile = 'fgsea_test/rnk.txt'
      outdirectory='/kb/module/work/tmp/gseapy_out' + str(uuid.uuid1())
      #result=gseapy.gsea(data=expfile, gene_sets=genesets, cls=clsfile, method=rmethod, outdir=outdirectory)
      result=gseapy.prerank(rnk=rankfile, gene_sets=genesets, method=rmethod, outdir=outdirectory)
      htmlstring = self.create_index_html(outdirectory)

      index_file_path = outdirectory + "/index.html"
      html_file = open(index_file_path, "wt")
      n = html_file.write(htmlstring)
      html_file.close()

      return (outdirectory)
  '''    
      
  
