class Solution:

#----------------------------------------------------------------------------------------
# 0013

    def romanToInt(self, s: str) -> int:
        dict = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
        sum = 0
        previous = 0
        for char in s:
            now = dict[char]
            if now <= previous:
                sum += now
            else:
                sum += (now-2*previous)
            previous = now
        return sum
    
	# 像这种需要对比序列内元素前后关系的情况下，用range来循环会更好一点，因为这样的话，在每一次循环中，序列中的每个元素都是可以被调用的
	# 相比我上一种做法，我不需要专门把之前的数字储存起来用作下一次循环的对比，而且也不需要，用减去两倍的先前值这样的操作来抵消之前的误操作，科学多了
    # def romanToInt_0(self, s: str) -> int:
    #     romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     res = 0
    #     for i in range(len(s)-1):
    #         if romans[s[i]]  < romans[s[i+1]]:
    #             res -= romans[s[i]]
    #         else:
    #             res += romans[s[i]]
    #     res += romans[s[len(s)-1]

#----------------------------------------------------------------------------------------
# 0014

	# 最简单粗暴的一个一个对比
    def longestCommonPrefix_0(self, strs: List[str]) -> str:
        ans = ''
        
        # empty input case:
        if len(strs) == 0: return ans
        
        # single input case:
        elif len(strs) ==1: return strs[0]
        
        
                # empty input case:
        if len(strs) == 0: return ans
        
        # single input case:
        elif len(strs) ==1: return strs[0]
        
        # normal case:
        else:
            for i in range(len(strs[0])):
                flag = 0 
                for str in strs[1:]:
                    # if compared string is shorter than current position
                    # OR: characters not matched
                    if len(str)<i+1 or str[i]!=strs[0][i]:
                        flag = 1
                        break
                if flag == 0:
                    ans += strs[0][i]
                else:
                    break
            return ans
        
        
#         # normal case (by using while()):
#         else:
#             for i in range(len(strs[0])):
#                 current = 1
#                 MATCHED = True
#                 while(current<=len(strs)-1):
#                     # if compared string is shorter than current position
#                     # OR: characters not matched, then break
#                     if len(strs[current])<i+1 or strs[current][i]!=strs[0][i]:
#                         MATCHED = False
#                         break
#                     current += 1
#                 if MATCHED:   
#                     ans += strs[0][i]
#                 else:
#                     break
#             return ans

    # python有太多方便的用法了……像这个min，就可以直接把数组里最短长度的元素找出来了
    # 然后下面这个all的用法，我一开始也想到了，但是语法不会用
    # 思路和我是一样的
    def longestCommonPrefix_1(self, strs):
        prefix=""
        if len(strs)==0: return prefix
        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i]==c for a in strs):
                prefix+=c
            else:
                break
        return prefix
    
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort() # string的sorting居然是根据元素的长度排序，有点神奇
        p = ""
        # 我去zip这个函数简直就是为了这种情况量身定做的啊
        # 这种只对比最长和最短的两个的手法简直神来之笔啊，太厉害了
        for x, y in zip(strs[0], strs[-1]):
            if x == y: p+=x
            else: break
        return p

#----------------------------------------------------------------------------------------
# 0020

	# with stack processing
    def isValid(self, s: str) -> bool:
        dict = {
            ')':'(',
            ']':'[',
            '}':'{',
            '(':None,
            '[':None,
            '{':None
        }
        stack = []
        for char in s:
            if len(stack)==0 or stack[0]!=dict[char]:
                stack.insert(0,char)
            else:
                del stack[0]
        if len(stack) == 0:
            return True
        else:
            return False
        
    ## with string processing    
    # def isValid(self, s):
    #     while "()" in s or "{}" in s or '[]' in s:
    #         s = s.replace("()", "").replace('{}', "").replace('[]', "")
    #     return s == ''

