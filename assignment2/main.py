from bmp import *
import os.path

def Invert(pixels):
    for i in range(len(pixels)) :
        for a in range(len(pixels[i])):
            for b in range(len(pixels[i][a])):
                pixels[i][a][b] = 255 - pixels[i][a][b]
                #print(pixels[i][a][b])

def DisplayChannel(pixels,channels):
    for i in range(len(pixels)) :
        for a in range(len(pixels[i])):
            for b in range(len(pixels[i][a])):
                if b != channels:
                    pixels[i][a][b] = 0
                    pass

def Flip(pixels,typeFlip):
    if typeFlip == "horizontally":
        for i in range(len(pixels)) :
            pixels[i].reverse()
    if typeFlip == "vertically":
        pixels.reverse()

def DrawRect(pixels,x1,y1,x2,y2):
    
    for i in range(len(pixels)) :
        for a in range(len(pixels[i])):
            if i == y1 and x2 >= a >=x1:
                pixels[i][a][0] = 250
                pixels[i][a][1] = 0
                pixels[i][a][2] = 0
            if i == y2 and x2 >= a >=x1:
                pixels[i][a][0] = 250
                pixels[i][a][1] = 0
                pixels[i][a][2] = 0
            if a == x1 and y1 >= i >=y2:
                pixels[i][a][0] = 250
                pixels[i][a][1] = 0
                pixels[i][a][2] = 0
            if a == x2 and y1 >= i >=y2:
                pixels[i][a][0] = 250
                pixels[i][a][1] = 0
                pixels[i][a][2] = 0            
            
def Grayscale(pixels):
    for i in range(len(pixels)) :
        for a in range(len(pixels[i])):
            temp = 0
            for b in range(len(pixels[i][a])):
                temp = pixels[i][a][b] + temp
                temp1 = temp//3
                pixels[i][a][0] = temp1
                pixels[i][a][1] = temp1
                pixels[i][a][2] = temp1
                
def Brightness(pixels,br):
    for i in range(len(pixels)) :
        for a in range(len(pixels[i])):
            for b in range(len(pixels[i][a])):
                if br == 1:
                    if pixels[i][a][b]+25 <= 255:
                        pixels[i][a][b] = pixels[i][a][b] + 25

                if br == 2:
                    if pixels[i][a][b]-25 >= 0:
                        pixels[i][a][b] = pixels[i][a][b] - 25

def Contrast(pixels,con):
    for i in range(len(pixels)) :
        for a in range(len(pixels[i])):
            for b in range(len(pixels[i][a])):
                if con == 1:
                    temp = int((1.4238)*(pixels[i][a][b] - 128) + 128)
                    if 0<= temp <= 255:
                        pixels[i][a][b] = temp
                    if temp > 255:
                        pixels[i][a][b] = 255
                    if temp < 0:
                        pixels[i][a][b] = 0
                    
                if con == 2:
                    temp = int((0.7016)*(pixels[i][a][b] - 128) + 128)
                    if 255 >= temp >= 0:
                        pixels[i][a][b] = temp
                    if temp > 255:
                        pixels[i][a][b] = 255
                    if temp < 0:
                        pixels[i][a][b] = 0



def main():
    listFunction = ['Invert', 'DisplayChannel', 'Flip', 'DrawRect', 'Grayscale', 'Brightness', 'Contrast']
    fileName = input("FileName *.bmp:")
    if os.path.isfile(fileName):
    #print(ReadBMP(fileName))
        pixelsTemp = ReadBMP(fileName)
    
    else: 
        print('No file found')
    
    #print(pixelsTemp[2][0])
    functionYouNeed = input("What you want to do: Invert, DisplayChannel, Flip, DrawRect, Grayscale, Brightness, Contrast:")
    if listFunction.count(functionYouNeed)>0:
        if functionYouNeed == "Invert":
            Invert(pixelsTemp)
            tempfile = 'inverted.bmp'
        
        if functionYouNeed == "DisplayChannel":
            channel = int(input("Channel (0) for Red, (1) for Green and (2) for Blue:"))
            DisplayChannel(pixelsTemp,channel)
            tempfile = 'channel.bmp'
        
        if functionYouNeed == "Flip":
            flipType = input("vertically or horizontally:")
            Flip(pixelsTemp,flipType)
            tempfile = 'flipped.bmp'
        
        if functionYouNeed == "DrawRect":
            x1,y1= input("A(x,y): ps. x,y :").split(",")
            x2,y2= input("B(x,y): ps. x,y :").split(",")
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            if(x1 > x2):
                temp = x2
                x2 = x1
                x1 = temp
            if(y2 > y1):
                temp = y2
                y2 = y1
                y1 = temp
            DrawRect(pixelsTemp,x1,y1,x2,y2)
            tempfile = 'drawRect.bmp'
        
        if functionYouNeed == "Grayscale":
            Grayscale(pixelsTemp)
            tempfile = 'grayscale.bmp'
        
        if functionYouNeed == "Brightness":
            br = int(input("increase (1) or decrease (2) brightness  (0) to quit:"))
            while br != 0:
                br = int(input("increase (1) or decrease (2) brightness  (0) to quit:"))
                Brightness(pixelsTemp,br)
            tempfile = 'brightness.bmp'
        
        if functionYouNeed == "Contrast":
            con = int(input("Contrast increase (1) or decrease (2)  (0) to quit:"))
            while con != 0:
                con = int(input("Contrast increase (1) or decrease (2)  (0) to quit:"))
                Contrast(pixelsTemp,con)
            tempfile = 'contrast.bmp'
        
        WriteBMP(pixelsTemp,tempfile)
    
    else:
        print("No fuction")


    
    #print(ReadBMP("inverted.bmp"))
    #print(pixelsTemp[2][0][0])
    

if __name__== "__main__":
        main()
    