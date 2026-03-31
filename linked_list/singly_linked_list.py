from __future__ import annotations
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """
    A node used in a singly linked list.

    Each node stores a value and a reference to the next node.

    :param value: The value held by the node.
    :type value: T
    :param next: Reference to the next node (or None if this is the last node).
    :type next: Optional[Node[T]]
    :return: None
    :rtype: None
    """

    def __init__(self, value: T, next: Optional[Node[T]] = None) -> None:
        # Use name mangling for "private" fields in Python.
        self.__value: T = value
        self.__next: Optional[Node[T]] = next

    @property
    def value(self) -> T:
        """
        Get the value stored in the node.
        """
        return self.__value

    @value.setter
    def value(self, new_value: T) -> None:
        """
        Set the value stored in the node.
        """
        self.__value = new_value

    @property
    def next(self) -> Optional[Node[T]]:
        """
        Get a reference to the next node (or None if this is the last node).
        """
        return self.__next

    @next.setter
    def next(self, next_node: Optional[Node[T]]) -> None:
        """
        Set a reference to the next node.
        """
        self.__next = next_node


def main() -> None:
    first: Node[int] = Node(1)
    second: Node[int] = Node(2)
    third: Node[int] = Node(3)

    first.next = second
    second.next = third

    if first.next is not None:
        print(f"{first.value} -> {first.next.value}")

    if second.next is not None:
        print(f"{second.value} -> {second.next.value}")


if __name__ == "__main__":
    main()
