card_num=input("Enter credit card number:")
card_num = [int(digit) for digit in card_num]
checking_num=card_num.pop()
card_num.reverse()
print(card_num)
print(checking_num)
double_num=[]
for i,value in enumerate(card_num):
    if i%2==0 :
        double=card_num[i]*2
        if double > 9:
            double -= 9
        card_num[i]=double
print(card_num)
card_num.append(checking_num)
total_sum=sum(card_num)  
print("total_sum:",total_sum)  
if total_sum%10==0:
    print("Credit card is valid")
else:
    print("Credit card is invalid")

