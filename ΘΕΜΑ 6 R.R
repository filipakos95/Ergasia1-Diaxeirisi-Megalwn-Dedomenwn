#thema 6


euclidean <- function(x, y) sqrt(sum((x - y)^2))

#orizw ta dianysmata ths askhshs

x1<-c("Green", "Potato", "Ford")
y1<-c("Tyrian purple", "Pasta", "Opel")

x2<- c("Eagle", "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay") 
y2<- c("Eagle", "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay")


x3<- c("Werner Herzog", "Aquirre, the wrath of God", "Audi", "Spanish red") 
y3<- c("Martin Scorsese", "Taxi driver", "Toyota", "Spanish red")



#################################################################################################

#orizw ta dianysmata me o kai 1

p<- c(1,0,1,0,1,0)
r<- c(0,1,0,1,0,1)

t <- c(1,1,1,1,1)
u <- c(1,1,1,1,1)

x<-c(1,0,1,0,1,0,1)
y<-c(0,1,0,1,0,1,1)

##################################################################################################

#ftiaxnw ton diadiko pinaka gia to prwto zeygos dianysmatwn

row<- c("p","r")
coln <- c("green", "Tyr Pu", "potato", "pasta", "ford", "opel")
m <- matrix(c(p,r), nrow = 2, byrow = TRUE, dimnames = list(row,coln))
print(m)

##################################################################################################

#ftiaxnw ton diadiko pinaka gia to deytero zeygos dianysmatwn

row1<- c("t","u")
coln1<- c("eagle", "ronaldo", "real madrid", "prussian blue", "michael bay")
n <- matrix(c(t,u), nrow = 2, byrow = TRUE, dimnames = list(row1,coln1) )
print(n)

###################################################################################################

#ftiaxnw ton diadiko pinaka gia to trito zeygos dianysmatwn

row2<- c("x","y")
coln2<- c("werner", "martin", "aquirre", "taxi driver", "audi", "tayota", "spanish red")
z <- matrix(c(x,y), nrow = 2, byrow = TRUE, dimnames = list(row2,coln2))
print(z)

###################################################################################################

#briskwtis apostaseis twn dianysmatvn me thn synarthsh ths eykleidias apostashs
euclidean(p,r)
euclidean(t,u)
euclidean(x,y)
