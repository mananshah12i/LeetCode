class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        inv=[]
        for i in image:
            inv.append(i[::-1])
        print(inv)
        for i in range(len(image)):
            for j in range(len(image)):
                if inv[i][j]==0:
                    inv[i][j]=1
                else:
                    inv[i][j]=0
        return inv