class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        previous_row = self.getRow(rowIndex-1)

        current_row = [1]
        for i in range(1,len(previous_row)):
            current_row.append(previous_row[i] + previous_row[i-1])

        current_row.append(1)
        return current_row
        
