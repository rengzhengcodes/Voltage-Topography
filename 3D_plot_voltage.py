# library
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

 

#I wound up not using these libraries, but you can do more cool stuff if you do
import seaborn as sns
import numpy as np 
 
# Get the data 
data = pd.read_csv('e_field.csv')
 
# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# Transform the spreadsheet rows and columns into centimeters
df['X']=pd.Categorical(df['X'])

df['X']=df['X'].cat.codes*2 +1

df['Y']=pd.Categorical(df['Y'])

df['Y']=df['Y'].cat.codes*2 +1

# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.coolwarm, linewidth=0.2)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.inferno, linewidth=0.2)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.RdBu, linewidth=0.2)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.PiYG, linewidth=0.2)
ax.set_xlabel('X coordinate (cm)')
ax.set_ylabel('Y coordinate (cm)')
ax.set_zlabel('Voltage (V)')

plt.title('Electric Potential Scalar Field')

plt.show()
 


 

