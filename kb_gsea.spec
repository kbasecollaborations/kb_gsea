/*
A KBase module: kb_gsea
*/

module kb_gsea {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    typedef structure{
        string filename;
      } inparams;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_kb_gsea(inparams params) returns (ReportResults output) authentication required;

};
