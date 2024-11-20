class Solution(object):
    def generate(self, numRows):

        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        pascal_triangle = self.generate(numRows - 1)
        previous_row = pascal_triangle[-1]
        len_row = len(previous_row)

        current_row = [1]
        
        for index in range(1,len_row):
            current_row.append(previous_row[index] + previous_row[index-1])

        current_row.append(1)
        pascal_triangle.append(current_row)

        return pascal_triangle
