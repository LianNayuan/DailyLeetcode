class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank) # 行数
        n = len(bank[0]) # 列数
        count = 0
        a = []
        
        def sum_sta(lst):
            count = 0
            for i in range(len(lst)):
                if lst[i] == '1':
                    count += 1
            return count
        
        for i in range(m):
            b = sum_sta(bank[i])
            if b != 0:
                a.append(b)
        
        if len(a) > 1:
            for j in range(len(a)-1):
                count += a[j]*a[j+1]
            
        return count
