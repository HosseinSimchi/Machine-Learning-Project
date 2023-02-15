from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
angle1 = np.arange(0,6,0.006)
r1 =np.random.randint(0,6,angle1.shape[0])
x0= r1 * np.cos(angle1) + 5
y0= r1 * np.sin(angle1) + 5
#plt.scatter(z,r)
angle2 = np.arange(0,7,0.006)
r =np.random.randint(0,6,angle2.shape[0])
x= r * np.cos(angle2) + 25
y= r * np.sin(angle2) + 5
#plt.scatter(x,y)
angle3 = np.arange(0,7,0.006)
r =np.random.randint(0,6,angle3.shape[0])
x1= r * np.cos(angle3) + 5
y1= r * np.sin(angle3) + 20
#plt.scatter(x1,y1)
angle4 = np.arange(0,7,0.006)
r =np.random.randint(0,6,angle4.shape[0])
x2= r * np.cos(angle4) + 25
y2= r * np.sin(angle4) + 20
#plt.scatter(x2,y2)
xx = []
yy = []
for i in range(len(x0)):
    xx.append(x0[i])
    yy.append(y0[i])
for i in range(len(x)):
    xx.append(x[i])
    yy.append(y[i])
for i in range(len(x1)):
    xx.append(x1[i])
    yy.append(y1[i])
for i in range(len(x2)):
    xx.append(x2[i])
    yy.append(y2[i])
    

xt = []
sum2 = 0
p =[]
y_predd = []
sum3=[]


#we need to convert x1 and y1 to array to use in the gradient descent method
x1 = np.array(xx)
y1 = np.array(yy)
plt.scatter(x1,y1)

###closed equation and find the best line to classify data###
xtest = np.array([[2],[0.1],[1.75],[1.25],[1.7],[1.2],[22.5],[27.6]])
x =np.c_[np.ones((len(x1),1)),x1]
zaviye = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y1)
xtestb = np.c_[np.ones((len(xtest),1)),xtest]
ypred = xtestb.dot(zaviye)
plt.title('2 Dimensional Closed Equation ')
plt.plot(xtest,ypred,'r')
plt.show()

m =0
c =0
M=[]
C=[]

###gradient descent method and after some epochs we'll converg to a best line to classify data###

l = 0.9 #learning rate 
epochs = 30

n = int(len(x1))
#define a function to draw a line to converg a line
#y_pred = m*x1 + c 
def plot_line( y , data_points,i) :
    x_values = data_points#[ i for i in range(int(min(data_points))-1 , int(max(data_points))+2)]
    y_values = y #[ y_pred for x in x_values]
    if 0<=i<10  :
        plt.plot(x_values, y_values, 'orange')
    if 10<=i<20:
        plt.plot(x_values, y_values, 'blue')
    if 20<=i<30:
        plt.plot(x_values, y_values, 'green')
# we define a for loop to find a best line after some epochs


for i in range(epochs):
    y_pred = m*x1 + c
    d_m = (2/n) * sum(x1 * (y_pred - y1[i]))
    d_c = (2/n) * sum(y_pred - y1[i])
    m = m - l * d_m #update m in each iteration
    c = c - l * d_c #update c in each iteration
    M.append(m)
    C.append(c)
    plot_line(y_pred,x1,i)
#draw a circle again
print('Optimum m in "y = m * x + c" is {}'.format(M[29]))
print('Optimum c in "y = m * x + c" is {}'.format(C[29]))
plt.title('2 Dimensional Gradient Descent ')
plt.scatter(x1,y1)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
#we define a mean square error function to find a error in every update and epoch
sum2=0
sm = []
smm=[]
smm1 = []
epoch = np.arange(30)

for j in range(len(M)):
    for i in range(len(x1)):
        y = M[j] * x1[i] + C[j]
        y_predd.append(y)
    for i in range(len(x1)):
        #mean square error formula
        sum2 = (1/len(y_predd))*(((y1[i] - y_predd[i])*(y1[i] - y_predd[i])))
        smm.append(sum2)
        smm1.append(sum2)
        sum2 = 0
    sm.append(np.sum(smm))
    smm = []
#we draw a 2 dimensional plot for error function that we found
plt.title('2 Dimensional MSE Error Function')
plt.plot(sm)
plt.xlabel('EPOCHS')
plt.ylabel('MSE_ERROR_2D')
plt.show()

    
def draw_3d_plot():
    #we draw a 3 dimensional plot for error function that we found
    x11,x12= np.meshgrid(sm,sm)
    z11,z12 = np.meshgrid(M,C)
    fig = plt.figure(figsize = (8,8))
    ax = fig.gca(projection = '3d')
    s= ax.plot_surface(z11,z12,x11,cmap = plt.cm.rainbow)
    cset = ax.contour(z11,z12,x11,zdir='z',offset=0,cmap = plt.cm.rainbow)#define contour for 3D plot
    plt.title('3 Dimensional Error Function with draw 3 Dimensional contour')
    plt.ylabel('C : from y_pred = x * M + C')
    plt.xlabel('M : from y_pred = x * M + C')
    plt.show()
    plt.title('2 Dimensional contour by showing direction of convergence')
    plt.xlabel('M : from y_pred = x * M + C')
    plt.ylabel('Error')
    plt.contourf(z11,x12,x11)# define a 2 dimensional countor for 3D plot
    plt.colorbar();
    plt.scatter(z11,x11,marker='v',color="yellow")
    plt.show()
draw_3d_plot()
#we define a MAE function to find a error in every update and epoch
sum2=0
sm = []
smm=[]
for j in range(len(M)):
    for i in range(len(x1)):
        y = M[j] * x1[i] + C[j]
        y_predd.append(y)
    for i in range(len(x1)):
        sum2 = (1/len(y_predd))*abs(((y1[i] - y_predd[i])))
        smm.append(sum2)
        sum2 = 0
    sm.append(np.sum(smm))
    smm = []
plt.title('2 Dimensional MAE Error Function')
plt.plot(sm)
plt.xlabel('EPOCHS')
plt.ylabel('MSA_ERROR_2D')
plt.show()
draw_3d_plot()
plt.show()
#we define a UKA function to find a error in every update and epoch
sum2=0
sm = []
smm=[]
for j in range(len(M)):
    for i in range(len(x1)):
        y = M[j] * x1[i] + C[j]
        y_predd.append(y)
    for i in range(len(x1)):
        sum2 = (1/len(y_predd))*((y1[i] - y_predd[i]))
        smm.append(sum2)
        sum2 = 0
    sm.append(np.sum(smm))
    smm = []
plt.title('2 Dimensional UKE Error Function')
plt.plot(sm)
plt.xlabel('EPOCHS')
plt.ylabel('UKE_ERROR_2D')
plt.show()
draw_3d_plot()



    




