import cv2
from matplotlib import pyplot as plt
import glob
import time



def make1 (Matrix):
    # menerima matrix sembarang
    # mengembalikan dalam bentuk array dengan panjang m*n dengan m baris dan n kolom 
    Array = []
    for i in range(len(Matrix)):
        for j in range (len(Matrix[0])):
            Array.append(Matrix[i][j])
    return Array


def readImg (img_path):
    # membaca image dari file
    # return bentuk matriksnya
    img = cv2.imread(img_path,0)
    return img


def showImg (img):
    # Untuk menampilkan gambar
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.show()


def getHimpunanImg(path, N):
    # mengembalikan himpunan of image
    # Asumsi isi file terurut selalu image1, image2, ..., imageN
    S = []
    for i in range (1,N+1):
        string = path+'image'+str(i)+'.jpg'
        A = readImg(string)
        S.append(A)
    return S


def averageImgV1(path, N):
    # merata-ratakan seluruh image
    # Asumsi isi file terurut selalu image1, image2, ..., imageN
    # Asumsi fungsi ini masih menganggap ukuran image 256 x 256
    rata = [[0 for j in range (256)] for k in range (256)]
    for i in range (1,N+1):
        string = path+'image'+str(i)+'.jpg'
        A = readImg(string)
        for x in range (0,255):
            for y in range (0,255):
                rata[x][y] = rata[x][y] + A[x][y]
    for v in range (256):
        for w in range (256):
            rata[v][w] = rata[v][w]/N
    return rata


def averageImgV2(path, N):
    # merata-ratakan seluruh image
    # Asumsi isi file terurut selalu image1, image2, ..., imageN
    # Asumsi fungsi ini masih menganggap ukuran image 256 x 256
    S = getHimpunanImg(path,N)
    rata = [[0 for i in range (256)] for j in range (256)]
    for k in range (N):
        for l in range (256):
            for m in range (256):
                rata[l][m] += S[k][l][m]
    for n in range (256):
        for o in range(256):
            rata[n][o] /= N,
    return rata


def averageImgV3(path,N):
    # merata-ratakan seluruh image
    # Asumsi isi file terurut selalu image1, image2, ..., imageN
    # Asumsi fungsi ini masih menganggap ukuran img sembarang tetapi semuanya sama
    S = getHimpunanImg(path,N)
    panjang = print(len(S[0]))
    lebar = print(len(S[0][0]))
    rata = [[0 for i in range (panjang)] for j in range (lebar)]
    for k in range (N):
        for l in range (panjang):
            for m in range (lebar):
                rata[l][m] += S[k][l][m]
    for n in range (panjang):
        for o in range(lebar):
            rata[n][o] /= N,
    return rata


def averageImgV4(path, N):
    # merata-ratakan seluruh image
    # Asumsi isi file terurut selalu image1, image2, ..., imageN
    # Ukuran image bisa berbeda
    S = getHimpunanImg(path,N)
    maxP = len(S[0])
    maxL = len(S[0][0])
    for i in range (N):
        if (len(S[i]) > maxP):
            maxP = len(S[i])
        if (len(S[i][i] > maxL)):
            maxL = len(S[i][i])
    # Saat ini didapat nilai terbesar image
    rata = [[0 for i in range (maxP)] for j in range (maxL)]
    for j in range (N):
        for k in range (len(S[j])):
            for l in range (len(S[j][j])):
                rata[k][l] += S[j][k][l]
    for m in range (maxP):
        for n in range (maxL):
            rata[m][n] /= N
    return rata


def getHimpunanImgV2(path):
    # Mendapatkan himpunan gambar hanya dengan memasukkan folder
    # File yang dibaca hanyalah bentuk jpg dengan nama sembarang
    file = glob.glob(str(path)+"/*")
    new_file = []
    for i in range (len(file)):
        new_file.append(file[i].replace("\\","/"))
    # new_file merupakan seluruh path yang ada di folder image
    S = []
    for j in range (len(new_file)):
        S.append(readImg(new_file[j]))
    return S

def averageImgV5(path):
    # merata-ratakan seluruh image dari folder path
    # isi folder sembarang, semua image berukuran sama
    S = getHimpunanImgV2(path)
    N = len(S)
    maxP = len(S[0])
    maxL = len(S[0][0])
    for i in range (N):
        if (len(S[i]) > maxP):
            maxP = len(S[i])
        if (len(S[i][0] > maxL)):
            maxL = len(S[i][0])
    # Saat ini didapat nilai terbesar image
    rata = [[0 for i in range (maxL)] for j in range (maxP)]
    for j in range (N):
        for k in range (len(S[j])):
            for l in range (len(S[j][0])):
                rata[k][l] += S[j][k][l]
    for m in range (maxP):
        for n in range (maxL):
            rata[m][n] /= N
    return rata
    
    
def averageImgV6(path):
    # merata-ratakan seluruh image dari folder path
    # isi folder sembarang dan ukuran bisa bervariasi
    S = getHimpunanImgV2(path)
    N = len(S)
    SET = 256
    for i in range (N):
        S[i] = cv2.resize(S[i], (SET,SET), fx = 1, fy = 1)
    rata = [[0 for i in range (SET)] for j in range (SET)]
    for j in range (N):
        for k in range (SET):
            for l in range (SET):
                rata[k][l] += S[j][k][l]
    for m in range (SET):
        for n in range (SET):
            rata[m][n] /= N
    return rata


def getColorImage(number, path):
    images = [cv2.imread(file) for file in glob.glob(path+'/*')]
    return images[number-1]

def getcolorImageV2(number, path):
    file = glob.glob(str(path)+"/*")
    new_file = []
    for i in range (len(file)):
        new_file.append(file[i].replace("\\","/"))
    return new_file[number-1]
    

# # Contoh driver:
''' start_time = time.time()
# # Note: directory bisa diganti
# # Fungsi yang efektif adalah averageImgV6 (versi keenam) dan getHimpunanImgV2 (versi kedua)
# newImg = averageImgV6('.\\test/classes_pins_dataset/pins_Adriana Lima')
newImg = averageImgV6('.\\test\\small_dataset\\1')
print("--- %s seconds ---" % (time.time() - start_time))
showImg(newImg)
 '''
