class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # prod = None
        # zero = False

        # for i in range(len(nums)):
        #     if not nums[i]:
        #         if zero: # second_zero case
        #             for i in range(len(nums)):
        #                 output.append(0)
        #             return output
        #         zero = True
        #         continue
        #     if prod is None:
        #         prod = nums[i]
        #     else:
        #         prod *= nums[i]
        
        # for i in range(len(nums)):
        #     if zero:
        #         if prod is None:
        #             prod = 0
        #         if not nums[i]:
        #             output.append(prod)
        #         else:
        #             output.append(0)
        #     else:
        #         output.append(prod//nums[i])

        # return output

        output = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= post
            post *= nums[i]
        
        return output


        