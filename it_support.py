
import numpy as np

##### TODO #########################################
### IMPLEMENT 'getMyPosition' FUNCTION #############
### TO RUN, RUN 'eval.py' ##########################

nInst = 50 # number of instruments
currentPos = np.zeros(nInst) # current position, initialized to 0

'''
getMyPosition:
    input: prcSoFar, a 2D array of prices
    output: currentPos, a 1D array of positions
    description:
        - if time steps < 2, return 0 for all instruments
        - calculate last return, log of today's price / yesterday's price
        - normalize last return, so that the norm is 1
    this ia  Momentum based strategy, that is, we buy the instrument with the highest return and 
    sell the instrument with the lowest return.
    The position is calculated as 5000 * last return / today's price.
    The current position is updated by adding the new position.
'''

def getMyPosition(prcSoFar): # prcSoFar is a 2D array of prices
    global currentPos # current position
    (nins, nt) = prcSoFar.shape # (n of instruments, n of time steps/days)
    if (nt < 2): # if time steps < 2, return 0
        return np.zeros(nins) # return 0 for all instruments

    #Step 1: CALCULATE YESTERDAYS RETURN
    lastRet = np.log(prcSoFar[:, -1] / prcSoFar[:, -2]) # last return, log of today's price / yesterday's price
    #Step 2: NORMALIZE LAST RETURN
    lNorm = np.sqrt(lastRet.dot(lastRet)) # norm of last return
    lastRet /= lNorm # normalize last return, so that the norm is 1

    #Step 3: CALCULATE POSITION
    rpos = np.array([int(x) for x in 5000 * lastRet / prcSoFar[:, -1]]) # rpos is the position

    #Step 4: UPDATE CURRENT POSITION
    currentPos = np.array([int(x) for x in currentPos+rpos]) # update current position
    return currentPos
