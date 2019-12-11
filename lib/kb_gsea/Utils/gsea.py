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
      outdirectory='/kb/module/work/tmp/' + str(uuid.uuid1())
      #TODO: Make sure you test for success of creatinga  directory
      os.mkdir(outdirectory)

      #outdirectory='/kb/module/work/tmp/'
      command = "Rscript /kb/module/lib/kb_gsea/Utils/run_Ath_Kbase.R "+ outdirectory

      #TODO: Try to fihure out how to put logs 
      print (command)
      os.system(command)
      htmlstring = self.create_index_html(outdirectory)
      index_file_path = outdirectory + "/index.html"
      html_file = open(index_file_path, "wt")
      n = html_file.write(htmlstring)
      html_file.close()

      return (outdirectory)

      
  
