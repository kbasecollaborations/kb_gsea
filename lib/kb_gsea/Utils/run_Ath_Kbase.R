#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
library(fgsea)
library(data.table)

outdir=args[1]
outfile=paste0(outdir,"/fgseaRes_kbase_ath.txt")
rnk.file<-"/kb/module/work/tmp/rank.txt"
gmt.file <- "/kb/module/data/Ath.gmt"

ranks <- read.table(rnk.file,
                    header=TRUE, colClasses = c("character", "numeric"))
ranks <- setNames(ranks$t, ranks$ID)
str(ranks)

pathways <- gmtPathways(gmt.file)

str(head(pathways))


fgseaRes <- fgsea(pathways, ranks, minSize=15, maxSize=500, nperm=1000)
dataout<-as.data.frame(fgseaRes)

df <-dataout[order(dataout$NES),]
print(colnames(df))
fwrite(df, file=outfile, sep="\t", sep2=c("", " ", ""))
print(df$pathway[1])

#fwrite(fgseaRes, file=outfile, sep="\t", sep2=c("", " ", ""))

for (i in 1:10)
{
    print(df$pathway[i])
    name <- gsub("//", "", df$pathway[i], fixed=TRUE) 
    png(paste0(outdir,"/",name,".png"))
    plotx = plotEnrichment(pathways[[df$pathway[i]]], ranks, gseaParam = 1, ticksSize = 0.2)
    print(plotx)
    dev.off()
}


print("printing bottom 10\n")
num<-nrow(df)

for (j in (num-10):num)
{
    print(df$pathway[j])
    name <- gsub("//", "", df$pathway[j], fixed=TRUE)
    png(paste0(outdir,"/",name,".png"))
    plotx = plotEnrichment(pathways[[df$pathway[j]]], ranks, gseaParam = 1, ticksSize = 0.2)
    print(plotx)
    dev.off()
}


