from random import random
from random import randint
from random import shuffle

from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL import Image
import numpy




def create_square(color, position):
    glColor3d(color[0], color[1], color[2])
    glBegin(GL_POLYGON)
    glVertex2d(position[0][0], position[0][1])
    glVertex2d(position[1][0], position[1][1])
    glVertex2d(position[2][0], position[2][1])
    glVertex2d(position[3][0], position[3][1])

    glEnd()
    glFlush()


def re_create():
    glClearColor(0.4, 0.4, 0.4, 1.0)  # cor de fundo
    glClear(GL_COLOR_BUFFER_BIT)

    colorStench = (0.75, 0.56, 0)
    colorWumpus = (0.47, 0.24, 0.015)
    colorAgent = (0.6, 0.6, 0.7)
    colorWhite = (1, 1, 1)
    colorGSB = (0.83, 1, 0.82)
    colorBreeze = (0.64, 0.76, 0.95)
    colorPit = (0, 0, 0)
    colorSB = (1, 1, 0.60)

    mapRand = randint(1, 3)
    print("mapRand", mapRand)

    colorsLRooms = []

    if mapRand == 1:
        colorsLRooms = [ colorBreeze, colorPit, colorBreeze, colorWhite, colorStench,  colorBreeze, colorPit, colorSB,
                         colorWumpus, colorStench, colorBreeze,  colorPit,   colorGSB, colorWhite, colorWhite]
    elif mapRand == 2:
         colorsLRooms = [colorStench, colorWhite, colorWhite, colorStench, colorWumpus, colorGSB, colorWhite, colorBreeze,
                         colorSB, colorPit, colorBreeze, colorPit, colorBreeze, colorBreeze, colorWhite]
    elif mapRand == 3:
         colorsLRooms = [colorStench, colorWumpus,  colorStench, colorBreeze, colorWhite, colorGSB, colorWhite,
                         colorPit, colorBreeze, colorPit, colorBreeze, colorBreeze, colorWhite, colorBreeze, colorPit]
    #shuffle(colorsLRooms)


    vInit = 0.18
    printLRoom = 6
    pointInit = vInit
    qtdLRoom = 5
    nCicle = 1

    for c in range(1, qtdLRoom):
        LRoom = vInit
        for a in range(1, qtdLRoom):
            if pointInit == vInit and LRoom == vInit:
               create_square((colorAgent), ((pointInit, LRoom), (printLRoom * (c), LRoom), (printLRoom * (c), printLRoom *(a)), (pointInit, printLRoom *(a))))
            else:
                create_square((colorsLRooms[nCicle-1]), ((pointInit, LRoom), (printLRoom * (c), LRoom), (printLRoom * (c), printLRoom * (a)), (pointInit, printLRoom * (a))))
                nCicle += 1
            LRoom = (printLRoom * a) +vInit
        pointInit = (printLRoom * c) +vInit


    agente = Image.open("imagens/agente/arqueiro.png")
    #img_data = numpy.array(list(agente.getdata()), numpy.uint8)
    flipped_image = agente.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = flipped_image.convert("RGBA").tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, agente.width, agente.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    print(agente.width, agente.height)


def tecle(key, x=0, y=0):
    if ord(key) == 27:
        exit()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(520, 400)
glutCreateWindow(b'WOLRD WUMPUS')
glutDisplayFunc(re_create)
glutKeyboardFunc(tecle)
glOrtho(-2, 27, -2, 27, -1, 1)
glutMainLoop()