#----------------------------------------------------------------------------------------
# 0021

	# Definition for singly-linked list
	class ListNode:
	    def __init__(self, val=0, next=None):
	        self.val = val
	        self.next = next

	# def extract_val(nodelist):
    #     val_list = []
    #     while nodelist != None:
    #         val_list.insert(0,nodelist.val)
    #         nodelist = nodelist.next
    #     return val_list
    #
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     l1v = extract_val(l1)
    #     l2v = extract_val(l2)
    #     newlist = l1v+l2v
    #     newlist.sort()
    #     newlist.reverse()
    #     result = None
    #     for v in newlist:
    #         result = ListNode(v,result)
    #     return result
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        while(l1!=None and l2!=None):
            if l1.val <= l2.val:
                result.insert(0,l1.val)
                l1 = l1.next
            else:
                result.insert(0,l2.val)
                l2 = l2.next
                
        if l1 == None:
            while(l2!=None):
                result.insert(0,l2.val)
                l2 = l2.next
        elif l2 == None:
            while(l1!=None):
                result.insert(0,l1.val)
                l1 = l1.next
        
        out = None
        for v in result:
            out = ListNode(v,out)
        return out

#----------------------------------------------------------------------------------------
# 0026

	class Solution:
	    
	    # def removeDuplicates(self, nums: List[int]) -> int:
	    #     for elem in nums:
	    #         for i in range(nums.count(elem)-1):
	    #             nums.remove(elem)
	    #     return len(nums)
	    
	    def removeDuplicates(self, nums: List[int]) -> int:
	        i = 0
	        while i+1 < len(nums):
	            while nums[i] == nums[i+1]:
	                del nums[i+1]
	                if i+1 >= len(nums): break
	            i += 1
	        return len(nums)

#----------------------------------------------------------------------------------------
# 0027

	def removeElement(self, nums: List[int], val: int) -> int:
		        while val in nums:
		            nums.remove(val)
		        return (len(nums))
		        
		    # def removeElement(self, nums: List[int], val: int) -> int:
		    #     count = 0
		    #     for i in range(len(nums)):
		    #         if nums[i] != val :
		    #             nums[count] = nums[i]
		    #             count +=1
		    #     return count

#----------------------------------------------------------------------------------------
# 0028

	# def strStr(self, haystack: str, needle: str) -> int:
	    #     if len(needle) == 0 : return 0
	    #     elif len(haystack)==0 or len(haystack)<len(needle): return -1
	    #     elif len(needle) == len(haystack): 
	    #         if needle == haystack: return 0
	    #         else: return -1
	    #     for i in range(len(haystack)-len(needle)+1):
	    #         if haystack[i]==needle[0]:
	    #             j = 1
	    #             flag = 1
	    #             while j<len(needle):
	    #                 if haystack[i+j]!=needle[j]:
	    #                     flag = 0
	    #                     break
	    #                 j += 1
	    #             if flag == 1:
	    #                 return i
	    #     return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == '' and needle != '':
            return -1
        if needle == '':
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

#----------------------------------------------------------------------------------------
# 0035

	def searchInsert(self, nums: List[int], target: int) -> int:
	        for i in range(len(nums)):
	            if nums[i] >= target: return i
	        return len(nums)
	    
	    # def searchInsert(self, nums: List[int], target: int) -> int:
	    #     index = 0
	    #     for n in nums:
	    #         if n >= target: return index
	    #         index += 1
	    #     return len(nums)
	        
	    
	    # def searchInsert(self, nums: List[int], target: int) -> int:
	    #     if target in nums: 
	    #         return nums.index(target)
	    #     else:
	    #         nums.append(target)
	    #         nums.sort()
	    #         return nums.index(target)

#----------------------------------------------------------------------------------------
# 0038

	def next_num(string):
	    out = ''
	    index  = 0
	    while index < len(string):
	        step = 1       
	        if index == len(string)-1:
	            out += str(step)+string[index]
	            break
	        else:
	            while index+step < len(string):      
	                if string[index+step] == string[index]:
	                    step += 1
	                else: 
	                    break
	            out += str(step)+string[index]
	        index += step
	    return out

    def countAndSay(self, n: int) -> str:
        now = '1'
        if n == 1:
            return now
        for i in range(n-1):
            now = next_num(now)
        return now


