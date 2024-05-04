# EQUALITY IN STRINGS

## Approach 1

Below are the steps to determine whether the string contains an equal number of `A` and `B`:

Step 1: Add `M` to the start and end of the string.

Step 2: Begin an infinite loop with a pointer starting at the first character in the string.

Step 3: If the pointer encounters `A` first, proceed to Step 4. If it encounters `B` first, proceed to Step 5. If it encounters `M` first, proceed to Step 7. Otherwise, increment the pointer until encountering either `A`, `B`, or `M`.

Step 4:  
- Replace `A` with `X`.
- Ignore `X`.
- Ignore `A`.
- Increment pointer until encountering `B`.
- Replace `B` with `X`.
- Set the pointer to the start of the string.
- If `B` is not encountered and the pointer reaches `M`, proceed to Step 8.
- Skip Step 5.

Step 5:  
- Replace `B` with `X`.
- Ignore `X`.
- Ignore `B`.
- Increment pointer until encountering `A`.
- Replace `A` with `X`.
- Set the pointer to the start of the string.
- If `A` is not encountered and the pointer reaches `M`, proceed to Step 8.

Step 6: Do Step 3.

Step 7: Return True.

Step 8: Return False.

## Approach 2

Below are the steps to determine whether the string contains an equal number of A and B:

Step 1: Initialize a key variable and an empty stack.

Step 2: Begin a loop to cover the entire string.

Step 3: If the length of the stack is 0 and the key is not equal to the current element, store the current element in the key and push the key to the stack.

Step 4: Else if the current element is not equal to the key, pop a value from the stack.

Step 5: Else push the key to the stack.

Step 6: At the end of the loop, if the length of the stack is 0, return True; otherwise, return False.
