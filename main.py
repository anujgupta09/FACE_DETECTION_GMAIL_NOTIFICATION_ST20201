import cv2
import time
import os
import passwords

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
os.system("cls")
cap = cv2.VideoCapture(0)

while True:
    os.system("color 7")
    retuurn, pic_data = cap.read()
    cv2.imwrite("anuujj.jpg", pic_data)
    model = cv2.CascadeClassifier('harcascade_frontalface_default.xml')
    faces = model.detectMultiScale(pic_data)

    if len(faces) == 0:
        os.system("color 2")
        print(">>>>>>>>>>>> ALL GOOD <<<<<<<<<<<<<<\n")
        pass
        time.sleep(2)
        os.system("color 7")

    else:
        toaddr = "1anujgupta123@gmail.com"
        os.system("color 4")
        print("\n\n>>>>>>>>> ALERT...  (  ( ( INTRUDER ) )  )  DETECTED...",">>>>>>>>> Notifying via mail on - ", toaddr, "<<<<<<<<<<<\n")
        time.sleep(2)
        os.system("color 7")
        x = faces[0][0]
        y = faces[0][1]
        x1 = faces[0][0]+faces[0][2]
        y1 = faces[0][1]+faces[0][3]

        height = faces[0][3]
        width = faces[0][2]

        rect = cv2.rectangle(pic_data, (x, y), (x1, y1), [0, 255, 0], 5)
        # cv2.imshow("a.jpg",rect)
        # cv2.waitKey(10)

        crop = pic_data[y:y+width, x:x+height, :]
        cv2.imwrite("alert.jpg", crop)
        cv2.imshow("alert.jpg", crop)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

        # sending mail

        fromaddr = "1anujgupta123@gmail.com"
        toaddr = "1anujgupta123@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = ">>>>>>>>>>>>>>> ALERT NOTIFICATION <<<<<<<<<<<<<<<<<<<<"
        body = ">>>>>>>>> (    (   (  ( INTRUDER DETECTED )  )   )    ) >>>>>>>>>>>>>>"
        msg.attach(MIMEText(body, 'plain'))

        filename = "alert.jpg"
        attachment = open("alert.jpg", "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',
                     "attachment; filename= %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # stored file secretly on my device need to put ur pass their
        s.login(fromaddr, passwords.gmail)   #put either ur pass directly here or make a seperate file and import here 
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        time.sleep(1)

cv2.destroyAllWindows()
