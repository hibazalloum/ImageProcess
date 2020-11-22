import imgProcess

elsaImage = r'C:\Users\User\PycharmProjects\home work 4\elsa.jpg'
gray = imgProcess.convertGrey(elsaImage)
thumb = imgProcess.thumbnails(r'C:\Users\User\PycharmProjects\home work 4/')
hist = imgProcess.imageHistogram(elsaImage)
