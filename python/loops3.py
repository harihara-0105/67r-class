ip=12345
count=0
while(ip>0):
      count +=1
      ip //=10

print(count)      



#sum of only even num in given up
#count only odd num in given ip
num=12589
even_sum=0
odd_count=0
while num>0:
      rem=num%10
      if rem%2==0:
            even_sum+=rem
      else:
            odd_count+=1
      num//=10
print(even_sum)
print(odd_count)

