import numpy as np
import math


def matrixAverage(M, order):
    M = np.array(M)
    rval = 0
    for r in range(0, len(M)):
        for c in range(0, len(M[0])):
            rval += M[r, c]
    rval = rval / (order ** 2)
    rval = math.ceil(rval)
    return rval


def compressor(ImgMatrix, Order):
    ImgMatrix = np.array(ImgMatrix)
    Rows = len(ImgMatrix)
    Columns = len(ImgMatrix[0])
    StartRow, StartCol = 0, 0
    m = math.floor(Rows / Order)
    n = math.floor(Columns / Order)
    CompressedImg = np.empty((m, n))
    for i in range(0, m):
        StartCol = 0
        for j in range(0, n):
            M = ImgMatrix[StartRow: StartRow + Order, StartCol: StartCol + Order]
            compressedVal = matrixAverage(M, Order)
            CompressedImg[i, j] = int(compressedVal)
            StartCol += Order
        StartRow = StartRow + Order
        CompressedImg = CompressedImg.astype(np.uint8)
    return CompressedImg


def lessFrame(imgMatrix, skipVAl):
    imgMatrix = np.array(imgMatrix)
    rows = len(imgMatrix)
    columns = len(imgMatrix[0])
    m = math.floor(rows / skipVAl)
    n = math.floor(columns / skipVAl)
    startRow, startCol = 0, 0
    outputImg = np.empty((m, n))
    for i in range(0, m):
        startCol = 0
        for j in range(0, n):
            val = imgMatrix[startRow, startCol]
            outputImg[i, j] = val
            startCol += skipVAl
        startRow += skipVAl

    return outputImg.astype(np.uint8)

