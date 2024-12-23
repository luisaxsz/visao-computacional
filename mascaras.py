# Tipos de mascaras
# KNN, GMG,CNT,MOG,MOG2
# KNN -> Agrupa grupos de acordo com suas semelhanças
# GMG -> Teorema de Bayes
# CNT -> É utilizado na contagem de frames para encontrar o fundo ou o objeto de primeiro plano da imagem.
# MOG -> MOG é uma abreviação de Mixture of Gaussians, que em português podemos adaptar para Mistura de fundo adaptativa.
# Nela é feita uma distribuição gaussiana (também conhecida como distribuição normal para cada pixel, de forma que seja caracterizado por sua intensidade no espaço de cores RGB.

import cv2;
import sys;

from dill.temp import capture
from qtconsole.mainwindow import background
from sympy.strategies.core import switch

VIDEO = "Dados/Ponte.mp4";

algoritmo = ['KNN', 'GMG', 'CNT', 'MOG', 'MOG2'];
algoritmoSelecionado = algoritmo[4];

#KNN - 10.07 **
#GMG - 26.2
#CNT - 8.29 *
#MOG - 15.64
#MOG2 - 10.4 **

def Substractor(algoritmoSelecionado):
    match algoritmoSelecionado:
        case 'KNN':
            return cv2.createBackgroundSubtractorKNN();
        case 'GMG':
            return cv2.bgsegm.createBackgroundSubtractorGMG();
        case 'CNT':
            return cv2.bgsegm.createBackgroundSubtractorCNT();
        case 'MOG':
            return cv2.bgsegm.createBackgroundSubtractorMOG();
        case 'MOG2':
            return cv2.createBackgroundSubtractorMOG2();
        case _:
            return print("Algoritmo não encontrado"), sys.exit(1);


capture = cv2.VideoCapture(VIDEO);
# background_subtractor = Substractor(algoritmoSelecionado);
# e1 = cv2.getTickCount();

background_substractor = []
for i, a in enumerate(algoritmo):
    background_substractor.append(Substractor(a))
    print(background_substractor[i])

def main():
    while (capture.isOpened()):
        hasFrame, frame = capture.read();

        if not hasFrame:
            print("Fim dos Frames");
            break;


        knn = background_substractor[0].apply(frame);
        gmg = background_substractor[1].apply(frame);
        cnt = background_substractor[2].apply(frame);
        mog = background_substractor[3].apply(frame);
        mog2 = background_substractor[4].apply(frame);

        # frame_number += 1
        frame = cv2.resize(frame, (0, 0), fx=0.35, fy=0.35)

        cv2.imshow('Frame', frame);
        cv2.imshow('KNN', knn);
        cv2.imshow('GMG', gmg);
        cv2.imshow('CNT', cnt);
        cv2.imshow('MOG', mog);
        cv2.imshow('MOG2', mog2);

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break;

        # e2 = cv2.getTickCount();
        # time = (e2 - e1) / cv2.getTickFrequency();
        # print(time);
main();