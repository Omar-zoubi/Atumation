import re
with open('potential-contacts.txt') as file :
    new_text = file.readlines()
    new_text=''.join(new_text)
    # print(new_text)
    phone_reg = r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    email_reg = r"[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]"
    all_phone= re.findall(phone_reg, new_text)
    all_emails= re.findall(email_reg,new_text)
    unique_phone = []
    unique_email = []
    for x in all_phone:
        if x not in unique_phone:
            unique_phone.append(x)

    for x in all_emails:
         if x not in unique_email:
            unique_email.append(x)
    # unique_phone = unique_phone.sort()
    a = [',','-','.','(',')']
    for j in range(len(unique_phone)):
        for i in a :
            unique_phone[j]=unique_phone[j].replace(i,'')
            
    def phone_format(phone_number):
        clean_phone_number = re.sub('[^0-9]+', '', phone_number)
        formatted_phone_number = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
        return formatted_phone_number
    for j in range(len(unique_phone)): 
        if len(unique_phone[j]) <= 7 :
            unique_phone[j] = '206'+ unique_phone[j]
        elif len(unique_phone[j]) == 8:
            unique_phone[j] = '00'+ unique_phone[j]

        elif len(unique_phone[j]) == 9:
            unique_phone[j] = '0'+ unique_phone[j]
        
    for j in range(len( unique_phone)): 
        unique_phone[j]= re.sub('^000', '206', unique_phone[j])
        
    for j in range(len( unique_phone)): 
        unique_phone[j] = re.sub(r'(\d{3})(\d{3})(\d{4})', r'\1- \2-\3', str(unique_phone[j]))
        # print(j)
         
    unique_phone.sort()
    unique_email.sort()
    print(unique_phone)
    file= open("phone_numbers.txt", "w")
    file.write(str(unique_phone))
    file.close()

    file= open("emails.txt", "w")
    file.write(str(unique_email))
    file.close()