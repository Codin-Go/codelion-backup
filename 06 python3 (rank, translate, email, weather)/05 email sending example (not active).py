#chkd v "subject" o 'subject

message = EmailMessage()
message.set_content("본문입니다.")

# MIME의 Header에 제목,발신자,수신자를 추가해봅시다. 빈칸을 채워주세요.
message['Subject'] = "제목입니다."
message['From'] = "발신자@gmail.com"
message['To'] = "수신자@gmail.com"

# 이미지 파일을 읽는 구문을 작성해요. 빈칸을 채워주세요.
with open("codelion.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)
message.add_attachment(image_file,maintype='image',subtype=image_type)

# SSL 설정을 포함해서 SMTP 서버에 연결하는 구문을 작성해요. 빈칸을 채워주세요.
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("발신자@gmail.com","password")
sendEmail("수신자@gmail.com")
smtp.quit()