library(fgsea)
library(data.table)


rnk.file <- "rnk.txt"
gmt.file <- "Ath.gmt"

ranks <- read.table(rnk.file,
                    header=TRUE, colClasses = c("character", "numeric"))
ranks <- setNames(ranks$t, ranks$ID)
str(ranks)

pathways <- gmtPathways(gmt.file)
str(head(pathways))


fgseaRes <- fgsea(pathways, ranks, minSize=15, maxSize=500, nperm=1000)
head(fgseaRes)


fwrite(fgseaRes, file="fgseaRes4.txt", sep="\t", sep2=c("", " ", ""))


