import pandas as pd
import numpy as np
​
nama_file = input('Masukan file : ')
df = pd.read_csv(nama_file)
df = pd.read_csv(nama_file,na_values = ["na","-","NaN"])
x0 = int(input('Masukan Jumlah variabel : '))
hayo1 = []
for i in range(x0):
    va = input('Masukan nama variabel : ')
    hayo1.append(va)
df1 = df.loc[:,hayo1].values
n = len(df1)
df2 = df1[:,:]
n1 = len(df2[0])#jumlah dimensi
jmlcluster = int(input('Input jumlah cluster yang ingin diinput : '))
​
himpunan6 = []
for i in range(jmlcluster):
    himpunan6.append([])
​
jmlcentroid = []
for i in range(jmlcluster):
    centroid0 = int(input('Mau data ke berapa : '))
    jmlcentroid.append(df1[centroid0-1,:])
​
himpunan = []
for i in range(n):
    himpunan1 = []
    for j in range(jmlcluster):
        a1 = 0
        for k in range(n1):
            a1 += (df2[i][k] - jmlcentroid[j][k])**2
        a2 = np.sqrt(a1)
        himpunan1.append(a2)
    himpunan.append(himpunan1)
            
himpunan2 = []
himpunan3 = []
for i in range(n1*jmlcluster):
    himpunan3.append([])
​
himpunan2 = []
for i in range(n):
    cluster = 0
    for k in range(jmlcluster):
       if min(himpunan[i]) == himpunan[i][k]:
           cluster = k + 1
           for j in range(n1):
               himpunan3[cluster-1 + j*jmlcluster].append(df2[i][j])
    himpunan2.append(cluster)
​
clus = []    
for i in range(n):
    clus.append(0)
    
while himpunan2 != clus:
    clus = himpunan2
    #membuat centroid baru
    jmlcentroid = []
    for i in range(jmlcluster):
        jmlcentroid.append([])
    #centroid baru
    for i in range(jmlcluster):
        for j in range(n1):
            centroid1 = sum(himpunan3[i + j*jmlcluster])/len(himpunan3[i + j*jmlcluster])
            jmlcentroid[i].append(centroid1)
    
    himpunan = []
    for i in range(n):
        himpunan1 = []
        for j in range(jmlcluster):
            a1 = 0
            for k in range(n1):
                a1 += (df2[i][k] - jmlcentroid[j][k])**2
            a2 = np.sqrt(a1)
            himpunan1.append(a2)
        himpunan.append(himpunan1)
        
    himpunan3 = []
    for i in range(n1*jmlcluster):
        himpunan3.append([])
​
    himpunan2 = []
    for i in range(n):
        cluster = 0
        for k in range(jmlcluster):
            if min(himpunan[i]) == himpunan[i][k]:
                cluster = k + 1
                for j in range(n1):
                    himpunan3[cluster-1 + j*jmlcluster].append(df2[i][j])
        himpunan2.append(cluster)
​
df = df.drop('sas',axis = 1)
z= np.array(himpunan2)
df11 = pd.DataFrame(z)
df12 = pd.concat([df,df11],axis = 1)
pemain = df.loc[:,'Nama'].values
himpunan7 = []
himpunan8 = []
​
for i in range(jmlcluster):
    himpunan7.append([])
    himpunan8.append([])
        
for i in range(len(himpunan2)):
    if himpunan2[i] == 1:
        himpunan7[0].append(pemain[i])
        himpunan8[0].append(df2[i])
    if himpunan2[i] == 2:
        himpunan7[1].append(pemain[i])
        himpunan8[1].append(df2[i])
    if himpunan2[i] == 3:
        himpunan7[2].append(pemain[i])
        himpunan8[2].append(df2[i])
    if himpunan2[i] == 4:
        himpunan7[3].append(pemain[i])
        himpunan8[3].append(df2[i])
​
for i in range(jmlcluster):
    n3 = len(himpunan7[i])
    print('daftar pemain pada cluster ke',i+1)
    print('{0:^3}|{1:^30}|{2:^4}|{3:^4}|{4:^4}|{5:^4}|{6:^4}|'.format('No','Nama',hayo1[0],hayo1[1],hayo1[2],hayo1[3],hayo1[4]))
    for k in range(n3):
        print('{0:^3}|{1:^30}|{2:^4}|{3:^4}|{4:^4}|{5:^4}|{6:^4}|'.format(k+1,himpunan7[i][k],himpunan8[i][k][0],himpunan8[i][k][1],himpunan8[i][k][2],himpunan8[i][k][3],himpunan8[i][k][4]))
​
hayo = []
for i in range(x0):
    va =int(input('Masukan nilai variabel secara berurutan : '))
    hayo.append(va)
​
himpunan = []
for j in range(jmlcluster):
    a1 = 0
    for k in range(n1):
        a1 += (hayo[k] - jmlcentroid[j][k])**2
    a2 = np.sqrt(a1)
    himpunan.append(a2)
​
cluster = 0
for k in range(jmlcluster):
    if min(himpunan) == himpunan[k]:
        cluster = k + 1
​
print('Player similiar to :')
print('{0:^3}|{1:^30}|{2:^4}|{3:^4}|{4:^4}|{5:^4}|{6:^4}|'.format('No','Nama',hayo1[0],hayo1[1],hayo1[2],hayo1[3],hayo1[4]))
for i in range(5):
    print('{0:^3}|{1:^30}|{2:^4}|{3:^4}|{4:^4}|{5:^4}|{6:^4}|'.format(i+1,himpunan7[cluster-1][i],himpunan8[cluster-1][i][0],himpunan8[cluster-1][i][1],himpunan8[cluster-1][i][2],himpunan8[cluster-1][i][3],himpunan8[cluster-1][i][4]))