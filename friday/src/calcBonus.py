import numpy as np


def get_bonus_score(allTime, maxM):
    # print(allTime, maxM)
    firstQ = np.percentile(allTime, 25)
    secQ = np.percentile(allTime, 50)
    thirQ = np.percentile(allTime, 75)

    # print(firstQ, secQ, thirQ)

    bScore = []
    for stu in allTime:
        if stu == 0:
            bScore.append(0)
        elif stu <= firstQ:
            bScore.append(maxM)
        elif stu <= secQ:
            bScore.append(0.75 * maxM)
        elif stu <= thirQ:
            bScore.append(0.5 * maxM)
        else:
            bScore.append(0.25 * maxM)
    return bScore
