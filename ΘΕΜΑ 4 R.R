#thema 4

# erwthma 1

#orismos euclideandistance

euclidean <- function(x, y) sqrt(sum((x - y)^2))
#################################################
#orismos dianysmatwn

x1 <- c(1,2,3,4,5,6) 
y1<-  c(1,2,3,4,5,6)

x2 <- c(-0.5, 1, 7.3, 7, 9.4, -8.2, 9, -6, -6.3) 
y2 <- c(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)

x3 <- c(-0.5, 1, 7.3, 7, 9.4, -8.2) 
y3 <- c(1.25, 9.02, -7.3, -7, 5, 1.3)

x4 <- c(0, 0, 0.2) 
y4 <- c(0.2, 0.2, 0)
##################################################################

#ypologismos apostasewn dianysmatwn me thn xrhsh ths synarthshs
euclidean (x1, y1)
euclidean (x2, y2)
euclidean (x3, y3)
euclidean (x4, y4)
###################################################################

#erwthma 2

#orizw ta dianysmata

p<- c(1,25000,14,7)
r<- c(2,42000,17,9)
s<- c(3,55000,22,5) 
t<-c(4,27000,13,11)
u<- c(5,58000,21,13) 

rown <- c("p","r","s","t","u")
coln <- c("ΑΑ","ΔΙΑΡΚΕΙΑ","ΠΛΗΘΟΣ","SMS","MB")
#ftiaxnw ton pinaka dianysmatwm
k <- matrix(c(p,r,s,t,u), nrow = 5, byrow = TRUE, dimnames = list(rown, coln))
print(k)

#ypologizw tis apostaseis
euclidean(p,u)
euclidean(r,u)
euclidean(s,u)
euclidean(t,u)

#ekxwrw tis apostaseis se mia meytavlhth
apostasi1<-euclidean(p,u)
apostasi2<-euclidean(r,u)
apostasi3<-euclidean(s,u)
apostasi4<-euclidean(t,u)
print(apostasi1)
print(apostasi2)
print(apostasi3)
print(apostasi4)

#briskw thn mikroterh apostash h opoia tha tairiazei sto profile toy xrhsth 5
min(apostasi1,apostasi2,apostasi3,apostasi4)

#to profile toy xrhsth 3 moiazei perissotero sto profile tou xrhsth 5 giati exoyn metajy toys thn mikroterh postash

