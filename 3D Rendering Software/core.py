from math import sin, cos, tan, degrees, radians, pi, atan2
from tkinter import *
screen_x_min = -200
screen_x_max = 200
screen_y_min = -100
screen_y_max = 100
fov_degrees = 180
#"""
from turtle import *
ht()
pu()
speed(0)
colormode(255)
#"""
screen_width = screen_x_max-screen_x_min
screen_height = screen_y_max-screen_y_min
sig_digits = 3
render_distance_max = 128
root = Tk()
canvas = Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
rectobjects = []
class Camera:
    def __init__(self, x, y, z):
        self.x_rad = float(0)
        self.y_rad = float(0)
        self.x = x
        self.y = y
        self.z = z
class RectObject:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.color = [0,0,0]
        rectobjects.append(self)
        self.str =str("RectObject object between points (" + str(self.x1)+ "," + str(self.y1)+ "," + str(self.z1) + "), (" + str(self.x2)+ "," + str(self.y2) + "," + str(self.z2) + ")")
    def str(self):
        return self.str
    def __check_point_in_self__(self, x, y, z): # Checking if the points are in range. Have fun with the print blocks I added in.
        x_in = True
        y_in = True
        z_in = True
        """
        if x >= self.x1:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): X at or above lower bound")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): X below lower bound")
            x_in = False
        if x <= self.x2:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): X at or below upper bound")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): X above upper bound")
            x_in = False
        if y >= self.y1:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Y at or above lower bound")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Y below lower bound")
            y_in = False
        if y <= self.y2:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Y at or below upper bound")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Y above upper bound")
            y_in = False
        if z >= self.z1:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Z at or above lower bound")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Z below lower bound")
            z_in = False
        if z <= self.z2:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Z at or below upper bound")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Z above upper bound")
            z_in = False
        if x_in:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): X in range")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): X out of range")
        if y_in:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Y in range")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Y out of range")
        if z_in:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Z in range")
        else:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Z out of range")
        if x_in and y_in and z_in:
            print(str(self) + " __check_point_in_self__ (" + str(x) + "," + str(y) + "," + str(z) + "): Point inside object")
            return True
        else:
            return False
        """
        if x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2 and z >= self.z1 and z <= self.z2:
            return True
        else:
            return False
def mouse(event):
    x = event.x
    y = event.y
    print("(" + str(x) + "," + str(y) + ")")
#root.bind('<Motion>', mouse)
class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #"""
        self.x_rad = (x)*(1/screen_width)*((2*pi)/(360/fov_degrees)) # Set x and y angles, in radians, of the pixel relative to the point on the screen
        self.y_rad = (y)*(1/screen_height)*((2*pi)/(360/fov_degrees))
        #"""
        """
        self.x_rad =
        """
        self.color = [0,0,0]
    def __trace__(self, x_ang, y_ang, x1, y1, z1):
        for z in range(0, render_distance_max, 1):
            x = round(((z+z1)*tan(self.x_rad + x_ang) + x1), sig_digits)
            y = round(((z+z1)*tan(self.y_rad + y_ang) + y1), sig_digits)
            print("x: " + str(x) + "\n" + "y: " + str(y) + "\n" + "z: " + str(z))
    def __get_coords__(self, x_ang, y_ang, x1, y1, z1, z):
        x = round(((z+z1)*tan(self.x_rad + x_ang) + x1), sig_digits)
        y = round(((z+z1)*tan(self.y_rad + y_ang) + y1), sig_digits)
        return x,y
    def __find_next_object__(self, x_ang, y_ang, x1, y1, z1):
        for i in range(0, render_distance_max, 1):
            z = (tan(x_ang)*z1)+i
            for object in rectobjects:
                x = self.__get_coords__(x_ang, y_ang, x1, y1, z1, z)[0]
                y = self.__get_coords__(x_ang, y_ang, x1, y1, z1, z)[1]
                if object.__check_point_in_self__(self.__get_coords__(x_ang, y_ang, x1, y1, z1, z)[0], self.__get_coords__(x_ang, y_ang, x1, y1, z1, z)[1], z):
                    return z
        return False


#root.mainloop()

def init():
    global pixels
    global camera
    camera = Camera(0, 0, 0)
    pixels = []
    for i in range(0, screen_width + 1, 1):
        pixels.append([])
        for y in range(0, screen_height + 1, 1):
            pixels[i].append(Pixel(int(i + screen_x_min), int(y + screen_y_min)))
    file_in = open('rectobjects.txt')
    for line in file_in:
        line = line.split()
        rect = RectObject(int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]))
def loop():
    global pixels
    i = screen_x_min
    for thing in pixels:
        print(i)
        i += 1
        for px in thing:
            color = px.__find_next_object__(px.x_rad + camera.x_rad, px.y_rad + camera.y_rad, camera.x, camera.y, camera.z)
            if color:
                #"""
                canvas.create_rectangle((px.x, px.y)*2 , fill=("black"))
                #"""
                #"""
                pu()
                goto(px.x, px.y)
                pd()
                pencolor(0, 0, int(color))
                dot(1.5)
                #"""
init()
# Finding angle from each point to camera
def reverse(obj):
    angles = []
    for x in range(obj.x1, obj.x2, 1):
        for y in range(obj.y1, obj.y2, 1):
            for z in range(obj.z1, obj.z2, 1):
                x_rad = atan2(z, x)
                y_rad = atan2(z, y)
                angles.append({"x":round(x_rad,sig_digits), "y":round(y_rad,sig_digits)})
    return angles
for rectobject in rectobjects:
    print(rectobject.str)
    angles = reverse(rectobject)
    for angle in angles:
        x_angle = angle["x"]
        y_angle = angle["y"]
for thing in pixels:
    for px in thing:
        if {"x":round(px.x_rad, sig_digits),"y":round(px.y_rad,sig_digits)} in angles:
            canvas.create_rectangle((px.x, px.y)*2, fill="black")
            pu()
            goto(px.x, px.y)
            pd()
            pencolor(0, 0, 0)
            dot(1.5)
            print(px.x + " " + px.y)
#loop()
root.mainloop()
