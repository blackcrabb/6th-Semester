fmax<-function(a)
{
  maxim=a[1]
  for(i in a)
  {
    if(i>maxim)
      maxim=i
  }
  return(maxim)
}
n=as.integer(readline("enter the length of list "))
a<-list()
for(i in 1:n)
{
  el=as.integer(readline("enter the element "))
  a[i]=el
}
res<-fmax(a)
res

