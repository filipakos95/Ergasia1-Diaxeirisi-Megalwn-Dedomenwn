#THEMA 5
library(lsa)
#orizw thn synarthsh poy tha xrhsinopoihsw
#cosine(x,y)


#orizw ta danysmata
x1<- c(9.32, -8.3, 0.2) 
y1<- c(-5.3, 8.2, 7)


x2<-c(6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3) 
y2<-c(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
 
 
x3<-c(-0.5, 1, 7.3, 7, 9.4, -8.2) 
y3<-c(1.25, 9.02, -7.3, -7, 15, 12.3)

x4<-c(2, 8, 5.2) 
y4<-c(2, 8, 5.2)

#ekxwrw thn apostash synhmitonoy se mia metavlhth
a <- cosine(x1,y1)
b <- cosine(x2,y2)
c <- cosine(x3,y3)
d <- cosine(x4,y4)

#emfanizw ths apostaseis synhmitonoy
print(a)
print(b)
print(c)
print(d)
