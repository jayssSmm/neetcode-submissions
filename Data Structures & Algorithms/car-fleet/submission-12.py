class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''d={}
        for i in range(len(position)):
            d[position[i]]=(target-position[i])/speed[i]
        d=tuple(sorted(d.items(), reverse=True))

        print(d)

        fleet=1
        for index in range(len(d)):
            if index<len(speed)-1 and d[index][1]<d[index+1][1]:
                max = d[index+1]
                fleet+=1 '''

        fleet=0
        max=-1
        d={}
        for i in range(len(speed)):
            time = (target-position[i])/speed[i]
            d[position[i]]=time

        for i in sorted(d.keys(), reverse=True):
            if d[i]>max:
                fleet+=1
                max=d[i]
        

        return fleet