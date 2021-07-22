from Detector import HandDetector
import cv2
import math
import numpy as np

handDetector = HandDetector(min_detection_confidence=0.7)
webcamFeed = cv2.VideoCapture(0)

while True:
    status, image = webcamFeed.read()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count = 0
    letter = "?"

    if (len(handLandmarks) != 0):

        Pinky_Tip_H = handLandmarks[20][2]
        Pinky_Dip_H = handLandmarks[19][2]
        Pinky_Pip_H = handLandmarks[18][2]
        Pinky_MCP_H = handLandmarks[17][2]

        Ring_Tip_H = handLandmarks[16][2]
        Ring_Dip_H = handLandmarks[15][2]
        Ring_Pip_H = handLandmarks[14][2]
        Ring_MCP_H = handLandmarks[13][2]

        Middle_Tip_H = handLandmarks[12][2]
        Middle_Dip_H = handLandmarks[11][2]
        Middle_Pip_H = handLandmarks[10][2]
        Middle_MCP_H = handLandmarks[9][2]

        Index_Tip_H = handLandmarks[8][2]
        Index_Dip_H = handLandmarks[7][2]
        Index_Pip_H = handLandmarks[6][2]
        Index_MCP_H = handLandmarks[5][2]

        Thumb_Tip_H = handLandmarks[4][2]
        Thumb_Dip_H = handLandmarks[3][2]
        Thumb_Pip_H = handLandmarks[2][2]
        Thumb_MCP_H = handLandmarks[1][2]

        Wrist_H = handLandmarks[0][2]

        Pinky_Tip_W = handLandmarks[20][1]
        Pinky_Dip_W = handLandmarks[19][1]
        Pinky_Pip_W = handLandmarks[18][1]
        Pinky_MCP_W = handLandmarks[17][1]

        Ring_Tip_W = handLandmarks[16][1]
        Ring_Dip_W = handLandmarks[15][1]
        Ring_Pip_W = handLandmarks[14][1]
        Ring_MCP_W = handLandmarks[13][1]

        Middle_Tip_W = handLandmarks[12][1]
        Middle_Dip_W = handLandmarks[11][1]
        Middle_Pip_W = handLandmarks[10][1]
        Middle_MCP_W = handLandmarks[9][1]

        Index_Tip_W = handLandmarks[8][1]
        Index_Dip_W = handLandmarks[7][1]
        Index_Pip_W = handLandmarks[6][1]
        Index_MCP_W = handLandmarks[5][1]

        Thumb_Tip_W = handLandmarks[4][1]
        Thumb_Dip_W = handLandmarks[3][1]
        Thumb_Pip_W = handLandmarks[2][1]
        Thumb_MCP_W = handLandmarks[1][1]

        Wrist_W = handLandmarks[0][1]
        # we will get y coordinate of finger-tip and check if it lies above middle landmark of that finger
        # details: https://google.github.io/mediapipe/solutions/hands

        # if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:  # Right Thumb
        #    count = count + 1
        # elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:  # Left Thumb
        #    count = count + 1
        # if handLandmarks[8][2] < handLandmarks[6][2]:  # Index finger
        #    count = count + 1
        # if handLandmarks[12][2] < handLandmarks[10][2]:  # Middle finger
        #    count = count + 1
        # if handLandmarks[16][2] < handLandmarks[14][2]:  # Ring finger
        #    count = count + 1
        # if handLandmarks[20][2] < handLandmarks[18][2]:  # Little finger
        #    count = count + 1

        if Index_Tip_H > Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H and Thumb_Tip_H < Index_Pip_H:
            letter = "a"

        #if (Pinky_Pip_H - 50 <= Ring_Pip_H <= Pinky_Pip_H or Pinky_Pip_H + 50 >= Ring_Pip_H >= Pinky_Pip_H) and (Ring_Pip_H - 50 <= Middle_Pip_H <= Ring_Pip_H or Ring_Pip_H + 50 >= Middle_Pip_H >= Ring_Pip_H) and (Middle_Pip_H - 50 <= Index_Pip_H <= Middle_Pip_H or Middle_Pip_H + 50 >= Index_Pip_H >= Middle_Pip_H) and (handLandmarks[4][3] == "Right" and Thumb_Tip_W > Thumb_Dip_W) or (handLandmarks[4][3] == "left" and Thumb_Tip_W > Thumb_Dip_W) and Index_Tip_H > Thumb_Tip_H:
         #   letter = "c"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and \
                Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "b"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "b"

        if Index_Dip_H + 30 >= Index_Tip_H >= Index_Dip_H - 30 and Middle_Dip_H + 30 >= Middle_Tip_H >= Middle_Dip_H - 30 and Ring_Dip_H + 30 >= Ring_Tip_H >= Ring_Dip_H - 30:
            if handLandmarks[4][3] == "Left" and Thumb_Tip_W < Thumb_Dip_W and Index_Tip_H <= Thumb_Tip_H:
                letter = "C"
            elif handLandmarks[4][3] == "Right" and Thumb_Tip_W > Thumb_Dip_W and Index_Tip_H <= Thumb_Tip_H:
                letter = "C"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "d"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "d"

        if Index_Tip_H > Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H and Middle_Tip_H + 20 >= Thumb_Tip_H  >= Middle_Tip_H - 20:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "e"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "e"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Index_Pip_W - 50 <= Thumb_Tip_W <= Index_Pip_W:
                letter = "g"
            elif handLandmarks[4][3] == "Right" and Index_Tip_H + 50 >= Thumb_Tip_H >= Index_Tip_H:
                letter = "g"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Index_Tip_H - 50 <= Thumb_Tip_H <= Index_Tip_H:
                letter = "f"
            elif handLandmarks[4][3] == "Right" and Index_Pip_W + 50 >= Thumb_Tip_W >= Index_Pip_W:
                letter = "f"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "h"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "h"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "I"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "I"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:  # Right Thumb
                letter = "L"
            elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:  # Left Thumb
                letter = "L"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Middle_MCP_W:
                letter = "k"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Middle_MCP_W:
                letter = "k"

        if Index_Tip_H > Wrist_H and Middle_Tip_H > Wrist_H and Ring_Tip_H > Ring_Dip_H and Pinky_Dip_H < Index_Dip_H:
            letter = "m"

        if Index_Tip_H > Wrist_H and Middle_Tip_H > Wrist_H and Pinky_Tip_H > Pinky_MCP_H and Ring_Dip_H < Index_Dip_H and Pinky_Dip_H < Index_Dip_H:
            letter = "n"

        #if Index_Tip_H > Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            #if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
             #   letter = "o"
            #elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
              #  letter = "o"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "q"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "q"

        if Index_Tip_H > Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H and Ring_Pip_H + 20 >= Thumb_Tip_H >= Ring_Pip_H - 20:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "s"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "s"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "u"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "u"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Thumb_Tip_W < Thumb_Dip_W:
                letter = "y"
            elif handLandmarks[4][3] == "Right" and Thumb_Tip_W > Thumb_Dip_W:
                letter = "y"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "p"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "p"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W and Middle_Tip_W < Index_Tip_W:
                letter = "r"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W and Middle_Tip_W > Index_Tip_W:
                letter = "r"

       # if Middle_Tip_H > Middle_MCP_H and Ring_Tip_H > Ring_MCP_H and Pinky_Tip_H > Pinky_MCP_H and Thumb_Tip_H >= Index_MCP_H and Index_Tip_H <= Index_Dip_H:
            #if handLandmarks[4][3] == "Left" and :
            #letter = "t"
            #elif handLandmarks[4][3] == "Right" and :
            #    letter = "t"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W and Middle_Tip_W - 80 >= Index_Tip_W:
                letter = "v"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W and Middle_Tip_W <= Index_Tip_W - 80:
                letter = "v"

        cv2.putText(image, letter, (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
        cv2.imshow("Volume", image)
        cv2.waitKey(1)
