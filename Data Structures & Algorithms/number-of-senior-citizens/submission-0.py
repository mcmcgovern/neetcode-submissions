class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # index 0:9 phone
        # index 10 gender
        # index 11:12 age
        # index 13: seat
        num_seniors = 0

        for s in details:
            if int(s[11:13]) > 60:
                num_seniors += 1

        return num_seniors