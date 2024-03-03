import math


# bigAreaWidth = 30
# bigAreaHeight = 150
# boxWidth= 30
# boxHeight = 50


while True:
    boxHeight = int(input('digite a altura do item: '))
    if(int(boxHeight) <= 0):
        boxHeight = int(input('Erro! digite uma altura Válida: '))

    boxWidth = int(input('digite a largura do item: '))
    if(int(boxWidth) <= 0):
        boxWidth = int(input('Erro! digite uma largura Válida: '))

    bigAreaHeight = int(input('digite a altura da área: '))
    if(int(bigAreaHeight) <= 0):
        bigAreaHeight = int(input('Erro! digite uma altura Válida: '))

    bigAreaWidth = int(input('digite a largura da área: '))
    if(int(bigAreaWidth) <= 0):
        bigAreaWidth = int(input('Erro! digite uma largura Válida: '))

    if((boxHeight > bigAreaHeight or boxHeight > bigAreaWidth or boxWidth > bigAreaHeight or boxWidth > bigAreaWidth) and bigAreaWidth == bigAreaHeight ):
        print('A área não comporta o item')
        break 
    if((boxHeight > bigAreaHeight and boxHeight > bigAreaWidth) or( boxWidth > bigAreaHeight and boxWidth > bigAreaWidth) ):
        print('A área não comporta o item')
        break 


    ## encontrando melhor layout inicial

    ## Layout 1
    partHeightToHeight = 0
    partWidthToWidth = 0

    partHeightToHeight = math.floor(bigAreaHeight/boxHeight)
    partWidthToWidth = math.floor(bigAreaWidth/boxWidth)

    ## Layout 1
    partHeightToWidth = 0
    partWidthToHeight = 0
    if(boxHeight != boxWidth):
        partHeightToWidth = math.floor(bigAreaHeight/boxWidth)
        partWidthToHeight = math.floor(bigAreaWidth/boxHeight)


    ## Guardando os valores dos layouts em variáveis 

    layout1, layout2 =  partHeightToHeight * partWidthToWidth, partHeightToWidth * partWidthToHeight 


    totalResult = 0
    matrixResult = None


    if (layout1 >= layout2):
        layoutMatrix1 = {'height': partHeightToHeight, 'width': partWidthToWidth}
        widthBoxes = bigAreaWidth - (layoutMatrix1['width'] * boxWidth)
        HeightBoxes = bigAreaHeight - (layoutMatrix1['height'] * boxHeight)
        print(layoutMatrix1, widthBoxes, HeightBoxes)
        if(boxWidth <= HeightBoxes):
            newLayout = int(HeightBoxes/boxWidth)
            layoutComplement = newLayout * layoutMatrix1['height']
            layoutComplementMatrix = {'height': newLayout, 'width': layoutMatrix1['height']}
            totalResult = layout1 + layoutComplement
            matrixResult = layoutMatrix1


            
        else: 
            totalResult = layout1
            matrixResult = layoutMatrix1

    else:
        layoutMatrix2 = {'height': partHeightToWidth, 'width': partWidthToHeight}
        widthBoxes = bigAreaWidth - (layoutMatrix2['width'] * boxHeight)
        HeightBoxes = bigAreaHeight - (layoutMatrix2['height'] * boxWidth)
        print(layoutMatrix2, widthBoxes, HeightBoxes)
        if(boxWidth <= widthBoxes):
            newLayout = int(widthBoxes/boxWidth)
            layoutComplement = newLayout * layoutMatrix2['width']
            layoutComplementMatrix = {'height': layoutMatrix2['width'], 'width': newLayout}
            totalResult = layout2 + layoutComplement
            matrixResult = layoutMatrix2
        else: 
            totalResult = layout2 
            matrixResult = layoutMatrix2

        
        
        
print(totalResult, matrixResult) 


        


        
    
        