#----------------------------------------------------------------------------------------
# 0053

    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, min_so_far, max_sub = 0, 0, float('-inf')
        for ele in nums:
            cur_sum += ele 
            max_sub, min_so_far= max(cur_sum - min_so_far, max_sub), min(min_so_far, cur_sum) 
        return max_sub

#----------------------------------------------------------------------------------------
# 0058

	def lengthOfLastWord(self, s: str) -> int:
        end = -1
        new = s.split(' ')
        while len(new[end]) == 0 and end != -len(new):
            end -= 1
        return len(new[end])

#----------------------------------------------------------------------------------------
# 0066

    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for num in digits:
            string += str(num)
        new = str(int(string) + 1)
        out = []
        for char in new:
            out.append(int(char))
        return out
    
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     end = -1
    #     digits[end] += 1
    #     while digits[end] > 9:
    #         digits[end] = 0
    #         end -= 1
    #         if -end > len(digits):
    #             break
    #         else:
    #             digits[end] += 1 
    #     if digits[0] == 0:
    #         digits.insert(0,1)
    #     return digits

#----------------------------------------------------------------------------------------
# 0067

	# def addBinary(self, a: str, b: str) -> str:
	    #     diff = len(a)-len(b)
	    #     if diff > 0:
	    #         unchanged = a[:diff]
	    #         a = a[diff:]
	    #     elif diff < 0:
	    #         unchanged = b[:-diff]
	    #         b = b[-diff:]
	    #     else:
	    #         unchanged = ''
	    #     c = 0
	    #     new = ''
	    #     for i in range(1,len(a)+1):
	    #         new_num = int(a[-i]) + int(b[-i]) + c
	    #         c = new_num // 2
	    #         new_num = new_num % 2
	    #         new = str(new_num) + new
	    #     for i in range(1,len(unchanged)+1):
	    #         new_num = int(unchanged[-i]) + c
	    #         c = new_num // 2
	    #         new_num = new_num % 2
	    #         new = str(new_num) + new
	    #     if c != 0:
	    #         new = '1' + new
	    #     return new
    
    def addBinary(self, a: str, b: str) -> str:
        temp = bin(int(a,2) + int(b,2))
        return temp[temp.index("b")+1:]

#----------------------------------------------------------------------------------------
# 0069

	 # def mySqrt(self, x: int) -> int:
	    #     return int(sqrt(x))
    
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        down = 0
        up = x
        now = x // 2
        while up != down+1:
            while now*now > x:
                up = now
                now = down + (now-down) // 2
            down = now
            now = up
        return down

#----------------------------------------------------------------------------------------
# 0070

#     def climbStairs(self, n: int) -> int:
#         def A(n):
#             res = 1
#             for i in range(1,n+1):
#                 res *= i
#             return res

#         ways = 0
#         for x in range(n+1):
#             if (n-x) % 2 == 0:
#                 y = int((n-x) / 2) 
#                 ways += A(x+y)/(A(x)*A(y))
                    
#         return int(ways)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        from_1, from_2 = 1, 1
        for i in range(n-1):
            from_1, from_2 = from_2, from_2+from_1
        return from_2

#----------------------------------------------------------------------------------------
# 0083 

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = head
        now = head.next
        while now != None:
            if now.val == prev.val:
                prev.next = now.next
                now = now.next
            else:
                prev = now
                now = now.next
        return head

#----------------------------------------------------------------------------------------
# 0088

    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     for i in range(n):
    #         nums1.pop(-1)
    #     for v in nums2:
    #         nums1.append(v)
    #     nums1.sort()
    #     return nums1
    
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1,p2=0,0
        temp=nums1.copy() #copied num1 to temp
        nums1.clear() #make num1 as empty list
        while(p1<m and p2<n):
            if (temp[p1]<nums2[p2]):
                nums1.append(temp[p1])
                p1+=1
            else:
                nums1.append(nums2[p2]) 
                p2+=1
        while(p1<m):
            nums1.append(temp[p1])
            p1+=1
        while(p2<n):
            nums1.append(nums2[p2])
            p2+=1

