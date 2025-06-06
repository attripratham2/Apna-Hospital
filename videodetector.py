{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP83aqwR5KVk//AkTsYx6az",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/attripratham2/Apna-Hospital/blob/main/videodetector.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EdfXloACu7TV",
        "outputId": "1f80394a-fe4b-4850-fcc6-443bd5ba3c05"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Failed to read frame from camera. Exiting loop.\n"
          ]
        }
      ],
      "source": [
        "import cv2  # opencv\n",
        "import time  # delay\n",
        "import imutils  # resize\n",
        "\n",
        "cam = cv2.VideoCapture(0)\n",
        "time.sleep(1)\n",
        "\n",
        "firstFrame = None\n",
        "area = 500\n",
        "\n",
        "while True:\n",
        "    _, img = cam.read()\n",
        "\n",
        "    # Check if the frame was successfully read\n",
        "    if img is None:\n",
        "        print(\"Failed to read frame from camera. Exiting loop.\")\n",
        "        break # Exit the loop if no frame is read\n",
        "\n",
        "    text = \"Normal\"\n",
        "\n",
        "    img = imutils.resize(img, width=500)\n",
        "\n",
        "    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
        "\n",
        "    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # smoothening\n",
        "\n",
        "    if firstFrame is None:\n",
        "        firstFrame = gaussianImg\n",
        "        continue\n",
        "\n",
        "    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  # absolute diff if any change\n",
        "\n",
        "    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]\n",
        "\n",
        "    threshImg = cv2.dilate(threshImg, None, iterations=2)  # dilate for better contour detection\n",
        "\n",
        "    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n",
        "    cnts = imutils.grab_contours(cnts)\n",
        "\n",
        "    for c in cnts:\n",
        "        if cv2.contourArea(c) < area:\n",
        "            continue\n",
        "\n",
        "        (x, y, w, h) = cv2.boundingRect(c)\n",
        "        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)\n",
        "        text = \"Moving Object detected\"\n",
        "\n",
        "    print(text)\n",
        "    cv2.putText(img, text, (10, 20),\n",
        "                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)\n",
        "\n",
        "    cv2.imshow(\"cameraFeed\", img)\n",
        "\n",
        "    key = cv2.waitKey(10)\n",
        "    print(key)\n",
        "    if key == ord(\"q\"):\n",
        "        break\n",
        "\n",
        "cam.release()\n",
        "cv2.destroyAllWindows()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8ldCAgSlvILo"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}