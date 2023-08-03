# basic loop
for i in range (6):
    print (i)



ax = df['medication'].value_counts() \
.head(10) \
.plot(kind = 'bar', title = 'Just a title')
ax.set_xlabel('Medicine')
ax.set_ylabel('Rx')
