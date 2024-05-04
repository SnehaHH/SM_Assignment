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


