class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        amounts = []
        for i in accounts:
            amounts.append(sum(accounts[i]))
        return max(amounts)
    
