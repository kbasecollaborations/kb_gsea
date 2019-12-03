import gseapy

# run GSEA.
gseapy.gsea(data='Ath.exp_matrix', gene_sets='Ath.gmt', cls='Ath.cls', method='signal_to_noise', outdir='test3' , weighted_score_type=2)
