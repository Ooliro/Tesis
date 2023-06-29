library(stringr)

ids <- system("grep '>' scfs_10gap.fa | sed 's/>//'", intern = T)
ids2 <- system("grep '>' subdb.fasta | sed 's/>//'", intern = T)
bed <- read.table("tag.BED", stringsAsFactors = F, header = F)
clados <- read.table("scfs_cc.csv", stringsAsFactors = F, header = F, sep = "\t")

subbed <- bed[bed$V2 %in% ids,]

accid <- str_remove(ids2, " .+")
descr <- str_remove(ids2, "^.+\\..") |> str_remove(" \\[.+")
sp <- str_remove(ids2,'.*\\[') |> str_remove("\\]") |> str_trim()

querys <- data.frame(accid,descr,sp)

querys$clado <- "-"

for(i in 1:length(sp)){
  cld <- grep(sp[i], clados$V2)
  if (length(cld) > 0){
    querys$clado[i] <- clados$V1[cld]
  }
}

write.csv(querys,"resumen_de_clados.csv", quote = F, row.names = F, col.names = F)
