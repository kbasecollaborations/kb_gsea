/*
A KBase module: kb_gsea
*/

module kb_gsea {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    typedef structure{
        string obj_name;
        int permutation_number;
      } gseaparams;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_kb_gsea(gseaparams params) returns (ReportResults output) authentication required;

};
