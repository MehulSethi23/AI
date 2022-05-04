import math

def MinMax(cur, i, maxTurn, score, target):
    
    if cur == target:
        return scores[i]
    if maxTurn:
        return max(MinMax(cur+1, i*2, False, scores, target),
                  MinMax(cur+1, i*2 + 1, False, scores, target))
    else:
        return min(MinMax(cur+1, i*2, True, scores, target),
                  MinMax(cur+1, i*2+1, True, scores, target))
      
      
      
     # https://github.com/shushrutsharma/18CSC305J-AI
