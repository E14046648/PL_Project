import  cv2
from math import pow
#载入并显示图片
img=cv2.imread('distance.jpg',-1)
size = img.shape
print(size[0])
imS = cv2.resize(img, (int(size[1]*0.1),int(size[0]*0.1)))  
cv2.imshow('img',imS)
#灰度化
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#输出图像大小，方便根据图像大小调节minRadius和maxRadius
print(img.shape)
#霍夫变换圆检测
circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=5,maxRadius=300)
#输出返回值，方便查看类型
print(circles)
#输出检测到圆的个数
print("number")
print(len(circles[0]))

print('-----------------------------------')
#根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    #圆的基本信息
    print(circle[2])
    #坐标行列
    x=int(circle[0])
    y=int(circle[1])
    #半径
    r=int(circle[2])
    #在原图用指定颜色标记出圆的位置
    img=cv2.circle(img,(x,y),r,(0,255,0),-1)
x_squre=pow((circles[0][1][0]-circles[0][2][0]),2)
y_squre=pow((circles[0][1][1]-circles[0][2][1]),2)
dis=(x_squre+y_squre)**0.5
prop=dis/15 #cm
x_squre=pow((circles[0][0][0]-circles[0][2][0]),2)
y_squre=pow((circles[0][0][1]-circles[0][2][1]),2)
dis=(x_squre+y_squre)**0.5
print(dis/prop)
x_squre=pow((circles[0][0][0]-circles[0][1][0]),2)
y_squre=pow((circles[0][0][1]-circles[0][1][1]),2)
dis=(x_squre+y_squre)**0.5
print(dis/prop)
#显示新图像
#line(img, (circles[0][0][0],circles[0][0][1]),(circles[0][1][0],circles[0][1][1]), (0,255,0), thickness=1,lineType=8, shift=0)
img = cv2.resize(img, (int(size[1]*0.1),int(size[0]*0.1))) 
cv2.imshow('res',img)

#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()