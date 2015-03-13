#content=open("evil2.gfx").read()
#[open("12_%d.jpg"%i,"wb").write(content[i::5]) for i in range(5)]
s=open("evil2.gfx","rb").read()
 
for i in range(5):
    si=s[i::5]
    open("result"+str(i)+".jpg","wb").write(si)
print "Done!"

