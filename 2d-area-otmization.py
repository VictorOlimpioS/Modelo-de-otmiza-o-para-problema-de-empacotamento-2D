import math


def get_dimensions(content):
    while True:
        try:
            dimension = int(input(f'Digite a {content} do item: '))
            if dimension <= 0:
                print(f"A {content} deve ser maior que zero.")
            else:
                return dimension
        except ValueError:
            print(f'Erro! Digite uma {content} válida.')

while True:
    containerHeight = get_dimensions('altura do container')
    containerWidth = get_dimensions('largura do container')
    objectHeight = get_dimensions('altura do objeto')
    objectWidth = get_dimensions('largura do objeto')

    if((objectHeight > containerHeight and objectHeight > containerWidth) or ( objectWidth > containerHeight and objectWidth > containerWidth)):
        print('Erro! A área não comporta o item')




    ## encontrando melhor layout inicial

    ## Layout 1
    partHeightToHeight = 0
    partWidthToWidth = 0

    partHeightToHeight = math.floor(containerHeight/objectHeight)
    partWidthToWidth = math.floor(containerWidth/objectWidth)

    ## Layout 1
    partHeightToWidth = 0
    partWidthToHeight = 0
    if(objectHeight != objectWidth):
        partHeightToWidth = math.floor(containerHeight/objectWidth)
        partWidthToHeight = math.floor(containerWidth/objectHeight)


    ## Guardando os valores dos layouts em variáveis 

    layout1, layout2 =  partHeightToHeight * partWidthToWidth, partHeightToWidth * partWidthToHeight 


    totalResult = 0
    matrixResult = None


    if (layout1 >= layout2):
        layoutMatrix1 = {'height': partHeightToHeight, 'width': partWidthToWidth}
        widthBoxes = containerWidth - (layoutMatrix1['width'] * objectWidth)
        HeightBoxes = containerHeight - (layoutMatrix1['height'] * objectHeight)
        print(layoutMatrix1, widthBoxes, HeightBoxes)
        if(objectWidth <= HeightBoxes):
            newLayout = int(HeightBoxes/objectWidth)
            layoutComplement =  math.floor(containerWidth/objectHeight)
            layoutComplementMatrix = {'height':newLayout , 'width':layoutComplement }
            totalResult = layout1 + layoutComplement
            matrixResult = layoutMatrix1
            print('Total de objetos: ', totalResult, '\nLayout 1--> ',matrixResult,'Altura do objeto paralela a altura da caixa\n', "Layout complementar--> ", layoutComplementMatrix, ' Posição do item  contrária a orientação do layout 1')
            break
        elif(objectHeight <= widthBoxes):
            print('aqui')
            newLayout = int(widthBoxes/objectHeight)
            layoutComplement = math.floor(containerHeight/objectWidth)
            layoutComplementMatrix = {'height': layoutComplement, 'width': newLayout}
            totalResult = layout1 + layoutComplement
            matrixResult = layoutMatrix1
            print('Total de objetos: ', totalResult, '\nLayout 1--> ',matrixResult,' Altura do objeto paralela a altura da caixa\n', "Layout complementar--> ", layoutComplementMatrix, ' Posição do item  contrária a orientação do layout 1')
            break
        else: 
            totalResult = layout1
            matrixResult = layoutMatrix1
            print('Total de objetos: ', totalResult, '\nLayout 1--> ',matrixResult, ' Altura do objeto paralela a altura da caixa')
            break


    else:
        layoutMatrix2 = {'height': partHeightToWidth, 'width': partWidthToHeight}
        widthBoxes = containerWidth - (layoutMatrix2['width'] * objectHeight)
        HeightBoxes = containerHeight - (layoutMatrix2['height'] * objectWidth)
        print(layoutMatrix2, widthBoxes, HeightBoxes)
        if(objectHeight <= HeightBoxes):
            newLayout = int(HeightBoxes/objectHeight)
            layoutComplement = math.floor(containerWidth/objectWidth)
            layoutComplementMatrix = {'height': newLayout, 'width': layoutComplement}
            totalResult = layout2 + layoutComplement
            matrixResult = layoutMatrix2
            print('Total de objetos: ', totalResult, '\nLayout 2--> ',matrixResult,' Altura do objeto perpendicular a altura da caixa\n', "Layout complementar--> ", layoutComplementMatrix, ' Posição do item  contrária a orientação do layout 2')
            break
        elif(objectWidth <= widthBoxes):
            newLayout = int(widthBoxes/objectWidth)
            layoutComplement = math.floor(containerHeight/objectHeight)
            layoutComplementMatrix = {'height': layoutComplement, 'width':newLayout}
            totalResult = layout2 + layoutComplement
            matrixResult = layoutMatrix2
            print('Total de objetos: ', totalResult, '\nLayout 2--> ',matrixResult,' Altura do objeto perpendicular a altura da caixa\n', "Layout complementar--> ", layoutComplementMatrix, ' Posição do item  contrária a orientação do layout 1')
            break
        else: 
            totalResult = layout2 
            matrixResult = layoutMatrix2
            print('Total de objetos: ', totalResult, '\nLayout 2--> ',matrixResult, ' Altura do objeto perpendicular a altura da caixa')
            break


        
        
        


        


        
    
        



