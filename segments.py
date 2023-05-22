import pytesseract
import cv2
import numpy as np
import random

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Read image

def segment_img(image_path,img_name,ch):
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Extract information 
    extractedInformation = pytesseract.image_to_string(img)

    list1=[]
    for i in range (5,256):
        list1.append(i)
    
    hImg,wImg,__=img.shape
    boxes=pytesseract.image_to_boxes(img)
    #print(boxes)
    #ch = input("Enter the char : ")
    sz=len(ch)
    for i in range(0,sz):
        if(ch[i]!='|'):
          for b in boxes.splitlines():
              j=random.choice(list1)
              k=random.choice(list1)
              l=random.choice(list1)
              #print(b)
              b=b.split(' ')
              x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
              
              if(b[0]==ch[i]):
                cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(j,k,l),2)
                cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(j,k,l),2)
                
        
    # Save the result image
    img_path="./static/media/Output/"+img_name;
    cv2.imwrite(img_path,img)
    output_image=cv2.imread(img_path)
    return img_path

    
    
if __name__=="__main__":
    
    segment('Input Data/n1.png','n1.png')
    