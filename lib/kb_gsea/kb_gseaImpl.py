# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import csv
from kb_gsea.Utils.gsea import gsea
from kb_gsea.Utils.rankutils import rankutils
from kb_gsea.Utils.htmlreportutils import htmlreportutils
from kb_gsea.Utils.expressionmatrixutil import expressionmatrixutil
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class kb_gsea:
    '''
    Module Name:
    kb_gsea

    Module Description:
    A KBase module: kb_gsea
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        self.gs = gsea()
        self.hr = htmlreportutils()
        self.eu = expressionmatrixutil()
        self.dfu = DataFileUtil(self.callback_url)
        self.ru = rankutils()
        #END_CONSTRUCTOR
        pass


    def run_kb_gsea(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_kb_gsea
        self.eu.download_expression_matrix(params['differential_expression_matrix'])
        #self.eu.download_expression_matrix(params['DifferentialExpressionMatrixRef'])
        diff_expr_matrix_file_name = 'gene_results.csv'
        result_directory = "/kb/module/work/tmp/"
        diff_expr_matrix_file = os.path.join(result_directory, diff_expr_matrix_file_name)
 
        self.ru.gen_rank(diff_expr_matrix_file)
        outputdir = self.gs.run_gsea()
        workspace = params['workspace_name']
        output = self.hr.create_html_report(self.callback_url, outputdir, workspace)
        report = KBaseReport(self.callback_url)
        #END run_kb_gsea

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_kb_gsea return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
