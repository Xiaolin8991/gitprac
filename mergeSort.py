class Solution:
    def sortArray(self, nums):
        lo=0
        upp=len(nums)-1
        self.merge_sort(nums,lo,upp)
        return nums


    def merge_sort(self,nums,lo,upp):
        #实现将nums排好序的功能
        #base case 如果相等，则无需排序
        if lo==upp:
            return
        mid=(lo+upp)//2
        self.merge_sort(nums,lo,mid)
        self.merge_sort(nums,mid+1,upp)
        #利用双指针法进行有序数组排序
        i=lo
        j=mid+1
        tmp=[]#对tmp进行更改，最后一次性更改nums
        while i<=mid and j<=upp:
            if nums[j]<nums[i]:
                tmp.append(nums[j])
                j+=1
            elif nums[i]<=nums[j]:
                tmp.append(nums[i])
                i+=1
        if i>mid and j<=upp:
            tmp+=nums[j:upp+1]
        if j>upp and i<=mid:
            tmp+=nums[i:mid+1]
        nums[lo:upp+1]=tmp
if __name__=='__main__':
    tmp=Solution()
    print(tmp.sortArray([-2,3,-5]))

