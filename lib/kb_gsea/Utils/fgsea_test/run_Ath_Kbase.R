#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
library(fgsea)
library(data.table)

outdir=args[1]
outfile=paste0(outdir,"/fgseaRes_kbase_ath.txt")
#rnk.file <- "/kb/module/work/fgsea_test/ranked_list_kbaseAth.txt"
rnk.file<-"/kb/module/work/tmp/rank.txt"
gmt.file <- "/kb/module/work/fgsea_test/Ath.gmt"

ranks <- read.table(rnk.file,
                    header=TRUE, colClasses = c("character", "numeric"))
ranks <- setNames(ranks$t, ranks$ID)
str(ranks)

pathways <- gmtPathways(gmt.file)
str(head(pathways))


fgseaRes <- fgsea(pathways, ranks, minSize=15, maxSize=500, nperm=1000)
head(fgseaRes)

fwrite(fgseaRes, file=outfile, sep="\t", sep2=c("", " ", ""))
#fwrite(fgseaRes, file="/kb/module/work/fgsea_test/fgseaRes_kbase_ath.txt", sep="\t", sep2=c("", " ", ""))


