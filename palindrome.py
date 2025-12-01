{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOlN5X0+33fyC1887JFzpQn",
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
        "<a href=\"https://colab.research.google.com/github/Roycereano/python-practice/blob/main/palindrome.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "word = 'racecar'\n",
        "word == word.lower()\n",
        "reversed_word = word[::-1]\n",
        "\n",
        "if word == reversed_word:\n",
        "  print(f\"{word} is a palindrome!\")\n",
        "else:\n",
        "  print(f\"{word} is not a palindrome\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CvzEjkyyX3Hj",
        "outputId": "c18e8c52-5459-49cc-8c7a-143488d569be"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "racecar is a palindrome!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def reverse_word():\n",
        "\n",
        "  while True:\n",
        "    print(\"\\nEnter 'quit' to stop the program\")\n",
        "    user_input = input(\"\\nEnter a word to test if it's a palindrome: \")\n",
        "\n",
        "    if user_input.lower() == 'quit':\n",
        "      print(\"\\nThanks for using the palindrome checker!\")\n",
        "      break\n",
        "\n",
        "    word = user_input.lower()\n",
        "    reversed_word= word[::-1]\n",
        "\n",
        "    if word == reversed_word:\n",
        "     print(f\"\\n{user_input} is a palindrome\")\n",
        "    else:\n",
        "      print(f\"\\n{user_input} is not a palindrome\")\n",
        "\n",
        "reverse_word()"
      ],
      "metadata": {
        "id": "8JvDhRSZY0u4"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}