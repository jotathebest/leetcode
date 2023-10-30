from typing import List


def validateBinaryTreeNodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    parents = [0 for _ in range(n)]
    children = [0 for _ in range(n)]
    roots = set(range(n)) - set(leftChild) - set(rightChild)
    index = 0

    for left, right in zip(leftChild, rightChild):
        if left != -1:
            parents[left] += 1
            children[index] += 1
        if right != -1:
            children[index] += 1
            parents[right] += 1
        index += 1

    # There cannot be more than one root
    if len(roots) != 1:
        return False

    visited = [0] * n
    for index, (parent, child) in enumerate(zip(parents, children)):

        # any node cannot have more than one parent
        if parent:
            visited[index] += 1
        if parent > 1:
            return False
        # any node cannot have more than two children
        if child > 2:
            return False

        if visited[index] > 1:
            return False

    return True


if __name__ == "__main__":
    # assert validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]) is True
    # assert validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]) is False
    # assert validateBinaryTreeNodes(2, [1, 0], [-1, -1]) is False
    # assert validateBinaryTreeNodes(6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]) is False
    # assert validateBinaryTreeNodes(5, [1, 3, -1, -1, -1], [-1, 2, 4, -1, -1]) is True
    # assert validateBinaryTreeNodes(4, [3, -1, 1, -1], [-1, -1, 0, -1]) is True
    assert validateBinaryTreeNodes(4, [1,0,3,-1], [-1,-1,-1,-1]) is False
