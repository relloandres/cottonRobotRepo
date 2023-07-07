

while True:
    fileName = input("enter file name: ")
    if fileName == "exit":
        break
    data = getData(5)
    np.savetxt(f'./testData/{fileName}.csv', data, delimiter=',')
