from PIL import Image

def convertToAscii(filename):
    f = open("ascii.txt", "w")
    with Image.open(filename) as image:
        width, height = image.size
        image = image.convert("L")
        for y in range(height):
            for x in range(width):
                brightness = image.getpixel((x, y))
                if(brightness <= 16):
                    f.write(".")
                elif(brightness > 16 and brightness <= 32):
                    f.write(":")
                elif(brightness > 32 and brightness <= 48):
                    f.write("/")
                elif(brightness > 48 and brightness <= 64):
                    f.write("+")
                elif(brightness > 64 and brightness <= 80):
                    f.write("o")  
                elif(brightness > 80 and brightness <= 96):
                    f.write("O")  
                elif(brightness > 96 and brightness <= 112):
                    f.write("$")  
                elif(brightness > 112 and brightness <= 128):
                    f.write("B")  
                elif(brightness > 128 and brightness <= 144):
                    f.write("M")  
                elif(brightness > 144 and brightness <= 160):
                    f.write("W")
                elif(brightness > 160 and brightness <= 176):
                    f.write("&")  
                elif(brightness > 176 and brightness <= 192):
                    f.write("8")  
                elif(brightness > 192 and brightness <= 208):
                    f.write("%")
                elif(brightness > 208 and brightness <= 224):
                    f.write("#")   
                elif(brightness > 224 and brightness <= 255):
                    f.write("@")    
            f.write("\n")
    f.close()    
                               
                                                    
    
convertToAscii("image.png")        