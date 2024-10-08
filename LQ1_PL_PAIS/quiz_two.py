#variable that stores names of groupmates
memberName1 = "Abegail A. Daproza"
memberName2 = "Jonadel N. Cabang"
memberName3 = "Francene Gian B. Pais"

#variable that stores age of groupmates
memberAge1 = "23"
memberAge2 = "22"
memberAge3 = "20"

age1 = int(memberAge1)
age2 = int(memberAge2)
age3 = int(memberAge3)

#variable that stores allowance of groupmates in decimal form
memberAllowance1 = float(1,000.0)
memberAllowance2 = float(2,000.0)
memberAllowance3 = float(500.0)

print("Member 1:" + memberName1 + "," + "his age is" + memberAge1 + "," + "allowance per week is" + memberAllowance1)
print("Member 2:" + memberName2 + "," + "his age is" + memberAge2 + "," + "allowance per week is" + memberAllowance2)
print("Member 3:" + memberName3 + "," + "his age is" + memberAge3 + "," + "allowance per week is" + memberAllowance3)

#variable that stores the length of the names of each member
member_1NameLength = len(memberName1)
member_2NameLength = len(memberName2)
member_3NameLength = len(memberName3)

print ("Member 1 consists of" + member_1NameLength + "characters")
print ("Member 2 consists of" + member_2NameLength + "characters")
print ("Member 3 consists of" + member_3NameLength + "characters")

#add all the ages of the members of the group
sumMember = (memberAge1 + memberAge2 + memberAge3)
print (sumMember)

#subtract all the ages of the members of the group
subMember = (memberAge1 - meberAge2 - meberAge3)
print (subMember)

#multiply the age and the allowances of every group
product1 = (memberAge1 * memberAllowance1)
product2 = (memberAge2 * memberAllowance2)
product3 = (memberAge3 * memberAllowance3)

print (product1)
print (product2)
print (product3)

#comparison of ages for every member
com1 = (memberAge1 - memberAge2)
com2 = (memberAge2 - memberAge3)

print (com1)
print (com2)

# comparison of name lengths for every member
LengthName1 = (member_1NameLength - member_2NameLength)
LengthName2 = (member_2NameLength - member_3NameLength)
print(LengthName1)
print(LengthName2)