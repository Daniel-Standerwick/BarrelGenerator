################### BARREL CREATOR ######################

##Copyright Daniel Standerwick
### WARNING: MAKE SURE THERE IS NO DEFAULT SET NAMES i.e: set1 
### Creates barrels with differences in width, height, # of rings, drain hole location, and lids or not. 

import maya.cmds as cmds
import random as rand

cmds.select(cl = True)
cmds.softSelect(sse=1)
toBeGrouped = cmds.sets()
queryDic = {}

def UI():
    if cmds.window('window', exists = True):
        cmds.deleteUI("window")
        
    window = cmds.window("window", title = "Barrel Generator", w = 650, h = 250)
    cmds.columnLayout()
    cmds.text(label = '\n Welcome to my Barrel Generator, click the preferred preferences bellow & then press continue when ready to generate.\n\n')
    cmds.text(label = 'Lid Options:\n') 
    queryDic['lidControl'] = cmds.radioButtonGrp(label = 'Lid On or Off:\n\n\t', labelArray3 =["On", "Off", "Random"], select=3, numberOfRadioButtons=3 )
    queryDic['lidLoc'] = cmds.radioButtonGrp(label = 'Lid Location (If On):\n\n\t', labelArray4 =["On", "Skewed", "Leaning", "Random"], select=4, numberOfRadioButtons=4)
    cmds.button(label = 'CONTINUE', command = makeBarrel)
    cmds.showWindow('window')

def cleanUp():
    cmds.delete('set1')
    cmds.select(cl = True)
    cmds.deleteUI("window")
    
