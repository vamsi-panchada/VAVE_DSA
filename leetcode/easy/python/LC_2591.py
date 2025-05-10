class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # failed case if money is less than children so we can't give a $1 to everyone
        if money < children:
            return -1

        # initally we have to distribute the moeny to everyone $1
        money-=children

        # after this every child has exactly $1
        # now we have to find the total possible $7's we have because we need to aim for $8
        # but we already gave $1

        children_with_8 = min(children, money//7)
        
        money -= children_with_8*7

        children_with_1 = children-children_with_8

        if (children_with_1 == 0 and money > 0) or (children_with_1 == 1 and money == 3):
            return children_with_8 - 1
        
        return children_with_8

solution = Solution()
money = int(input())
children = int(input())
print(solution.distMoney(money=money, children=children))