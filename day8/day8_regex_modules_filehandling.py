import re
text='Contact us at test@gmail.com or admin@yahoo.com'
pattern=r"[\w.-]+@[\w.-]+\.\w+"
 emails=re.findall(pattern,text)
 print(emails)

#Q  "order123 price45 quantity"
 text = "order123 price45 quantity"
 result=re.findall(r"\d+",text)
 print(result)

#Q validate a strong password
    # -At least 8 char
    # -one uppercase
    # -one lowercase
    # -one digit
    # -one special char

pattern="^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%*?&]).{8,}"
