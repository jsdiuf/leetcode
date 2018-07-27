/**
 * @author weicc
 * @create 2018-07-27 12:26
 * <p>
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 * <p>
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * <p>
 * Example:
 * <p>
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 * <p>
 * https://leetcode.com/problems/add-two-numbers/description/
 **/
public class Ad_Two_Numbers {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode p1 = l1, p2 = l2;

        int carry = 0;
        while (p1 != null && p2 != null) {
            int sum = p1.val + p2.val + carry;
            p1.val = sum % 10;
            p2.val = sum % 10;

            carry = (sum >= 10 ? 1 : 0);

            //同时走到头了 且有进位
            if (p1.next == null && p2.next == null&&carry==1) {
                p1.next = new ListNode(1);
                return l1;
            }

            p1 = p1.next;
            p2 = p2.next;

        }


        if (p1 != null) {
            while (p1 != null) {
                int sum = p1.val + carry;
                p1.val = sum % 10;

                carry = (sum >= 10 ? 1 : 0);

                if (p1.next == null && carry == 1) {
                    p1.next = new ListNode(1);
                    return l1;
                }
                p1 = p1.next;
            }
            return l1;
        } else {
            while (p2 != null) {
                int sum = p2.val + carry;
                p2.val = sum % 10;

                carry = (sum >= 10 ? 1 : 0);

                if (p2.next == null && carry == 1) {
                    p2.next = new ListNode(1);
                    return l2;
                }
                p2 = p2.next;
            }
            return l2;
        }


    }

    public static void main(String[] args) {
        ListNode node1 = new ListNode(2);
        ListNode node2 = new ListNode(4);
        ListNode node3 = new ListNode(3);
        node1.next = node2;
        node2.next = node3;

        ListNode node4 = new ListNode(5);
        ListNode node5 = new ListNode(6);
        ListNode node6 = new ListNode(4);
        ListNode node7 = new ListNode(9);
        node4.next = node5;
        node5.next = node6;
        //node6.next = node7;

        ListNode re = addTwoNumbers(node1, node4);
        System.out.println(re);
    }
}
