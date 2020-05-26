# both of the given code are correct


# code one


# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the saveThePrisoner function below.
# def saveThePrisoner(n, m, s):
    
#     if (s - 1 + m) % n==0:
#         return n
#     else:
#         return (s - 1 + m) % n

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         nms = input().split()

#         n = int(nms[0])

#         m = int(nms[1])

#         s = int(nms[2])

#         result = saveThePrisoner(n, m, s)

#         fptr.write(str(result) + '\n')

#     fptr.close()



# -------------------------or---------------------------------------


# code two

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    
    return (s - 2 + m) % n + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
