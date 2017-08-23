"""
Interview Practice
File Structure
Binary Tree

            Tatsuya Arai

"""

class Tree(object):
    """Binary Tree"""
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None



from collections import Counter          
def restoreBinaryTree(inorder, preorder):
    """Inorder and preorder lsts to Binary Tree"""
    if len(inorder) == 1:
        T = Tree(preorder[0])
    elif len(inorder) == 2:
        T = Tree(preorder[0])
        if inorder == preorder:
            T.right = restoreBinaryTree([inorder[1]], [preorder[1]])
        else:
            T.left = restoreBinaryTree([inorder[1]], [preorder[1]])            
    else:
        T = Tree(preorder[0])
        for i0 in range(len(preorder)):
            if inorder[i0] == preorder[0] and Counter(inorder[:i0]) == Counter(preorder[1:1+i0]):
                T.left = restoreBinaryTree(inorder[:i0], preorder[1:1+i0])
                T.right = restoreBinaryTree(inorder[i0+1:], preorder[1+i0:])
                break
    return T


inorder = [4, 2, 1, 5, 3, 6]
preorder = [1, 2, 4, 3, 5, 6]

T = restoreBinaryTree(inorder, preorder)

inorder2 = [2, 5]
preorder2 = [5, 2]

T2 = restoreBinaryTree(inorder2, preorder2)

#inorder3 = [1, 1, 1, 1, 1]
#preorder3 = [1, 1, 1, 1, 1]

#T3 = restoreBinaryTree(inorder3, preorder3)


def flatTreeInorder(Tree):
    """Binary Tree to Inorder lst"""
    if not Tree: return []
    return flatTreeInorder(Tree.left) + [Tree.value] + flatTreeInorder(Tree.right)

def flatTreePreorder(Tree):
    """Binary Tree to Inorder lst"""
    if not Tree: return []
    return [Tree.value] + flatTreePreorder(Tree.left) + flatTreePreorder(Tree.right)

flatTreeInorder(T) == inorder
flatTreePreorder(T) == preorder

def minimalBST(lst):
    """time: O(n) space: O(n)"""
    if not lst: return None
    lst = sorted(lst)
    middle = len(lst) // 2
    T = Tree(lst[middle])
    T.left = minimalBST(lst[:middle])
    T.right = minimalBST(lst[middle+1:])
    return T

lst = [1,4,2,3,6,5,7]
mBST = minimalBST(lst)

mBST_in = flatTreeInorder(mBST)
mBST_in
mBST_pre = flatTreePreorder(mBST)
mBST_pre

mBST2 = restoreBinaryTree(mBST_in, mBST_pre)

def isTreeIdentical(T1,T2):
    if not T1 and T2: return False
    if not T2 and T1: return False
    if not T2 and not T1: return True
    return (T1.value == T2.value 
    and isTreeIdentical(T1.left,T2.left) 
    and isTreeIdentical(T1.right,T2.right))


isTreeIdentical(mBST,mBST2)


### BST
# Tree.left.value < Tree.value < Tree.right.value
def isTreeBST(T, minval=float('-inf'), maxval=float('+inf')):
    """time: O(n) space: O(n)"""
    return ((minval < T.value < maxval)
            ### Left Hand Side: T.value is the largest
            and (not T.left or isTreeBST(T.left, minval, T.value))
            ### Right Hand Side: T.value is the smallest
            and (not T.right or isTreeBST(T.right, T.value, maxval))) 


isTreeBST(mBST)



# Grouping node values by depth. 
def lstByDepth(T, depth = 0, d = {}):
    if T: 
        if depth not in d:
            d[depth] = [T.value]
        else:
            d[depth] += [T.value]
        #print(depth)
        depth += 1
        lstByDepth(T.right, depth, d)
        lstByDepth(T.left, depth, d)
    return d



dBD_mBST = lstByDepth(mBST,0,{})
dBD_T = lstByDepth(T,0,{})



def lstLeaf(T, lst = []):
    if T:
        if not T.left and not T.right:
            lst += [T.value]
        elif T.left and not T.right:
            lstLeaf(T.left,lst)
        elif T.right and not T.left:
            lstLeaf(T.right,lst)
        else:
            lstLeaf(T.left,lst)
            lstLeaf(T.right, lst)
    return lst


lstLeaf(T,[])
lstLeaf(mBST,[])



def lstNodeSum(T, s = 0, lst = []):
    if T:
        if not T.left and not T.right:
            s += T.value
            lst += [s]
        elif T.left and not T.right:
            lstNodeSum(T.left, s + T.value, lst)
        elif T.right and not T.left:
            lstNodeSum(T.right, s + T.value, lst)
        else:
            lstNodeSum(T.left, s + T.value, lst)
            lstNodeSum(T.right, s + T.value, lst)
    return lst

lstNodeSum(T, 0, [])
lstNodeSum(mBST, 0, [])


def lstTreePath(T, lst_sub = [], lst = []):
    if T:
        if not T.left and not T.right:
            lst.append(lst_sub + [T.value])
        elif T.left and not T.right:
            lstTreePath(T.left, lst_sub + [T.value], lst)
        elif T.right and not T.left:
            lstTreePath(T.right, lst_sub + [T.value], lst)
        else:
            lstTreePath(T.left, lst_sub + [T.value], lst)
            lstTreePath(T.right, lst_sub + [T.value], lst)
    return lst

lstTreePath(T, [], [])
lstTreePath(mBST, 0, [])