def makeBarrel(*args):
    #Molding and Shaping first Plank
    cmds.polyCube( sx=8, sy=8, sz=4, h=20 )
    cmds.scale( 1, 1, 0.3 )
    cmds.select('pCube1.e[32:39]', 'pCube1.e[128:135]', 'pCube1.e[420:423]', 'pCube1.e[472:475]')
    cmds.softSelect(ssd=19, sud=0.5)
    cmds.move( 0, 0, -2, relative = True)
    cmds.softSelect(ssd=12.5, sud=0.5)
    cmds.scale(1.4,1,1)
    cmds.softSelect(ssd=5, sud=0.2)
    cmds.select('pCube1.e[56:63]', 'pCube1.e[104:111]', 'pCube1.e[432:435]', 'pCube1.e[484:487]')
    cmds.scale(1.05,1,1)
    cmds.select('pCube1.e[8:15]', 'pCube1.e[152:159]', 'pCube1.e[408:411]', 'pCube1.e[460:463]')
    cmds.scale(1.05,1,1)
    cmds.sets('pCube1', addElement = toBeGrouped)
    
    #Moving WholePlank & Duplication Process
    cmds.select('pCube1.vtx[4]')
    cmds.softSelect(ssd=500, sud=1)
    cmds.move(-cmds.pointPosition('pCube1.vtx[4]')[0], -cmds.pointPosition('pCube1.vtx[4]')[1], -cmds.pointPosition('pCube1.vtx[4]')[2], relative = True)
    cmds.move(0,0,-4, rotatePivotRelative = True, relative = True)
    cmds.select('pCube1')
    cmds.rename('pCube1', 'BarrelPlank1')
    
    i=0
    while (i < 23):
        cmds.duplicate(returnRootsOnly = True)
        cmds.rotate(0,15,0, relative = True)
        i = i+1
        
    #Creates Metal Rings With Variation
    
    #Chance of Top Four Top Rings
    i = 0 
    numbOfTopRings = rand.randint(1,4)
    openLoc = [0,0,0,0]
    while (i < numbOfTopRings):
        location = rand.randint(0,3)
        while (openLoc[location] == 1):
            location = rand.randint(0,3)
        if(location == 0):
            #0
            cmds.softSelect(ssd=5, sud=0.2)
            cmds.polyTorus(sx=20, sy=8, r=1, sr=0.01)
            cmds.move(0,19.5,0,relative = True)
            cmds.scale(4.55,45.1,4.55, relative = True)
            cmds.select('pTorus1.e[40:59]')
            cmds.softSelect(ssd=1.05, sud = 0.2)
            cmds.scale(0.97, 0.97, 0.97, relative = True)
            cmds.sets('pTorus1', addElement = toBeGrouped)
            cmds.rename('pTorus1', 'MetalRing1')
            openLoc[location] = 1
        elif(location == 1):
            #1
            cmds.softSelect(ssd=5, sud=0.2)
            cmds.polyTorus(sx=20, sy=8, r=1, sr=0.01)
            cmds.move(0,18,0,relative = True)
            cmds.scale(4.83,45.1,4.83, relative = True)
            cmds.select('pTorus1.e[40:59]')
            cmds.softSelect(ssd=1.05, sud = 0.2)
            cmds.scale(0.97, 0.97, 0.97, relative = True)
            cmds.sets('pTorus1', addElement = toBeGrouped)
            cmds.rename('pTorus1', 'MetalRing1')
            openLoc[location] = 1
        elif(location == 2):
            #2
            cmds.softSelect(ssd=5, sud=0.2)
            cmds.polyTorus(sx=20, sy=8, r=1, sr=0.01)
            cmds.move(0,16.5,0,relative = True)
            cmds.scale(5.05,60,5.05, relative = True)
            cmds.select('pTorus1.e[40:59]')
            cmds.softSelect(ssd=1.05, sud = 0.2)
            cmds.scale(0.97, 0.97, 0.97, relative = True)
            cmds.sets('pTorus1', addElement = toBeGrouped)
            cmds.rename('pTorus1', 'MetalRing1')
            openLoc[location] = 1
        else:
            #3
            cmds.softSelect(ssd=5, sud=0.2)
            cmds.polyTorus(sx=20, sy=8, r=1, sr=0.01)
            cmds.move(0,12.5,0,relative = True)
            cmds.scale(5.45,70,5.45, relative = True)
            cmds.select('pTorus1.e[40:59]')
            cmds.softSelect(ssd=1.05, sud = 0.2)
            cmds.scale(0.98, 0.98, 0.98, relative = True)
            cmds.sets('pTorus1', addElement = toBeGrouped)
            cmds.rename('pTorus1', 'MetalRing1')
            
        i += 1   
    
    
    
    #Guarented bottom ring then a change of two others
    #Guarented
    cmds.softSelect(ssd=5, sud=0.2)
    cmds.polyTorus(sx=20, sy=8, r=1, sr=0.01)
    cmds.move(0,0.45,0,relative = True)
    cmds.scale(4.55,45.1,4.55, relative = True)
    cmds.select('pTorus1.e[120:139]')
    cmds.softSelect(ssd=1.05, sud = 0.2)
    cmds.scale(0.97, 0.97, 0.97, relative = True)
    cmds.sets('pTorus1', addElement = toBeGrouped)
    cmds.rename('pTorus1', 'MetalRing1')
    
    i = 0 
    numbOfTopRings = rand.randint(0,2)
    openLoc = [0,0]
    while (i < numbOfTopRings):
        location = rand.randint(0,1)
        while (openLoc[location] == 1):
            location = rand.randint(0,1)
        if(location == 0):
            #0
            cmds.softSelect(ssd=5, sud=0.2)
            cmds.polyTorus(sx=20, sy=8, r=1, sr=0.01)
            cmds.move(0,3.8,0,relative = True)
            cmds.scale(5.12,60,5.12, relative = True)
            cmds.select('pTorus1.e[120:139]')
            cmds.softSelect(ssd=1.05, sud = 0.2)
            cmds.scale(0.97, 0.97, 0.97, relative = True)
            cmds.sets('pTorus1', addElement = toBeGrouped)
            cmds.rename('pTorus1', 'MetalRing1')
            openLoc[location] = 1
        else:
            #1
            cmds.softSelect(ssd=5, sud=0.2)
            cmds.polyTorus(sx=20, sy=8, r=1, sr=0.01)
            cmds.move(0,5.5,0,relative = True)
            cmds.scale(5.38,60,5.38, relative = True)
            cmds.select('pTorus1.e[120:139]')
            cmds.softSelect(ssd=1.05, sud = 0.2)
            cmds.scale(0.97, 0.97, 0.97, relative = True)
            cmds.sets('pTorus1', addElement = toBeGrouped)
            cmds.rename('pTorus1', 'MetalRing1')
            openLoc[location] = 1
        i += 1 
    
    #Make the lid and bottom
    #Bottom
    cmds.polyCube(sx=2, sy = 1, sz = 1, h = 0.143, d = 8.07)
    cmds.sets('pCube1', addElement = toBeGrouped)
    cmds.move(0,0.143,0)
    #Create planks off of first
    i = 0
    while (i < 4):
        if(i<4):
            cmds.duplicate(returnRootsOnly = True)
            cmds.move(1.01,0,0, relative = True)
            i = i+1
            
    #Shape Planks into rounded bottom
    cmds.softSelect(sse=0)
    def shapeLidPlank(plank,scale1,scale2,scale3): #ScalesPlankEdges
        i = 0
        while (i < 2):
            selectCube = cmds.format('pCube^1s.e', stringArg=(plank))
            cmds.select("{0}[{1}]".format(selectCube,8), "{0}[{1}]".format(selectCube,11), "{0}[{1}]".format(selectCube,14), "{0}[{1}]".format(selectCube,17))
            cmds.scale(1, 1, scale1, relative = True)
            cmds.select("{0}[{1}]".format(selectCube,9), "{0}[{1}]".format(selectCube,12), "{0}[{1}]".format(selectCube,15), "{0}[{1}]".format(selectCube,18))
            cmds.scale(1, 1, scale2, relative = True)
            cmds.select("{0}[{1}]".format(selectCube,10), "{0}[{1}]".format(selectCube,13), "{0}[{1}]".format(selectCube,16), "{0}[{1}]".format(selectCube,19))
            cmds.scale(1, 1, scale3, relative = True)
            i = i+1
    
    shapeLidPlank(2,0.997351,0.98069,0.962469)
    shapeLidPlank(3,0.963,0.925,0.885)
    shapeLidPlank(4,0.8835,0.8,0.7)
    shapeLidPlank(5,0.698,0.4,0.2)
    cmds.select('pCube5.f[1]','pCube5.f[3]','pCube5.f[5]','pCube5.f[7:8]')
    cmds.delete()
    cmds.polyCloseBorder('pCube5.e[5]', 'pCube5.e[7]', 'pCube5.e[9]', 'pCube5.e[11]')
    #mirror half of the lid
    cmds.polyUnite('pCube1','pCube2','pCube3','pCube4','pCube5')
    cmds.delete(ch = True)
    cmds.polyMirrorFace( 'polySurface1', direction=0, mergeMode=1 )
    cmds.sets('polySurface1', addElement = toBeGrouped)
    cmds.rename('polySurface1', 'LidBottom')
    
    #Decide To create top & Where to Place Top
    lidOn = 0
    if(cmds.radioButtonGrp(queryDic['lidControl'], q=True, select=True)==3):
        lidOn = rand.randint(0,4)
    if(cmds.radioButtonGrp(queryDic['lidControl'], q=True, select=True)==1 or lidOn > 0):
        #createTop
        cmds.duplicate(returnRootsOnly = True)
        cmds.polyCube(w = 7.433, h = 0.13)
        cmds.move(0,0,0.973)
        cmds.select('pCube1.e[8:9]')
        cmds.scale(1.07,1,1, relative = True)
        cmds.polyMirrorFace( 'pCube1', direction = 0, mergeMode=1, axis = 2 )
        cmds.polyUnite( 'pCube1', 'LidBottom1', n='Lid' )
        cmds.sets('Lid', addElement = toBeGrouped)
        cmds.rename('Lid', 'LidTop')
        cmds.delete(ch = True)
        cmds.delete('LidBottom1')
        
        lidLocRan = 0
        if(cmds.radioButtonGrp(queryDic['lidLoc'], q=True, select=True)==4):
            lidLocRan = rand.randint(1,3)
        if(cmds.radioButtonGrp(queryDic['lidLoc'], q=True, select=True)==1 or lidLocRan==1):
            cmds.move(0,19.5,0)
        elif(cmds.radioButtonGrp(queryDic['lidLoc'], q=True, select=True)==2 or lidLocRan==2):
            cmds.move(0,19.5,0)
            cmds.rotate(0,rand.random()*359,rand.random()*16, r=True, ws = True)
            cmds.rotate(0,rand.random()*359,0, r=True, ws = True)
        elif(cmds.radioButtonGrp(queryDic['lidLoc'], q=True, select=True)==3 or lidLocRan==3):
            cmds.rotate(0,rand.random()*359, 98.852097)
            cmds.move(6.2,4.3,0)
            
            
    #Finaly Group everything in the toBeGrouped set and cleanup
    cmds.select( toBeGrouped )
    cmds.group( n='Barrel1' )
    cleanUp()

    
UI()