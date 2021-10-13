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
            letter = "A"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and \
                Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "B"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "B"

        if Index_Dip_H + 30 >= Index_Tip_H >= Index_Dip_H - 30 and Middle_Dip_H + 30 >= Middle_Tip_H >= Middle_Dip_H - 30 and Ring_Dip_H + 30 >= Ring_Tip_H >= Ring_Dip_H - 30:
            if handLandmarks[4][3] == "Left" and Thumb_Tip_W < Thumb_Dip_W and Index_Tip_H <= Thumb_Tip_H:
                letter = "C"
            elif handLandmarks[4][3] == "Right" and Thumb_Tip_W > Thumb_Dip_W and Index_Tip_H <= Thumb_Tip_H:
                letter = "C"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "D"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "D"

        if Index_Tip_H > Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H and Middle_Tip_H + 20 >= Thumb_Tip_H  >= Middle_Tip_H - 20:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "E"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "E"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Index_Tip_H - 50 <= Thumb_Tip_H <= Index_Tip_H:
                letter = "F"
            elif handLandmarks[4][3] == "Right" and Index_Pip_W + 50 >= Thumb_Tip_W >= Index_Pip_W:
                letter = "F"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Index_Pip_W - 50 <= Thumb_Tip_W <= Index_Pip_W:
                letter = "G"
            elif handLandmarks[4][3] == "Right" and Index_Tip_H + 50 >= Thumb_Tip_H >= Index_Tip_H:
                letter = "G"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "H"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "H"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "I"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "I"

        if Index_Pip_H < Pinky_Pip_H: #and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Wrist_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "J"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "J"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Middle_MCP_W:
                letter = "K"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Middle_MCP_W:
                letter = "K"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:  # Right Thumb
                letter = "L"
            elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:  # Left Thumb
                letter = "L"

        if Index_Tip_H > Wrist_H and Middle_Tip_H > Wrist_H and Ring_Tip_H > Ring_Dip_H and Pinky_Dip_H < Index_Dip_H:
            letter = "M"

        if Index_Tip_H > Wrist_H and Middle_Tip_H > Wrist_H and Pinky_Tip_H > Pinky_MCP_H and Ring_Dip_H < Index_Dip_H and Pinky_Dip_H < Index_Dip_H:
            letter = "N"

        #if Index_Tip_H > Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            #if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
             #   letter = "O"
            #elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
              #  letter = "O"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "P"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "P"

        if Index_Tip_H < Middle_Dip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "Q"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "Q"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W and Middle_Tip_W < Index_Tip_W:
                letter = "R"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W and Middle_Tip_W > Index_Tip_W:
                letter = "R"

        if Index_Tip_H > Index_Pip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "S"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "S"

        if Index_Tip_H < Thumb_Tip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H and Thumb_Tip_H < Index_Pip_H:
            letter = "T"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W:
                letter = "U"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W:
                letter = "U"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W and Middle_Tip_W - 30 >= Index_Tip_W:
                letter = "V"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W and Middle_Tip_W <= Index_Tip_W - 30:
                letter = "V"

        if Index_Tip_H < Index_Pip_H and Middle_Tip_H < Middle_Pip_H and Ring_Tip_H < Ring_Pip_H and Pinky_Tip_H > Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Ring_MCP_W - 50 <= Thumb_Tip_W <= Ring_MCP_W and Middle_Tip_W - 30 >= Index_Tip_W and Ring_Tip_W - 30 >= Middle_Tip_W:
                letter = "W"
            elif handLandmarks[4][3] == "Right" and Ring_MCP_W + 50 >= Thumb_Tip_W >= Ring_MCP_W and Middle_Tip_W <= Index_Tip_W - 30 and Ring_Tip_W <= Middle_Tip_W - 30:
                letter = "W"

        if Index_Tip_H > Middle_Dip_H and Middle_Tip_H > Middle_Pip_H and Ring_Tip_H > Ring_Pip_H and Pinky_Tip_H < Pinky_Pip_H:
            if handLandmarks[4][3] == "Left" and Thumb_Tip_W < Thumb_Dip_W:
                letter = "Y"
            elif handLandmarks[4][3] == "Right" and Thumb_Tip_W > Thumb_Dip_W:
                letter = "Y"

        cv2.putText(image, letter, (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
        cv2.imshow("Volume", image)
        cv2.waitKey(1)
