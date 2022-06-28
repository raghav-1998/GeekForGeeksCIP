class Solution:
    def minDeletions(self, s: str) -> int:
        mp = {}
        
        N=len(s)
 
    # Store frequency of each distinct
    # character such that the largest
    # frequency is present at the top
        pq = []

        # Stores minimum count of characters
        # required to be deleted to make
        # frequency of each character unique
        cntChar = 0

        # Traverse the string
        for i in range(N):

            # Update frequency of str[i]
            mp[s[i]] = mp.get(s[i], 0) + 1

        # Traverse the map
        for it in mp:

            # Insert current
            # frequency into pq
            pq.append(mp[it])

        pq = sorted(pq)

        # Traverse the priority_queue
        while (len(pq) > 0):

            # Stores topmost
            # element of pq
            frequent = pq[-1]

            # Pop the topmost element
            del pq[-1]

            # If pq is empty
            if (len(pq) == 0):

                # Return cntChar
                return cntChar

            # If frequent and topmost
            # element of pq are equal
            if (frequent == pq[-1]):

                # If frequency of the topmost
                # element is greater than 1
                if (frequent > 1):

                    # Insert the decremented
                    # value of frequent
                    pq.append(frequent - 1)

                # Update cntChar
                cntChar += 1

            pq = sorted(pq)

        return cntChar