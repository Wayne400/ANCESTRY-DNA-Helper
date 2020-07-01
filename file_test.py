
f = open("mvp_type.txt", "r")
text = f.readline()
f.close

if text == "02":
    CDRFilesLocation = "/efs/CDR/MVP02/active"
elif text == "02aaa":
    CDRFilesLocation = "/efs/CDR/MVP02AAA/active"
else:
    CDRFilesLocation = "/efs/CDR/MVPCI/active"

print (CDRFilesLocation)

