# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h: list[int], word: str) -> int:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    heights = [h[ALPHABET.index(l)] for l in word]
    return max(heights) * len(word)