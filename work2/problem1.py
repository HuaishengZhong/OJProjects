li = []
class LCS():
    global li
    def input(self, x, y):
        if type(x) != str or type(y) != str:
            print('input error')
            return None
        self.x = x
        self.y = y

    def Compute_LCS(self):
        xlength = len(self.x)
        ylength = len(self.y)
        self.direction_list = [None] * xlength
        for i in range(xlength):
            self.direction_list[i] = [None] * ylength
        self.lcslength_list = [None] * (xlength + 1)
        for j in range(xlength + 1):
            self.lcslength_list[j] = [None] * (ylength + 1)

        for i in range(0, xlength + 1):
            self.lcslength_list[i][0] = 0
        for j in range(0, ylength + 1):
            self.lcslength_list[0][j] = 0
        for i in range(1, xlength + 1):
            for j in range(1, ylength + 1):
                if self.x[i - 1] == self.y[j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j - 1] + 1
                    self.direction_list[i - 1][j - 1] = 0  # 左上
                elif self.lcslength_list[i - 1][j] > self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 1  # 上
                elif self.lcslength_list[i - 1][j] < self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i][j - 1]
                    self.direction_list[i - 1][j - 1] = -1  # 左
                else:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 2  # 左或上
        self.lcslength = self.lcslength_list[-1][-1]
        return self.direction_list, self.lcslength_list


    def printLCS(self, curlen, i, j, s):
        if i == 0 or j == 0:
            return None

        if self.direction_list[i - 1][j - 1] == 0:
            if curlen == self.lcslength:
                s += self.x[i - 1]
                li.append(s[::-1])
            elif curlen < self.lcslength:
                s += self.x[i-1]
                self.printLCS(curlen + 1, i - 1, j - 1, s)
        elif self.direction_list[i - 1][j - 1] == 1:
            self.printLCS(curlen, i - 1, j, s)
        elif self.direction_list[i - 1][j - 1] == -1:
            self.printLCS(curlen, i, j - 1, s)
        else:
            self.printLCS(curlen, i - 1, j, s)
            self.printLCS(curlen, i, j - 1, s)


    def returnLCS(self):
        self.printLCS(1, len(self.x), len(self.y), '')

if __name__ == '__main__':
    str1 = input()
    str2 = input()
    p = LCS()
    p.input(str1, str2)
    p.Compute_LCS()
    p.returnLCS()
    for i in set(li):
        print(i)
