data=read.table("D:/ÅµºÌÖÂÔ´/±à³Ì¿¼ºË/02.plot.txt",header=T)
color=rep("red",dim(data)[1])
color[data[,1]==0]="green"
color[data[,2]==0]="blue"
pdf("D:/ÅµºÌÖÂÔ´/±à³Ì¿¼ºË/02.plot.pdf")
plot(data,xlab="The frequency of sample1",ylab="The frequency of sample2",main="The example",col=color,pch=16)
dev.off()