#----------------------------------------------------------------------------------------
# 0100

	# Definition for a binary tree node.
	class TreeNode:
	    def __init__(self, val=0, left=None, right=None):
	        self.val = val
	        self.left = left
	        self.right = right
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # p and q are both None
        if not p and not q: # 这种直接用对None来操作的手法要记住
            return True
        
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        
        # both p and q are not None and equal
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

	'''
	使用递归的时候，函数的操作越精简越好
	啥也不要管，直接扔给他做操作就好了
	'''   

#----------------------------------------------------------------------------------------
# 0101

#     def isSymmetric(self, root: TreeNode) -> bool:       
#         def box_check(box):
#             while len(box)!=0:
#                 if box[0] != box[-1]:
#                     return False
#                 else:
#                     box.pop(0)
#                     box.pop(-1)
#             return True
    
#         def birth_check(nodelist):
#             check_box = []
#             node_box = []
#             for parents in nodelist:
#                 if not parents: 
#                     return
#                 else:                    
#                     if not parents.left: 
#                         check_box.append('X')
#                     else: 
#                         check_box.append(parents.left.val)
#                         node_box.append(parents.left)
#                     if not parents.right: 
#                         check_box.append('X')
#                     else: 
#                         check_box.append(parents.right.val)
#                         node_box.append(parents.right)
#             return node_box, check_box
#         if not root:
#             return True
#         son = [root]
#         flag = True
#         while len(son) != 0:
#             son,check_box = birth_check(son)
#             if not box_check(check_box):
#                 return False
#         return True
        
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val==t2.val) and isMirror(t1.right,t2.left) and isMirror(t1.left,t2.right)
        return isMirror(root,root)

#----------------------------------------------------------------------------------------
# 0104

    # def maxDepth(self, root: TreeNode) -> int:
    #     def walk(root,box,depth):
    #         if not root: 
    #             return box
    #         box.append(depth)
    #         depth += 1
    #         box = walk(root.left,box,depth)
    #         box = walk(root.right,box,depth)
    #         return box
    #     box =[]
    #     depth = 1
    #     walks = walk(root,box,1)
    #     if len(walks)==0: return 0
    #     else: return max(walks)
        
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0;
        if not root.left and not root.right: return 1
        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth

#----------------------------------------------------------------------------------------
# 0107

#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         def birth(root_list,box):
#             son = []
#             this_run = []
#             for root in root_list:
#                 small_box = []
#                 if not root: continue
                    
#                 if not root.left: 
#                     son.append(None)
#                 else:
#                     son.append(root.left)
#                     small_box.append(root.left.val)
#                 if not root.right:
#                     son.append(None)
#                 else:
#                     son.append(root.right)
#                     small_box.append(root.right.val)

#                 if len(small_box)!=0:
#                     this_run += small_box
#             if len(this_run)!= 0:
#                 box.append(this_run)
#             return son,box
        
#         if not root: return []
#         else:
#             son = [root]
#             box = [[root.val]]
#             while len(son)!=0:
#                 son,box = birth(son,box)
#             box.reverse()
#             return box


    # stack methods
    # 括号套括号的方式不可避免
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = [root] # It captures the root node at the very beginning.
        levelOutput = [] # It captures the node values that are at the same level.
        output = [] # End result
        if root is None: # If the root is empty, return None.
            return (None)
        while stack:
            slen = len(stack)
            while slen > 0: # Keep traversing at the same level.
                temp = stack.pop(0)
                levelOutput.append(temp.val)
                if temp.left != None:
                    stack.append(temp.left)
                if temp.right != None:
                    stack.append(temp.right)
                slen -= 1
            output.append(levelOutput.copy())
            levelOutput.clear()
        return(output[::-1]) # Reverse the 2D list.

#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------

