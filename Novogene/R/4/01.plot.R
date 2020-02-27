data=read.table("D:/ÅµºÌÖÂÔ´/±à³Ì¿¼ºË/01.plot.txt",header=T)
pdf("D:/ÅµºÌÖÂÔ´/±à³Ì¿¼ºË/01.plot.pdf")
boxplot(data,ylim=c(-10,20),xlab="The name of xlab",ylab="The name of y lab",main="The example",col=c("red","green","cyan","purple"))
for(i in 1:dim(data)[2]) {text(i,15,paste("N=",dim(data)[1]-summary(data[,i])[7],sep=" "))}
dev.off()

